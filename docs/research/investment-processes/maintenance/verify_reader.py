from pathlib import Path
import re, json, hashlib
P=Path(__file__).resolve().parents[1]
A=P/'archive/reader-revision-2026-11-15'
manifest=json.loads((A/'manifest.json').read_text(encoding='utf-8'))
for r in manifest:
    assert hashlib.sha256((A/r['archived_path']).read_bytes()).hexdigest()==r['sha256']
urls=lambda t:set(re.findall(r'https?://[^\s)<>]+',t))
active=set().union(*(urls(f.read_text(encoding='utf-8')) for f in P.glob('*.md')))
old_sources=urls((A/'retail-investors-sources.md').read_text(encoding='utf-8'))
assert not old_sources-active, old_sources-active
catalog=(P/'retail-investors-cases.md').read_text(encoding='utf-8')
assert len(re.findall(r'^### ',catalog,re.M))==55
for n in range(1,56): assert catalog.count(f'<a name="ri-s{n:02}"></a>')==1
mapping=json.loads((A/'scenario-mapping.json').read_text(encoding='utf-8'))
assert len(mapping['new_scenarios'])==50 and len(mapping['old_client_scenarios'])==11
result=json.loads((P/'maintenance/reader-validation.json').read_text(encoding='utf-8'))
result.update(research_external_urls_preserved=len(old_sources),research_urls_missing_active=[],archive_hashes_valid=True)
(P/'maintenance/reader-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
