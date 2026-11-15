from pathlib import Path
import re, json, hashlib
P=Path(__file__).resolve().parents[1]
A=P/'archive/reader-revision-2026-11-15'
def edit(name,fn):
    f=P/name; f.write_text(fn(f.read_text(encoding='utf-8')).rstrip()+'\n',encoding='utf-8')
def toc(text,level):
    titles=re.findall(r'^'+('#'*level)+r' (.+)$',text,re.M)
    links=['- ['+s+'](#'+s.lower().replace(' ','-').replace(',','').replace(':','')+')' for s in titles]
    first=text.index('\n\n')
    return text[:first]+'\n\n'+ '\n'.join(links)+text[first:]
edit('retail-investors-cases.md',lambda t:toc(t,2))
def analysis(t):
    t=t.replace('Перенос из исследования, подготовленного 14–15 ноября. ','')
    t='\n\n'.join(p for p in t.split('\n\n') if not p.startswith('Подготовительная рамка сохранена'))
    start='Ниже предложены рабочие сегменты для анализа и рекрутинга.'
    i=t.index(start);j=t.index('\n\n| Рабочий сегмент',i)
    t=t[:i]+'''Для описания аудитории используются независимые признаки. Их значения относятся к конкретному моменту или решению; они не образуют складываемые доли населения.

| Измерение | Значения и граница |
|---|---|
| Состояние отношений | До открытия счёта; доступ без пополнения; работающий счёт; пауза; завершение отношений; возвращение |
| Финансовая задача | Резерв к ближайшей дате; накопление к будущей цели; текущий денежный доход; иной результат, который ещё требуется уточнить |
| Кто определяет действие | Собственное решение; заранее заданное личное правило; решение выбранного управляющего или автора стратегии |
| Частота операций | Отсутствие новых сделок; редкие сделки; регулярные покупки; частая торговля. Границы частоты следует задать для конкретного исследования |
| Контур данных | Один счёт; несколько счетов у одного посредника; несколько посредников. Зарубежная инфраструктура отмечается отдельным признаком |
| Опыт и ресурсы | Опыт, капитал, доступное время и знания фиксируются отдельно от способа принятия решения |

Следующая таблица показывает сочетания этих признаков и возникающие задачи. Строки не являются взаимоисключающими сегментами; задача может меняться у одного человека без смены его опыта или капитала.'''+t[j:]
    t=t.replace('| Рабочий сегмент |','| Ситуация клиента |')
    return toc(t,2)
edit('retail-investors-analysis.md',analysis)
def sources(t):
    nav='[Метод и сила оснований](#метод-и-сила-оснований); [пределы выводов](#противоречия-и-пределы-выводов); [проверки](#предложенные-проверки).\n\nРеестр: [рынок и клиентская статистика](#market-evidence); [поведение и опросы](#behavior-evidence); [интерфейсы и функции](#interface-evidence); [исследования и отдельные операции](#operation-evidence).'
    t=t.replace('<a name="method"></a>',nav+'\n\n<a name="method"></a>')
    for old,new in [('ri-m01','market-evidence'),('ri-b01','behavior-evidence'),('ri-c01','interface-evidence'),('ri-r01','operation-evidence')]:
        t=t.replace('<a name="'+old+'"></a>','<a name="'+new+'"></a>\n<a name="'+old+'"></a>')
    return t
edit('retail-investors-sources.md',sources)
edit('markets.md',lambda t:t.replace('с производные инструменты','с производными инструментами').replace('| производные инструменты |','| Производные инструменты |').replace('| репо с','| Репо с').replace('. клиринговые сертификаты участия','. Клиринговые сертификаты участия'))
for f in (P/'maintenance').glob('*.md'):
    f.write_text('# Прежняя служебная проверка\n\n[Сохранённая редакция](../archive/reader-revision-2026-11-15/maintenance/'+f.name+').\n\nТекущая проверка: [reader-validation.json](reader-validation.json).\n',encoding='utf-8')
# Operational diagrams are preserved in the byte-checked archive.
for name in ['market-routes.svg','processes.svg','support.svg','work.svg']:
    f=P/'assets'/name
    if f.exists():
        assert (A/'assets'/name).read_bytes()==f.read_bytes()
        f.unlink()
checks=[]
for row in json.loads((A/'manifest.json').read_text(encoding='utf-8')):
    assert hashlib.sha256((A/row['archived_path']).read_bytes()).hexdigest()==row['sha256'],row
    checks.append(row['path'])
catalog=(P/'retail-investors-cases.md').read_text(encoding='utf-8')
assert len(re.findall(r'^### ',catalog,re.M))==55
assert len(re.findall(r'<a name="ri-s\d+"',catalog))==55
visible_errors=[]
for f in P.glob('*.md'):
    t=f.read_text(encoding='utf-8')
    # Ignore URL/anchor payloads; only visible source codes are prohibited.
    t=re.sub(r'<[^>]+>|\]\([^)]*\)',']',t)
    if re.search(r'\b(?:RI-S\d+|[MBCRSF]\d{2})\b',t):visible_errors.append(f.name)
assert not visible_errors,visible_errors
result={'canonical_scenarios':55,'original_cjm_scenarios_preserved':50,'older_client_cases_mapped':11,'older_distinct_additions':5,'staff_scenarios_archived':15,'research_publications':51,'client_tool_source_records':8,'byte_preserved_files':len(checks),'visible_source_code_errors':visible_errors,'new_external_research_performed':False}
(P/'maintenance/reader-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
