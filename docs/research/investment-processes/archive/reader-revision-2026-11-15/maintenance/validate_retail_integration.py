"""Validate the HTML integration using only the Python standard library.

Run from any directory: python path/to/validate_retail_integration.py
The check is read-only and can be rerun after this PR is committed.
"""
from collections import Counter
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import json
import re
import subprocess
import unicodedata


ROOT = Path(__file__).resolve().parents[4]
P = ROOT / 'docs/research/investment-processes'
MAPPING = P / 'maintenance/retail-investors-mapping.json'
mapping = json.loads(MAPPING.read_text(encoding='utf-8'))
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


def git(*args):
    return subprocess.run(['git', *args], cwd=ROOT, check=True,
                          capture_output=True, encoding='utf-8').stdout


class SourceParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.sources = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'source-card' in attrs.get('class', '').split():
            self.sources.append(json.loads(attrs['data-search']))


archive = P / 'archive/retail-investors-2026-11-15/Russia_Retail_Investors_CJM.html'
raw = archive.read_bytes()
check(hashlib.sha256(raw).hexdigest() == mapping['source_sha256'], 'Archive SHA-256 mismatch')
# Check the stored Git blob as well: core.autocrlf must not normalize this archive.
arch_rel = archive.relative_to(ROOT).as_posix()
blob = subprocess.run(['git', 'show', 'HEAD:' + arch_rel], cwd=ROOT, capture_output=True)
if blob.returncode == 0:
    check(hashlib.sha256(blob.stdout).hexdigest() == mapping['source_sha256'],
          'Committed archive blob does not preserve the supplied bytes')
source_html = raw.decode('utf-8')
scenario_json = re.search(r'<script\b[^>]*\bid="scenario-data"[^>]*>(.*?)</script>', source_html, re.S)
source_scenarios = json.loads(scenario_json.group(1))
parser = SourceParser()
parser.feed(source_html)
source_ids = {s['id'] for s in parser.sources}
scenario_ids = {s['id'] for s in source_scenarios}
check(len(source_scenarios) == 50 and len(scenario_ids) == 50, 'Expected 50 distinct source scenarios')
check(len(parser.sources) == 51 and len(source_ids) == 51, 'Expected 51 distinct source records')
check(sum(s['used_in_report'] for s in parser.sources) == 48, 'Expected 48 report sources')
check({m['id'] for m in mapping['scenarios']} == scenario_ids, 'Mapping does not cover source IDs')
check(len(mapping['scenarios']) == 50, 'Mapping contains duplicate scenario rows')
check({m['id'] for m in mapping['sources']} == source_ids, 'Source mapping does not cover registry')
check(sum(m['decision'] == 'Объединён' for m in mapping['scenarios']) == 7, 'Expected 7 merged IDs')
check(sum(m['decision'] == 'Добавлен' for m in mapping['scenarios']) == 43, 'Expected 43 separate IDs')

texts = {p: p.read_text(encoding='utf-8') for p in ROOT.rglob('*.md') if '.git' not in p.parts}


def anchors(text):
    found = re.findall(r'<a\s+(?:name|id)="([^"]+)"', text)
    counts = Counter()
    for line in text.splitlines():
        if not re.match(r'^#{1,6} ', line):
            continue
        heading = re.sub(r'^#+\s+', '', line).strip().lower()
        heading = re.sub(r'<[^>]+>', '', heading)
        heading = re.sub(r'\[([^]]+)\]\([^)]+\)', r'\1', heading)
        slug = ''.join(c for c in heading if c in '-_ ' or unicodedata.category(c)[0] in 'LNM')
        slug = slug.replace(' ', '-')
        count = counts[slug]
        counts[slug] += 1
        found.append(slug + (f'-{count}' if count else ''))
    return found


anchor_sets = {p: set(anchors(t)) for p, t in texts.items()}
primary_counts = Counter()
for path, text in texts.items():
    if 'archive' in path.parts or 'maintenance' in path.parts:
        continue
    primary_counts.update(re.findall(r'<a name="(ri-s\d{2})"></a>', text))
check(primary_counts == Counter({f'ri-{sid.lower()}': 1 for sid in scenario_ids}),
      'Primary scenario anchors are missing, repeated, or unexpected')
for row in mapping['scenarios']:
    file, anchor = row['owner'].split('#')
    path = (P / file).resolve()
    check(path.exists() and anchor in anchor_sets.get(path, set()), f'Invalid owner: {row["id"]}')
    source = next(x for x in source_scenarios if x['id'] == row['id'])
    check(source['name'] == row['name'], f'Changed identity: {row["id"]}')
    check(set(source['source_ids']) <= source_ids, f'Unknown source IDs: {row["id"]}')

