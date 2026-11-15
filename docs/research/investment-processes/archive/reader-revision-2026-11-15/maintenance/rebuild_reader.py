from pathlib import Path
import re, json, shutil, hashlib

BASE = Path(__file__).resolve().parents[1]
ARCH = BASE / 'archive/reader-revision-2026-11-15'
ARCH.mkdir(parents=True, exist_ok=True)
manifest = []
for src in ([] if (ARCH/'manifest.json').exists() else list(BASE.glob('*.md')) + list((BASE/'maintenance').glob('*')) + list((BASE/'assets').rglob('*'))):
    if not src.is_file() or src.name == 'rebuild_reader.py':
        continue
    dst = ARCH / ('README.original.md' if src.relative_to(BASE).as_posix()=='README.md' else src.relative_to(BASE))
    dst.parent.mkdir(parents=True, exist_ok=True)
    if not dst.exists():
        shutil.copyfile(src, dst)
    manifest.append({'path': str(src.relative_to(BASE)).replace('\\','/'), 'archived_path':dst.relative_to(ARCH).as_posix(), 'sha256': hashlib.sha256(dst.read_bytes()).hexdigest()})
if (ARCH/'manifest.json').exists():
    manifest=json.loads((ARCH/'manifest.json').read_text(encoding='utf-8'))
