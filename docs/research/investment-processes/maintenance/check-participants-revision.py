"""Compare the revision with the exact PR 41 snapshot. Standard library only."""

import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[4]
BASE = "c1ba6b4053c178e3ea38b2237c970fae60ff981d"
PREFIX = "docs/research/investment-processes/"
EDITABLE = {
    "docs/research/README.md",
    PREFIX + "README.md",
    PREFIX + "participants-summary.md",
    PREFIX + "participants.md",
    PREFIX + "participant-cases.md",
}
MAINTENANCE = PREFIX + "maintenance/"


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def original(path):
    return git("show", BASE + ":" + path)


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def anchors(text):
    result = set(re.findall(r'<a\s+(?:name|id)="([^"]+)"', text))
    counts = {}
    for title in re.findall(r"^#{1,6}\s+(.+)$", text, re.M):
        title = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", title)
        slug = re.sub(r"[^\w\s-]", "", title.lower()).replace(" ", "-")
        n = counts.get(slug, 0)
        counts[slug] = n + 1
        result.add(slug + ("-" + str(n) if n else ""))
    return result


def cases(text):
    result = {}
    pattern = r'<a name="([^"]+)"></a>\s*\n## (\d+)\. ([^\n]+)\n(.*?)(?=\n<a name=|\nВсе карточки|\Z)'
    for anchor, number, title, body in re.findall(pattern, text, re.S):
        rows = [line for line in body.splitlines() if line.startswith("| ")]
        result[anchor] = {"number": int(number), "title": title, "rows": rows}
    return result


def roles(text):
    result = {}
    for line in text.splitlines():
        match = re.search(r'<a name="role-([ps]\d+)">', line)
        if match:
            if match[1] in result:
                raise AssertionError("Duplicate role: " + match[1])
            result[match[1]] = line.split("|")[1:-1]
    return result


def main():
    errors = []
    baseline_files = git("ls-tree", "-r", "--name-only", BASE).decode().splitlines()
    protected = []
    for path in baseline_files:
        target = ROOT / path
        if path not in EDITABLE:
            # Compare Git's canonical content, respecting Windows checkout EOL filters.
            expected = git("rev-parse", BASE + ":" + path).strip()
            actual = git("hash-object", "--path=" + path, str(target)).strip() if target.is_file() else None
            if actual != expected:
                errors.append("Protected file changed or missing: " + path)
            else:
                protected.append(path)
    untracked = git("ls-files", "--others", "--exclude-standard", "-z").decode().split("\0")
    changed = git("diff", "--name-only", BASE).decode().splitlines()
    for path in changed + untracked:
        if path and path not in EDITABLE and not path.startswith(MAINTENANCE):
            errors.append("Unexpected scope: " + path)

    old_cases = cases(original(PREFIX + "participant-cases.md").decode())
    new_cases = cases(read(PREFIX + "participant-cases.md"))
    if len(old_cases) != 16 or old_cases != new_cases:
        errors.append("The 16 original case tables or headings changed")
    old_index = original(PREFIX + "participant-cases.md").decode().split('<a name="bonds"></a>')[0]
    for anchor, result in re.findall(r'\| \[[^]]+\]\(#([^)]*)\) \| (.*?) \|', old_index):
        if result.rstrip(".") not in "\n".join(new_cases.get(anchor, {}).get("rows", [])):
            errors.append("Result removed from case index is absent from full card: " + anchor)
    old_roles = roles(original(PREFIX + "participants.md").decode())
    new_roles = roles(read(PREFIX + "participants.md"))
    expected_roles = {f"p{i:02}" for i in range(1, 26)} | {f"s{i:02}" for i in range(1, 15)}
    if set(old_roles) != expected_roles or set(new_roles) != expected_roles:
        errors.append("Expected 25 processes and 14 support functions exactly once")
    details = read(PREFIX + "details.md")
    for key in sorted(expected_roles):
        before, after = old_roles.get(key, []), new_roles.get(key, [])
        if len(before) != 4 or len(after) != 4 or before[1:] != after[1:]:
            errors.append("Role, work, recipient or depth changed: " + key)
            continue
        example = re.search(r"\. Пример: (.*?) \[Документ карты\]", before[0])
        if not example or example[1] not in details:
            errors.append("Removed example absent from intact process card: " + key)
        old_links = re.findall(r"\]\(([^)]+)\)", before[0])
        if old_links != re.findall(r"\]\(([^)]+)\)", after[0]):
            errors.append("Process or source link changed: " + key)

    summary = read(PREFIX + "participants-summary.md")
    overview = summary.split("## Какие ситуации углубить сначала")[0]
    overview_links = re.findall(r"participant-cases\.md#([\w-]+)", overview)
    if len(overview_links) != 16 or set(overview_links) != set(old_cases):
        errors.append("Overview must show all 16 cases exactly once")
    first_pass = summary.split("## Какие ситуации углубить сначала")[1].split("## Что передаётся")[0]
    shortlist = re.findall(r"participant-cases\.md#([\w-]+)", first_pass)
    if shortlist != ["bonds", "disclosure", "matching"]:
        errors.append("First-pass directions missing or repeated")

    checked_links = 0
    for path in sorted(EDITABLE):
        text = read(path)
        for target in re.findall(r"\]\(([^)\s]+)\)", text):
            if re.match(r"[a-z]+:", target):
                continue
            filename, _, fragment = unquote(target).partition("#")
            destination = ((ROOT / path).parent / filename).resolve() if filename else ROOT / path
            if not destination.is_file():
                errors.append(f"Missing local file: {path}: {target}")
            elif fragment and destination.suffix == ".md" and fragment not in anchors(destination.read_text(encoding="utf-8")):
                errors.append(f"Missing anchor: {path}: {target}")
            checked_links += 1
        explicit = re.findall(r'<a\s+(?:name|id)="([^"]+)"', text)
        if len(explicit) != len(set(explicit)):
            errors.append("Duplicate explicit anchor: " + path)

    diff = git("diff", "--unified=0", BASE, "--", *sorted(EDITABLE)).decode()
    for line in diff.splitlines():
        if line.startswith("+") and not line.startswith("+++"):
            if any(symbol in line for symbol in ["—", "→", "←", "↑", "↓", "·", ";"]):
                errors.append("Disallowed separator in added text: " + line[:110])

    case_report = []
    for anchor, case in new_cases.items():
        case_report.append({"anchor": anchor, "number": case["number"], "title": case["title"],
                            "table_sha256": hashlib.sha256("\n".join(case["rows"]).encode()).hexdigest(),
                            "preserved": old_cases.get(anchor) == case,
                            "overview_occurrences": overview_links.count(anchor)})
    report = {"baseline_commit": BASE, "comparison": "Git blob identity after checkout filters, including Windows line endings", "errors": errors,
              "protected_files_unchanged": protected,
              "processes": sorted(new_roles), "cases": case_report,
              "local_links_checked": checked_links,
              "first_pass": shortlist,
              "limitations": ["Link checks cover edited Markdown and its local targets.",
                              "No claim of complete source verification or user comprehension testing.",
                              "No GitHub branch or issue state is changed by this script."]}
    if len(sys.argv) == 2:
        destination = Path(sys.argv[1])
        if not destination.is_absolute():
            destination = ROOT / destination
        destination.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"errors": errors, "protected_files": len(protected),
                      "roles": len(new_roles), "cases": len(new_cases),
                      "local_links_checked": checked_links}, ensure_ascii=False))
    return int(bool(errors))


if __name__ == "__main__":
    sys.exit(main())