cases = texts[P / 'retail-investors-cases.md']
labels = ['Пользователь', 'Повод', 'Задача и результат', 'Действия', 'Входные данные',
          'Инструменты', 'Предполагаемая ручная работа',
          'Существующие способы по исходному исследованию', 'Предложение для проверки',
          'Степень делегирования', 'Статус основания', 'Неизвестное', 'Проверка',
          'Мера результата', 'Основания']
for row in mapping['scenarios']:
    if row['decision'] != 'Добавлен':
        continue
    block = cases.split(f'<a name="ri-{row["id"].lower()}"></a>', 1)[1].split('<a name=', 1)[0]
    for label in labels:
        check(f'| {label} |' in block, f'Missing field {label}: {row["id"]}')
    source = next(x for x in source_scenarios if x['id'] == row['id'])
    for sid in source['source_ids']:
        check(f'#ri-{sid.lower()}' in block, f'Missing scenario evidence {sid}: {row["id"]}')

registry = texts[P / 'retail-investors-sources.md']
registry_ids = re.findall(r'<a name="ri-([mbcr]\d{2})"></a>', registry)
check(Counter(registry_ids) == Counter(x.lower() for x in source_ids), 'Duplicate or missing registry records')
for source in parser.sources:
    check(source['url'] in registry, f'Missing original source URL: {source["id"]}')
report_html = re.search(r'<section[^>]*id="report"[^>]*>(.*?)</section>', source_html, re.S).group(1)
report_urls = {unescape(u) for u in re.findall(r'href="([^"]+)"', report_html)}
report_ids = {s['id'] for s in parser.sources if s['url'] in report_urls}
active = '\n'.join(texts[P/name] for name in [
    'retail-investors-summary.md','retail-investors-analysis.md','retail-investors-cjm.md',
    'product-formats.md','retail-investors-sources.md'])
for sid in report_ids:
    # Registry headings alone do not count as a citation in the transferred report.
    check(f'](retail-investors-sources.md#ri-{sid.lower()})' in active,
          f'Missing transferred report citation: {sid}')

base = mapping['base_commit']
changed = set(git('diff', '--name-only', base).splitlines())
changed.update(git('ls-files', '--others', '--exclude-standard').splitlines())
checked_links = 0
for rel in sorted(changed):
    path = (ROOT / rel).resolve()
    if path.suffix != '.md' or 'archive' in path.parts or not path.exists():
        continue
    text = texts[path]
    for match in re.finditer(r'\[[^\]\n]*\]\(([^\s)]+)\)', text):
        target = unescape(match.group(1)).strip('<>')
        u = urlsplit(target)
        if u.scheme or u.netloc:
            continue
        dest = (path.parent / unquote(u.path)).resolve() if u.path else path
        checked_links += 1
        check(dest.exists(), f'Broken local path {rel}: {target}')
        if u.fragment and dest.suffix == '.md' and dest.exists():
            check(unquote(u.fragment) in anchor_sets.get(dest, set()), f'Broken anchor {rel}: {target}')
    # Previous explicit anchors are stable public interfaces.
    try:
        old = git('show', base + ':' + rel)
    except subprocess.CalledProcessError:
        old = ''
    check(set(re.findall(r'<a name="([^"]+)"', old)) <= anchor_sets[path],
          f'Removed baseline anchor in {rel}')

ctx = json.loads((ROOT / '.agents/context.json').read_text(encoding='utf-8'))
entry = ctx['research_results']['retail_investors_cjm']
check(entry['source_scenario_count'] == 50 and entry['source_count'] == 51, 'Context counts mismatch')
check(entry['status'] == 'published' and entry['merged_pr'] == 61, 'CJM publication pointer mismatch')
for key in ['overview','mapping','archive','publication_package']:
    check((ROOT / entry[key]).is_file(), f'Missing context pointer: {key}')
for pointer in entry['details']:
    check((ROOT/pointer).is_file(), f'Missing detail pointer: {pointer}')
check(not (P/'candidates.md').exists(), 'Withdrawn shortlist is still present')
for name in ['retail-investors-summary.md','retail-investors-cjm.md','retail-investors-analysis.md','retail-investors-cases.md','retail-investors-sources.md']:
    check('—' not in texts[P/name], f'Long dash in active document: {name}')

result = {'source_scenarios':50, 'merged':7, 'new':43, 'source_records':51,
          'report_sources':len(report_ids), 'reused_source_urls':sum(bool(s['existing_locations']) for s in mapping['sources']),
          'primary_scenario_anchors':sum(primary_counts.values()), 'local_links_checked':checked_links,
          'changed_markdown_files':sum(p.endswith('.md') for p in changed), 'errors':errors}
print(json.dumps(result, ensure_ascii=False, indent=2))
raise SystemExit(bool(errors))