else:
    (ARCH/'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
def original(name): return (ARCH/name).read_text(encoding='utf-8')
def write(name, text): (BASE/name).write_text(text.rstrip()+'\n', encoding='utf-8')
html = (BASE/'archive/retail-investors-2026-11-15/Russia_Retail_Investors_CJM.html').read_text(encoding='utf-8')
scenarios = json.loads(re.search(r'<script type="application/json" id="scenario-data">(.*?)</script>', html, re.S)[1])
assert len(scenarios) == 50
old = original('participant-cases.md')
old_sections = {}
for m in re.finditer(r'<a name="([^"]+)"></a>\s*\n#{2,3} (\d+)\. ([^\n]+)\n(.*?)(?=<a name=|\Z)', old, re.S):
    old_sections[int(m[2])] = {'anchor':m[1], 'title':m[3], 'body':m[4].strip()}
assert set(range(17,27)) <= old_sections.keys()
source_text = original('retail-investors-sources.md')
source_titles = {m[1].lower():m[2] for m in re.finditer(r'^### ([MBCR]\d+)\. (.+)$',source_text,re.M)}
old_sources = original('current-methods-sources.md')
legacy_titles = {m[1].lower():m[2] for m in re.finditer(r'\*\*(S\d+)\. \[([^\]]+)\]', old_sources)}
legacy_titles.update(s28='Composer: создание и выполнение стратегии',s29='TradingView: стратегии и модель исполнения')
def clean(text):
    text = re.sub(r'\[([MBCR]\d+)\]\(retail-investors-sources.md#ri-([mbcr]\d+)\)', lambda m:'['+source_titles[m[2]]+'](retail-investors-sources.md#ri-'+m[2]+')',text)
    text = re.sub(r'\[(S\d+)\]\(current-methods-sources.md#(s\d+)\)', lambda m:'['+legacy_titles[m[2]]+'](current-methods-sources.md#'+m[2]+')',text)
    return text.replace(' · ','; ').replace(' — ',' – ')
def rows(body):
    return [(m[1].strip(),m[2].strip()) for m in re.finditer(r'^\| ([^|]+) \| (.*?) \|$',body,re.M) if m[1].strip()!='Поле']
def keep_old(n):
    allowed={'Область','Роль','Ситуация','Задача','Вход','Результат','Получатель','Область и роль','Результат и получатель','Предполагаемая цена ошибки','Основание и проверка','Основание и статус','Дополнительная проверка','Полномочия и системы'}
    return [(k,v) for k,v in rows(old_sections[n]['body']) if k in allowed]
# A scenario has one primary home. Related lifecycle steps remain links, never copies.
merges={1:18,18:29,19:41,21:23,22:24,26:36}
extras={20:51,17:52,23:53,24:54,25:55}
mapping=[]
for n,target in {**merges,**extras}.items():
    mapping.append({'legacy_case':n,'legacy_anchor':old_sections[n]['anchor'],'canonical_scenario':target,'disposition':'merged' if n in merges else 'distinct task retained'})
extra_titles={51:'Разобраться в денежных потоках и условиях одной облигации',52:'Объяснить изменение стоимости собственного портфеля',53:'Отрепетировать сделку на учебном счёте',54:'Проверить формализованную торговую стратегию на данных',55:'Запустить выбранную стратегию с бюджетом и ограничениями'}
for n,i in extras.items(): scenarios.append({'id':f'S{i:02}','name':extra_titles[i],'legacy':n})
groups=[
('Цель и доступные деньги',[1,2,3]),
('Посредник, счёт и доступ',[4,5,6,7,8]),
('Пополнение и размещение свободных денег',[9,10,11]),
('Поиск идеи и проверка инструмента',[12,13,14,15,16,17,51,18,19,20,54]),
('Выбор способа входа',[21,22]),
('Подготовка действия',[53,23,24,55]),
('Исполнение и контроль открытых обязательств',[25,26,27,28]),
('Удержание, события и права',[29,30,31,32,33]),
('Пересмотр позиции и стратегии',[34,35,36]),
('Проверка результата и учёт',[52,37,38]),
('Налоги',[39,40]),
('Получение денег и перевод активов',[41,42,43]),
('Пауза и возвращение',[45,46]),
('Сквозная помощь и собственные инструменты',[44,47]),
('Особые условия владения',[48,49,50])]
owners={i:title for title,ids in groups for i in ids}
assert len(owners)==55 and set(owners)==set(range(1,56))
lookup={int(s['id'][1:]):s for s in scenarios}
def anchor(i): return f'ri-s{i:02}'
def link(i): return f'[{lookup[i]["name"]}](retail-investors-cases.md#{anchor(i)})'
index=['# Путь частного инвестора','', '[Обзор](README.md); [сегменты и поведение](retail-investors-analysis.md); [основания и ограничения](retail-investors-sources.md).','',
'Путь начинается с финансовой задачи и продолжается после покупки: выплаты, контроль результата, налоги, получение денег, пауза и возвращение. На каждом этапе возможны ожидание, отказ и сохранение прежнего решения. Это аналитическая карта, а не измеренный маршрут среднего инвестора.','',
'Каталог объединяет 50 сценариев карты пути и пять самостоятельных задач из прежних клиентских материалов. У каждой задачи одно основное место по её результату. Поддержка и собственные инструменты проходят через разные этапы; наследование и особенности инфраструктуры меняют условия пути. Эти ветви вынесены отдельно от последовательности.','']
catalog=['# Сценарии частного инвестора','', '[Карта пути и навигация](retail-investors-cjm.md); [сегменты и поведение](retail-investors-analysis.md); [метод и источники](retail-investors-sources.md).','',
'Здесь собраны 55 разных задач клиента. Основание отдельной операции не доказывает частоту всей истории, трудозатраты, спрос или готовность делегировать действие. Сценарии являются моделями для исследования; документированная операция помечена отдельно.','',
'Поля «ручная работа» и «цена ошибки» обозначают гипотезы. Описанные функции сервисов взяты из прежнего исследования и не означают проверку на клиентском счёте. Решения о запуске стратегии, заявке, отмене и закрытии позиции имеют разные результаты.','']
for title,ids in groups:
    index+=['## '+title,'']+[f'- {link(i)}' for i in ids]+['']
    catalog+=['## '+title,'']
    for i in ids:
        s=lookup[i]
        aliases=[m['legacy_anchor'] for m in mapping if m['canonical_scenario']==i]
        catalog += [f'<a name="{a}"></a>' for a in [anchor(i)]+aliases]
        catalog+=['','### '+s['name'],'','| Поле | Содержание |','|---|---|']
        if i<=50:
            fields=[('Пользователь',s['segment']),('Повод',s['trigger']),('Задача и результат',s['goal']),('Действия','; '.join(s['actions'])),('Входные данные','; '.join(s['data'])),('Инструменты','; '.join(s['tools'])),('Предполагаемая ручная работа',s['manual_work']),('Существующие способы',s['existing_automation']),('Статус основания',s['evidence_status']),('Неизвестное',s['unknowns']),('Проверка',s['validation']),('Мера результата',s['success_metric']),('Основания',', '.join('['+source_titles[k.lower()]+'](retail-investors-sources.md#ri-'+k.lower()+')' for k in s['source_ids']))]
        else: fields=keep_old(s['legacy'])
        if i<=50:
            previous=re.search(r'<a name="'+anchor(i)+r'"></a>(.*?)(?=<a name=|\Z)',original('retail-investors-cases.md'),re.S)
            if previous:
                fields=[(k.replace('Существующие способы по исходному исследованию','Существующие способы'),v) for k,v in rows(previous[1]) if k not in {'Предложение для проверки','Степень делегирования'}]
        catalog += ['| '+k+' | '+clean(v).replace('|',' / ')+' |' for k,v in fields]+['']
        if i in {18,20,23,24,29,41,42}:
            previous=re.search(r'<a name="'+anchor(i)+r'"></a>(.*?)(?=<a name=|\Z)',old,re.S)
            if previous:
                content=previous[1].strip().split('Основание ветки:')[0].strip()
                catalog+=[clean(content),'']
        for n,target in merges.items():
            if target==i:
                catalog+=['**Уточнение задачи из прежнего клиентского разбора.**','']+['- **'+k+'.** '+clean(v) for k,v in keep_old(n)]+['']
        if i==41:
            catalog+=['Плановый вывод связан с заранее известной датой расхода. При внезапной потребности меняются срок и допустимые альтернативы: '+link(42)+'.','']
        if i==54: catalog+=['Результат здесь – проверяемая версия правила и отчёт испытания. Ручной план сессии рассматривается отдельно: '+link(20)+'. Решение о запуске также отдельно: '+link(55)+'.','']
        # Preserve the factual current-methods paragraphs, but archive early product proposals.
        for n,target in {**merges,**extras}.items():
            if target!=i: continue
            methods=original('current-methods.md')
            am=re.search(r'<a name="'+re.escape(old_sections[n]['anchor'])+r'"></a>(.*?)(?=<a name=|\Z)',methods,re.S)
            if am:
                paras=re.findall(r'\*\*(?:Как решают сейчас|Что уже есть|Затруднение или гипотеза|Гипотеза затруднения)\.\*\*.*?(?=\n\n|\Z)',am[1],re.S)
                if paras: catalog+=['**Текущая практика и ограничения.**','']+[clean(p)+'\n' for p in paras]
write('retail-investors-cjm.md','\n'.join(index))
write('retail-investors-cases.md','\n'.join(catalog))
# Detailed source records survive with descriptive labels and stable invisible aliases.
source_text=re.sub(r'^### [MBCR]\d+\. ', '### ',source_text,flags=re.M)
source_text=re.sub(r'В реестре 51 материал,.*?\n\n','В реестре 51 материал. Повторные публикации одного исследования не являются независимыми наблюдениями. Ссылки ведут к описаниям публикаций с датами, методом, ограничениями и статусом чтения.\n\n',source_text,flags=re.S)
source_text=source_text.replace('В исходнике 50 сценариев:', 'В исходной карте 50 сценариев:')
source_text=source_text.replace('Новые интервью, наблюдения, финансовые расчёты и вызовы брокерского API не выполнялись.', 'Новые интервью, наблюдения, финансовые расчёты и вызовы брокерского API не выполнялись. Пять самостоятельных задач прежнего клиентского разбора добавлены к карте отдельно; их основания перечислены в карточках и в реестре клиентских инструментов.')
source_text='\n\n'.join(p for p in source_text.split('\n\n') if not p.startswith(('Исходник:', 'Исследование включало подготовку', 'Реестр хранит даты')))
source_text=source_text.replace('## Происхождение и сила оснований','## Метод и сила оснований')
source_text=source_text.replace('В исходной карте 50 сценариев:', 'Срез публикаций относится к 14 ноября 2026 года. Новые интервью и проверки функций на клиентском счёте не выполнялись. В исходной карте 50 сценариев:')
write('retail-investors-sources.md',clean(source_text))
client_ids=['s01','s24','s25','s26','s27','s28','s29','s30']
registry=['# Источники о клиентских инструментах','', '[Каталог сценариев](retail-investors-cjm.md); [исследования и метод](retail-investors-sources.md).','', 'Публичные описания подтверждают функции, заявленные поставщиками. Они не подтверждают удобство, экономию времени или спрос. Даты и ограничения относятся к ранее выполненному исследованию.','']
for key in client_ids:
    m=re.search(r'<a name="'+key+r'"></a>(.*?)(?=<a name=|\Z)',old_sources,re.S)
    if not m: continue
    body=m[1].split('\n## ')[0].strip()
    body=re.sub(r'\*\*S\d+\. ', '**',body)
    body=re.sub(r'Ситуаци[яи] [\d, и–-]+\.', '',body)
    registry+=[f'<a name="{key}"></a>','',clean(body),'']
write('current-methods-sources.md','\n'.join(registry))
# All retired entrypoints remain linkable without duplicating their old full text.
retired=['details.md','participants.md','participants-summary.md','participant-cases.md','current-methods.md','current-methods-summary.md','product-formats.md','product-formats-summary.md','product-formats-sources.md']
for name in retired:
    orig=original(name)
    title='Клиентские сценарии' if name.startswith('participant') else ('Прежние предложения автоматизации' if name.startswith('product-format') else 'Материалы прежней карты')
    lines=['# '+title,'','[Актуальная карта клиентского пути](retail-investors-cjm.md); [каталог задач клиента](retail-investors-cases.md).','','Прежняя редакция сохранена в [архиве исследования](archive/reader-revision-2026-11-15/README.md). Операционные задачи сотрудников и ранние предложения автоматизации доступны отдельно от действующего каталога.','']
    route_links=[]
    for a in re.findall(r'<a name="([^"]+)"></a>',orig):
        target=None
        if a.startswith('ri-s'):
            mt=re.match(r'ri-s(\d+)',a)
            if mt and int(mt[1])<=50: target=int(mt[1])
        for m in mapping:
            if a==m['legacy_anchor']: target=m['canonical_scenario']
        lines += [f'<a name="{a}"></a>']
        if target and link(target) not in route_links: route_links.append(link(target))
    lines+=['']+['- '+x for x in route_links]+['',f'[Полный прежний материал](archive/reader-revision-2026-11-15/{name})']
    write(name,'\n'.join(lines))
analysis=clean(original('retail-investors-analysis.md'))
write('retail-investors-analysis.md',analysis)
market=original('markets.md')
table=re.search(r'(\| Область \| Инструменты.*?)(?=\n\s*\n)',market,re.S)[1]
table=table.replace('биржевых паевой инвестиционный фонд','биржевых фондов').replace('производные финансовые инструменты','производные инструменты').replace('Наличие центральный контрагент','Наличие центрального контрагента')
table=table.replace('продажа с обязательством обратного выкупа','репо').replace('клиринговый сертификат участия','клиринговые сертификаты участия').replace('В репо','В сделке репо').replace('валютный своп','Валютный своп')
write('markets.md','# Рынки и инструменты\n\n[Карта клиентского пути](retail-investors-cjm.md).\n\nКласс инструмента, срок владения и способ исполнения описывают разные стороны одного решения. Пай фонда облигаций остаётся паем; владение фьючерсом на актив отличается от владения самим активом. Доступность конкретной операции определяется условиями счёта и посредника.\n\n'+clean(table)+'\n\nВклад и погашение личного долга рассматриваются в клиентском пути как альтернативы размещению свободных денег. Результат сравнения может состоять в отказе от инвестиций.\n')
write('README.md','''# Клиентский путь частного инвестора

Как человек определяет цель, выбирает способ вложения, проверяет инструмент, совершает действие и получает результат. Каталог охватывает самостоятельного инвестора и частного трейдера, включая обслуживание, выплаты, налоги, выход и возвращение.

| Материал | Что в нём |
|---|---|
| [Карта пути](retail-investors-cjm.md) | Последовательность этапов и ссылки на 55 задач клиента |
| [Каталог сценариев](retail-investors-cases.md) | Повод, действия, входные данные, результат, текущие способы и основания каждой задачи |
| [Сегменты и поведение](retail-investors-analysis.md) | Различия инвесторов, способы принятия решений и ограничения статистики |
| [Рынки и инструменты](markets.md) | Предмет вложения и особенности финансового контекста |
| [Исследования и источники](retail-investors-sources.md) | Метод, сила свидетельств, даты, ссылки и ограничения |
| [Клиентские инструменты](current-methods-sources.md) | Документация сервисов, использованная в прежних клиентских разборах |

Первые 50 задач получены из карты полного пути. Ещё пять сохраняют самостоятельные результаты прежнего клиентского исследования: понимание условий одной облигации, объяснение изменения портфеля, учебная сделка, проверка формализованной стратегии и её запуск. Остальные прежние клиентские задачи объединены с соответствующими карточками. У каждой задачи одно основное место, сквозная помощь и особые условия владения выделены отдельно.

Материал основан на публикациях, документации и аналитической декомпозиции. Он не измеряет частоту задач, затраты времени, спрос или готовность делегировать операции. Срез источников относится к 14 ноября 2026 года; функции сервисов не проверялись на клиентском счёте.

[Исследование существующих инвестиционных продуктов](../ai-investment-products/README.md) помогает сопоставлять задачи с доступными способами работы.

[Архив прежних результатов](archive/reader-revision-2026-11-15/README.md) сохраняет широкую карту деятельности, задачи сотрудников и предложения автоматизации.
''')
write('retail-investors-summary.md','''# Частный инвестор: путь и задачи

Инвестиционная работа продолжается после сделки: человек проверяет выплаты, объясняет результат, готовит налоги, получает деньги к личной дате и решает, продолжать ли отношения с посредником.

[Карта пути](retail-investors-cjm.md) объединяет 55 задач. [Подробные карточки](retail-investors-cases.md) показывают повод, действия, данные, результат и неизвестное. [Анализ поведения](retail-investors-analysis.md) объясняет различия сегментов и ограниченность общерыночных выводов.

В самостоятельной работе инвестора нужно различать понимание инструмента, сравнение альтернатив, проверку параметров и фактическое исполнение. Для стратегий также различаются выбор, проверка правил, запуск и остановка. Пауза новых сигналов сама по себе не отменяет заявки и не закрывает позиции.

Частота, трудозатраты и спрос в этих сценариях не измерены. Документация подтверждает отдельные операции, опрос описывает ответы своей выборки, а аналитическая карточка задаёт предмет будущего наблюдения. [Метод, источники и ограничения](retail-investors-sources.md).
''')
(ARCH/'scenario-mapping.json').write_text(json.dumps({'new_scenarios':[{'original_id':s['id'],'canonical_anchor':anchor(int(s['id'][1:])),'primary_home':owners[int(s['id'][1:])]} for s in scenarios[:50]],'old_client_scenarios':mapping,'staff_archived':list(range(2,17)),'total_canonical':55}, ensure_ascii=False, indent=2)+'\n',encoding='utf-8')
(ARCH/'README.md').write_text('''# Архив прежних результатов

Редакция до объединения клиентского каталога от 15 ноября 2026 года сохранена без изменения байтов. Реестр контрольных сумм: [manifest.json](manifest.json). Соответствие каждой из 50 задач исходной карты и всех 11 прежних клиентских ситуаций: [scenario-mapping.json](scenario-mapping.json).

| Результат | Сохранённые материалы |
|---|---|
| Широкая карта рынка и процессов | [Обзор](README.original.md), [рынки](markets.md), [подробные процессы и источники](details.md) |
| Роли и задачи сотрудников | [Участники](participants.md), [обзор ролей](participants-summary.md), [рабочие ситуации](participant-cases.md) |
| Текущие способы и аналоги | [Сопоставление](current-methods.md), [обзор](current-methods-summary.md), [источники](current-methods-sources.md) |
| Ранние предложения автоматизации | [Карточки форматов](product-formats.md), [обзор](product-formats-summary.md), [основания](product-formats-sources.md) |
| Прежняя интеграция клиентского пути | [Обзор](retail-investors-summary.md), [карта](retail-investors-cjm.md), [сценарии](retail-investors-cases.md), [анализ](retail-investors-analysis.md), [источники](retail-investors-sources.md) |

Клиентские задачи объединены в [действующий каталог](../../retail-investors-cjm.md). Пятнадцать ситуаций сотрудников, широкие профессиональные процессы и ранние предложения не считаются текущим выбором продукта. Они сохранены как результаты прежнего исследования. Служебные проверки прежней редакции находятся в соседней папке maintenance.
''',encoding='utf-8')
print(json.dumps({'canonical_scenarios':55,'original_scenarios':50,'old_client_cases':len(mapping),'archived_files':len(manifest)},ensure_ascii=False))
