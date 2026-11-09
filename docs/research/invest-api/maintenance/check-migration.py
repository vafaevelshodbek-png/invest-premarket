"""Verify content preservation for the issue 30 migration. Standard library only."""

import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[4]
TOPIC = ROOT / 'docs/research/invest-api'
BASE = '468659dfbf25b7572d4ba33c2f8f8de66e9b863d'


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def anchors(text):
    ids = set(re.findall(r'<a\s+(?:name|id)="([^"]+)"', text))
    for title in re.findall(r'^#{1,6}\s+(.+)$', text, re.M):
        ids.add(re.sub(r'[^\w\s-]', '', title.lower()).replace(' ', '-'))
    return ids


def main():
    errors = []
    original = (TOPIC / 'maintenance/archive/issue-30-2026-11-09.md').read_text(encoding='utf8')
    reference = (TOPIC / 'reference.md').read_text(encoding='utf8')
    overview = (TOPIC / 'README.md').read_text(encoding='utf8')
    sources = dict(re.findall(r'^\[(S\d+)\]: (.+)$', original, re.M))
    labels = {url: label for label, url in re.findall(r'^- \[([^]]+)\]\(([^)]+)\)', reference, re.M)}

    def convert(text):
        for key, url in sources.items():
            if url not in labels:
                errors.append('Source absent from reference: ' + key)
                continue
            text = text.replace('[' + key + ']', '[' + labels[url] + '](' + url + ')')
        text = text.replace('. Д для', '. По документации для').replace(', Н для', ', не проверено для')
        text = re.sub(r'\. Д$', '. По документации', text)
        text = re.sub(r'\. Н$', '. Не проверено', text)
        return text

    matrix = original.split('### 2. Матрица возможностей\n')[1].split('### 3. Подключение')[0]
    rows = [line.split('|')[1:-1] for line in matrix.splitlines() if line.startswith('| ')][1:]
    cards = re.findall(r'<a name="([^"]+)"></a>\s*<details>\s*<summary>(.*?)</summary>(.*?)</details>', reference, re.S)
    report_rows = []
    for i, row in enumerate(rows):
        expected = [convert(cell.strip()) for cell in row]
        preserved = len(cards) > i and all(text in cards[i][2] for text in expected)
        if not preserved:
            errors.append('Original matrix row lost or changed without mapping: ' + str(i + 1))
        report_rows.append({'source_row': i + 1, 'methods': row[0].strip(),
                            'anchor': cards[i][0] if len(cards) > i else None,
                            'all_five_fields_preserved': preserved})
    if len(rows) != 18 or len(cards) != 19:
        errors.append('Expected 18 original directions and one archive addition')
    source_status = [{'source': key, 'url': url, 'retained': url in reference}
                     for key, url in sources.items()]
    if len(sources) != 32 or not all(row['retained'] for row in source_status):
        errors.append('Original source inventory incomplete')
    if re.search(r'\[S\d+\]', reference + overview):
        errors.append('Internal source codes visible in reader pages')

    checks_section = original.split('### 8. Непроверенные условия и передача в #19')[1].split('### Источники')[0]
    checks = [line for line in checks_section.splitlines() if line.startswith('| ')][1:]
    if len(checks) != 6 or not all(convert(line) in reference for line in checks):
        errors.append('Original six future checks not retained')
    candle_table = reference.split('| Интервал | Максимальный период запроса | Максимальное число свечей |')[1].split('\n\n')[0]
    candle_rows = [line for line in candle_table.splitlines() if line.startswith('| ') ]
    if len(candle_rows) != 16:
        errors.append('Expected all 16 candle intervals')
    for line in ['| 1 минута | 1 день | 2400 |', '| 5 минут | 1 неделя | 2400 |',
                 '| 1 час | 3 месяца | 2400 |', '| 1 день | 6 лет | 2400 |']:
        if line not in reference:
            errors.append('Original candle limit absent: ' + line)
    for value in ['600', '200', '15', '300', '100 мс', '0,05%', '1.51', '1000', 'units', 'nano', 'tools/list']:
        if value not in reference:
            errors.append('Original technical detail absent: ' + value)
    for url in ['https://invest-public-api.tbank.ru/rest/', 'https://sandbox-invest-public-api.tbank.ru/rest/',
                'https://invest-public-api.tbank.ru/mcp', 'https://sandbox-invest-public-api.tbank.ru/mcp']:
        if url not in reference:
            errors.append('Original endpoint absent: ' + url)

    checked_links = 0
    for path in [TOPIC / 'README.md', TOPIC / 'reference.md', TOPIC / 'maintenance/audit.md',
                 TOPIC / 'maintenance/audit-plan.md', ROOT / 'docs/research/README.md']:
        text = path.read_text(encoding='utf8')
        if re.search(r'\?{3,}', text):
            errors.append('Corrupted text: ' + str(path))
        for target in re.findall(r'\]\(([^)\s]+)\)', text):
            if re.match(r'[a-z]+:', target):
                continue
            name, _, fragment = unquote(target).partition('#')
            resolved = (path.parent / name).resolve() if name else path
            if not resolved.is_file():
                errors.append('Missing file: ' + target)
            elif fragment and resolved.suffix == '.md' and fragment not in anchors(resolved.read_text(encoding='utf8')):
                errors.append('Missing anchor: ' + target)
            checked_links += 1
        if path.name in ['README.md', 'reference.md'] and any(c in text for c in ['—', '→', '←', '·']):
            errors.append('Decorative separator in reader page: ' + str(path))

    changed = git('diff', '--name-only', BASE).decode().splitlines()
    for path in changed:
        if path not in ['.agents/context.json', 'docs/research/README.md'] and not path.startswith('docs/research/invest-api/'):
            errors.append('Change outside migration scope: ' + path)
    data = json.loads((ROOT / '.agents/context.json').read_text(encoding='utf8'))
    previous = json.loads(git('show', BASE + ':.agents/context.json').decode())
    for key in previous:
        if key != 'research_results' and previous[key] != data[key]:
            errors.append('Unrelated machine context changed: ' + key)
    for key in previous['research_results']:
        if key != 'api_mcp' and previous['research_results'][key] != data['research_results'][key]:
            errors.append('Another research pointer changed: ' + key)

    report = {'baseline_commit': BASE, 'source_issue': 30,
              'original_sha256': hashlib.sha256(original.encode()).hexdigest(),
              'matrix': report_rows, 'original_sources': source_status,
              'original_pending_checks_retained': len(checks), 'candle_intervals': len(candle_rows),
              'local_links_checked': checked_links, 'errors': errors,
              'limitations': ['Preservation and links do not establish source accuracy or account access.',
                              'External source verification methods and gaps are documented in audit.md.']}
    if len(sys.argv) == 2:
        destination = Path(sys.argv[1])
        if not destination.is_absolute(): destination = ROOT / destination
        destination.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    print(json.dumps({'errors': errors, 'matrix_rows_preserved': sum(row['all_five_fields_preserved'] for row in report_rows),
                      'source_links_retained': len(source_status), 'candle_intervals': len(candle_rows),
                      'local_links_checked': checked_links}, ensure_ascii=False))
    return int(bool(errors))


if __name__ == '__main__':
    sys.exit(main())
