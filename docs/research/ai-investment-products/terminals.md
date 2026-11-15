# ИИ в розничных и профессиональных терминалах

Срез на 15 ноября 2026 года.

[Обзор](README.md) | [Брокеры](brokers.md) | [Самостоятельные сервисы](research-services.md) | [Россия](russia.md) | [Терминалы](terminals.md) | [Фонды](funds.md) | [Источники](sources.md)

Здесь собраны восемь розничных платформ и шесть профессиональных систем. Разделение показывает аудиторию и рабочую среду. Брокерская принадлежность Questrade не создаёт вторую карточку в разделе брокеров, а российское происхождение Cbonds не создаёт вторую карточку в разделе России.

[Как читать термины](README.md#термины-простыми-словами). Страна в карточке описывает рынок и происхождение продукта, конкретный клиентский доступ указан отдельно.

## На этой странице

- [Розничные терминалы и платформы](#розничные-терминалы-и-платформы)
- [Профессиональные терминалы и исследовательские системы](#профессиональные-терминалы-и-исследовательские-системы)
- [Российские терминалы: что есть внутри, а что подключается снаружи](#российские-терминалы-что-есть-внутри-а-что-подключается-снаружи)

Таблицы продуктов в начале подразделов содержат прямые ссылки на все карточки.

## Розничные терминалы и платформы

Терминал здесь понимается как рабочее место анализа и торговли: график, данные, скринеры, стратегии и связь с брокером. TradingView, TrendSpider и MT5 имеют встроенные помощники, TradeStation в данном кейсе соединяется с внешним ИИ через MCP. Для Trade Ideas архитектура диалогового помощника не раскрыта.

| Продукт | Что делает | Текущий статус |
|---|---|---|
| [TradingView AI Copilot](#t01) | Анализ инструмента, настройка рабочего места, скрининг и разработка индикаторов/стратегий | Доступен как native add-on, прежнее расширение beta более не поддерживается активно |
| [TrendSpider Sidekick AI](#t02) | Связать анализ рынка с созданием сканера, индикатора, теста и алерта | Доступен |
| [MetaTrader 5 AI Assistant и MCP](#t03) | Анализ рынка и счёта, исследование стратегии, разработка MQL5 и операции через инструменты | Встроен в выпущенную desktop-платформу |
| [Koyfin Compare Matrix и AI Summary](#t04) | Сравнить содержание раскрытий компаний по конкурентам и кварталам, объяснить атрибуцию портфеля | Compare Matrix beta, AI Summary в attribution доступен Advisor Pro |
| [Trade Ideas AI Assistant, отдельно Holly AI Signals](#t05) | Создать рыночный сканер по описанию и объяснить открытый график | AI Assistant доступен, конкретная LLM не подтверждена |
| [TradeStation MCP](#t06) | Разбирать позиции и пользоваться функциями брокерской экосистемы из диалога | Выпущен для клиентов с условиями доступа |
| [QuantWheel QW Intelligence и MCP](#t07) | Поиск опционных возможностей, анализ позиций, рыночных потоков и торгового журнала | QW Intelligence и MCP описаны как доступные, часть автоматизации остаётся в планах, документы по исполнению расходятся |
| [Questrade Pro Intelligence и Questrade MCP](#rwb01) | Исследовать бумагу в терминале и подготовить действие из внешнего AI-клиента | Questrade Pro в открытой beta, Intelligence и MCP документированы как доступные |

<a name="t01"></a>

### TradingView AI Copilot

**Кому и зачем.** Международная платформа. Анализ инструмента, настройка рабочего места, скрининг и разработка индикаторов/стратегий.

**Что внедрено.**

- Учитывает открытый график и финансовые данные TradingView.
- Меняет индикаторы и разметку, создаёт уведомления и списки наблюдения.
- Генерирует Pine Script и объясняет результаты бэктеста.
- Подбирает инструменты по условиям, заданным обычным языком.

**Статус и доступ.** Доступен как native add-on, прежнее расширение beta более не поддерживается активно. Любой платный план Essential/Plus/Premium/Ultimate плюс отдельный ежемесячный add-on, web и desktop, mobile пока не поддерживается.

**Запуск и важные изменения.** 2026-04-02 public beta расширения, 2026-09-28 native.

**Технология и границы.** LLM/генеративный ИИ с инструментами платформы. Обновление 09.11.2026 называет DeepSeek V4.1 Flash, GPT-6 Luna, Claude Sonnet 5.5, модель выбирается для чата. Есть месячный лимит использования, поставщик предупреждает об ошибках. Исполнение брокерских заявок этой справкой не подтверждено. Доступность конкретного российского аккаунта не проверена.

<details>
<summary>Источники и подтверждения</summary>

- [Getting started with AI Copilot](https://www.tradingview.com/support/solutions/43000795131-getting-started-with-ai-copilot/)
- [AI Copilot comes to TradingView](https://www.tradingview.com/blog/en/ai-copilot-now-on-tradingview-61231/)
- [New in AI Copilot: use Claude, ChatGPT, or DeepSeek](https://www.tradingview.com/blog/en/ai-copilot-claude-chatgpt-deepseek-62292/)

</details>

<a name="t02"></a>

### TrendSpider Sidekick AI

**Кому и зачем.** США / международная платформа. Связать анализ рынка с созданием сканера, индикатора, теста и алерта.

**Что внедрено.**

- Исследует графики, финансовые показатели, отчётность и звонки по результатам.
- Создаёт и запускает сканеры и бэктесты, пишет индикаторы.
- Готовит уведомления и торговых роботов.
- Получает данные о позициях через поддерживаемое подключение брокера и SignalStack.

**Статус и доступ.** Доступен. 25 сообщений в месяц включены в каждую подписку TrendSpider, отдельные Sidekick пакеты Basic $49, Plus $129, Max $349 в месяц добавляют лимиты и модели.

**Запуск и важные изменения.** Точная первоначальная дата не установлена.

**Технология и границы.** Многомодельный LLM-агент с инструментами платформы. Поддерживаются модели Anthropic, OpenAI и Google, доступный набор обновляется и зависит от тарифа. Базовая подписка оплачивается отдельно от дополнительных пакетов Sidekick. Доступ к позициям требует поддерживаемого подключения. Бэктест не устанавливает будущую доходность.

<details>
<summary>Источники и подтверждения</summary>

- [Sidekick AI Trading Assistant](https://trendspider.com/product/sidekick-ai-trading-assistant)
- [TrendSpider Sidekick AI](https://trendspider.reamaze.com/kb/sidekick/trendspider-sidekick)

</details>

<a name="t03"></a>

### MetaTrader 5 AI Assistant и MCP

**Кому и зачем.** Международная платформа через брокеров. Анализ рынка и счёта, исследование стратегии, разработка MQL5 и операции через инструменты.

**Что внедрено.**

- Читает котировки, открытые позиции и торговую историю.
- Настраивает графики, тестирует и оптимизирует Expert Advisors.
- Генерирует/исправляет MQL5 код.
- Может выполнять поддерживаемые торговые операции при разрешении пользователя.

**Статус и доступ.** Встроен в выпущенную desktop-платформу. Обновлённая desktop-версия MT5 и вход в MQL5.community, MQL5 lite бесплатно, альтернативные провайдеры по своим ключам/условиям.

**Запуск и важные изменения.** 2026-07-24, build 6060, MetaEditor text/code assistant с 2023-06-14.

**Технология и границы.** LLM-агент с доступом к MCP инструментам терминала и MetaEditor. Бесплатная MQL5 lite по умолчанию, доступны собственные ключи моделей OpenAI, Anthropic, Google и других провайдеров. Торговлю, web и shell можно ограничить отдельно, поддерживаемые инструменты зависят от терминала и брокера. Факт native LLM в MT5 нельзя автоматически переносить на MT4, web/mobile и любого брокера.

<details>
<summary>Источники и подтверждения</summary>

- [MCP Servers and AI Assistant](https://www.metatrader5.com/en/terminal/help/mcp_and_ai)
- [The Evolution of MQL and MetaTrader](https://www.metatrader5.com/en/news/2453)
- [AI in MetaTrader 5: From Market Analysis to Trading Strategy Testing](https://www.metaquotes.com/en/company/news/5567)

</details>

<a name="t04"></a>

### Koyfin Compare Matrix и AI Summary

**Кому и зачем.** США / международный сервис. Сравнить содержание раскрытий компаний по конкурентам и кварталам, объяснить атрибуцию портфеля.

**Что внедрено.**

- Сравнивает одну компанию по кварталам или несколько компаний между собой.
- Отвечает по отчётности, звонкам, новостям и релизам.
- Показывает ссылки на источники в ячейках и экспортирует CSV.
- AI Summary объясняет причины отклонения результата модельного портфеля от бенчмарка на тарифе Advisor Pro.

**Статус и доступ.** Compare Matrix beta, AI Summary в attribution доступен Advisor Pro. Compare Matrix находится в Research Tools, beta с месячной token-квотой, конкретный тариф для beta не указан. AI Summary в attribution требует Advisor Pro.

**Запуск и важные изменения.** 2026-10-01 Compare Matrix, 2026-09-01 attribution AI Summary.

**Технология и границы.** LLM прямо подтверждена для Compare Matrix, генерация текста для AI Summary. Поставщик и версия LLM не раскрыты в рассмотренных инструкциях. Beta лимиты временные, обновление ответа расходует квоту. Нельзя объявлять весь Koyfin LLM-продуктом или автоматически относить advisor AI Summary к розничному тарифу.

<details>
<summary>Источники и подтверждения</summary>

- [Compare Matrix (Beta)](https://www.koyfin.com/help/release-notes/compare-matrix-beta/)
- [Attribution in Model Portfolios](https://www.koyfin.com/help/release-notes/attribution-in-model-portfolios/)

</details>

<a name="t05"></a>

### Trade Ideas AI Assistant, отдельно Holly AI Signals

**Кому и зачем.** США. Создать рыночный сканер по описанию и объяснить открытый график.

**Что внедрено.**

- Создаёт окно Alert или список Top List по текстовому запросу.
- Объясняет открытый график.
- Дополняется инструментом OddsMaker для проверки условий.

**Статус и доступ.** AI Assistant доступен, конкретная LLM не подтверждена. AI Assistant включён в TI Pro на всех планах Trade Ideas, Holly AI Signals и OddsMaker относятся к TI Premium.

**Запуск и важные изменения.** AI Assistant подтверждён текущей страницей, точная дата первичного запуска не установлена.

**Технология и границы.** Диалоговый AI Assistant, отдельно Holly Signals на алгоритмах и машинном обучении. LLM-архитектура и базовая модель помощника не раскрыты. AI Assistant и Holly Signals решают разные задачи. Данные и исполнение у брокера имеют собственные условия.

<details>
<summary>Источники и подтверждения</summary>

- [AI-powered Market Analyst & Trading Assistant](https://forums.trade-ideas.com/ai-assistant-for-trading/)
- [Aite Group: Trade Ideas Leveraging AI to Maximize the First Impression](https://www.trade-ideas.com/cms_static/PDF/Trade%20Ideas_Leveraging_AI_Maximize_First_Impression_Brief.pdf)

</details>

<a name="t06"></a>

### TradeStation MCP

**Кому и зачем.** США. Разбирать позиции и пользоваться функциями брокерской экосистемы из диалога.

**Что внедрено.**

- Подключает внешнего ИИ-ассистента к брокерскому счёту TradeStation.
- Поддерживает заявленные сценарии анализа позиций и торговой автоматизации.

**Статус и доступ.** Выпущен для клиентов с условиями доступа. Нужен брокерский счёт, соблюдение требований к нему и необходимых разрешений, на запуске требовалась подписка Claude Pro.

**Запуск и важные изменения.** 2026-01-13.

**Технология и границы.** Подключение брокерского аккаунта к внешней LLM через MCP. На запуске Claude от Anthropic, расширение списка AI-платформ анонсировано. Официальный MCP подключает внешний AI-клиент. Встроенный Self-Help отвечает о функциях платформы, его инвестиционные исследовательские возможности отдельно не установлены.

<details>
<summary>Источники и подтверждения</summary>

- [TradeStation Securities Releases MCP Connection](https://www.tradestation.com/press-and-news/tradestation-securities-releases-mcp-connection-allowing-users-to-connect-trading-accounts-with-third-party-ai-platforms/)
- [Monex Group announcement: TradeStation Securities Releases MCP Connection](https://www.monexgroup.jp/jp/news_release/irnews/auto_20260115534412/pdfFile.pdf)
- [TradeStation Desktop Release Notes](https://help.tradestation.com/10_00/eng/tradestationhelp/default/releasenotes_archives.htm)

</details>

<a name="t07"></a>

### QuantWheel QW Intelligence и MCP

**Кому и зачем.** Международный сервис с фокусом на опционы США. Поиск опционных возможностей, анализ позиций, рыночных потоков и торгового журнала.

**Что внедрено.**

- Переводит словесный запрос в скринер с заданными фильтрами.
- Учитывает рынок и собственные позиции на подходящем платном плане.
- Передаёт внешнему ассистенту данные экспозиции к гамме, потоков, портфеля и журнала через MCP.

**Статус и доступ.** QW Intelligence и MCP описаны как доступные, часть автоматизации остаётся в планах, документы по исполнению расходятся. Встроенный портфельный чат доступен на Wheel или Quant, есть демо. MCP включён в платные планы, набор инструментов и квоты зависят от плана.

**Запуск и важные изменения.** QW Intelligence подтверждён help от 2026-04-27, точный первый запуск неизвестен.

**Технология и границы.** Встроенный диалоговый ИИ и внешняя LLM через MCP. Поставщик встроенной модели не раскрыт, MCP поддерживает Claude, ChatGPT и совместимые клиенты. Справка встроенного чата ограничивает его исследованием без отправки сделок. Страница MCP описывает инструменты заявок, которые пользователь должен отдельно включить. Автоматические торговые агенты ещё анонсированы.

<details>
<summary>Источники и подтверждения</summary>

- [How to use QW Intelligence](https://quantwheel.com/how-to/qw-intelligence-overview)
- [Options Trading MCP for Claude and ChatGPT](https://quantwheel.com/mcp)
- [Agentic Options Trading Platform](https://quantwheel.com/)

</details>

<a name="rwb01"></a>

### Questrade Pro Intelligence и Questrade MCP

**Кому и зачем.** Канада. Исследовать бумагу в терминале и подготовить действие из внешнего AI-клиента.

**Что внедрено.**

- Intelligence отвечает на вопросы об акции, секторе и теме внутри браузерного терминала.
- Отдельный MCP использует позиции и историю брокерского счёта.
- MCP готовит заявку, а подтверждение приходит в приложение через Push Approval.

**Статус и доступ.** Questrade Pro в открытой beta, Intelligence и MCP документированы как доступные. Pro работает в браузере, Intelligence временно доступен для бесплатной пробы. MCP требует счёт, совместимый AI-клиент и настройку прав, подтверждения через приложение версии 2.0.0 и новее.

**Запуск и важные изменения.** Точные первые даты не установлены, текущие документы относятся к платформе 2026.

**Технология и границы.** Встроенный генеративный LLM-помощник и отдельное подключение внешних моделей. Intelligence предоставляется Boosted.ai, раскрыты инфраструктурные провайдеры OpenAI и Anthropic, конкретная модель не названа. Intelligence является информационным инструментом и не соединён с исполнением заявок. Торговые действия относятся к отдельному MCP, каждая заявка требует подтверждения. Автоматическое распознавание графических паттернов является другой функцией и не доказывает использование LLM.

<details>
<summary>Источники и подтверждения</summary>

- [Questrade AI Assistant: Important Disclosures and Risk Information](https://www.questrade.com/disclosure/legal-notice-and-disclosures/questrade-ai-assistant-important-disclosures-and-risk-information)
- [Questrade Pro: Open Beta](https://invest.questrade.com/questrade-pro)
- [Questrade MCP: Amplify your trading with AI](https://wealth.questrade.com/mcp)

</details>

## Профессиональные терминалы и исследовательские системы

Это B2B-сравнение. Доступ обычно зависит от профессиональной подписки, модулей и прав на источники. Наличие демо или технической возможности подключить физическое лицо не превращает такую систему в массовый B2C-продукт. Cbonds включён как российская профессиональная интеграция данных.

| Продукт | Что делает | Текущий статус |
|---|---|---|
| [Cbonds MCP Server](#ru11) | Запросить данные облигации и исторические котировки в диалоге вместо ручного запроса API | MCP описан как запущенный, интеграция с GigaCowork отдельно анонсирована |
| [Bloomberg Terminal: ASKB и GenAI summaries](#t08) | Анализ компаний и рынков с собственной перепиской, списками бумаг и файлами фирмы | ASKB generally available с 15.10.2026, раньше beta |
| [LSEG Workspace AI Search и Deep Research](#t09) | Сложные инвестиционные вопросы по структурированным и текстовым данным с проверяемым результатом | AI Search GA с июля 2026, Deep Research доступен |
| [FactSet Workstation: Mercury, Transcript Assistant, Pitch Creator](#t10) | Вопросы к earnings calls и подготовка данных/графиков/слайдов для анализа и инвестиционного банкинга | Поставлены Transcript Assistant и Pitch Creator, Mercury beta стартовала в 2023, API действует, v2 API обозначен beta |
| [S&P Capital IQ Pro: ChatIQ и Document Intelligence](#t11) | Сравнить компании и документы, построить screening/chart, подготовить модель или объяснить портфель | Основные функции выпущены, ChatIQ Presentations в Labs, Portfolio Insights beta |
| [AlphaSense Generative Search, Deep Research и workflow agents](#t12) | Исследование инвестиционной идеи, сравнение отрасли, due diligence и повторяющийся мониторинг | Доступен, отдельные коннекторы имеют beta-статус |

<a name="ru11"></a>

### Cbonds MCP Server

**Кому и зачем.** Россия, глобальная финансовая база. Запросить данные облигации и исторические котировки в диалоге вместо ручного запроса API.

**Что внедрено.**

- MCP-доступ к базе Cbonds.
- Запросы по облигациям естественным языком.
- Использование финансовых данных внутри внешнего ИИ-ассистента.

**Статус и доступ.** MCP описан как запущенный, интеграция с GigaCowork отдельно анонсирована. Требуется доступ к Cbonds API, стоимость и права уточняются у поставщика. Наличие подписки на сайт само по себе не доказывает доступ к API.

**Запуск и важные изменения.** Дата первого запуска MCP не раскрыта, договорённость с GigaCowork объявлена 2 октября 2026.

**Технология и границы.** Доступ внешней LLM к структурированным финансовым данным через MCP. Модель выбирает пользователь в совместимом ассистенте, страница перечисляет YandexGPT, ГигаЧат и ChatGPT. Профессиональный поставщик данных, а не массовый розничный торговый терминал. Договорённость об интеграции с GigaCowork не подтверждает её завершение.

<details>
<summary>Источники и подтверждения</summary>

- [Cbonds API & Data Feed](https://cbonds.ru/api/)
- [GigaCowork и Cbonds договорились об интеграции](https://cbonds.ru/news/4114583/)

</details>

<a name="t08"></a>

### Bloomberg Terminal: ASKB и GenAI summaries

**Кому и зачем.** США / международная профессиональная система. Анализ компаний и рынков с собственной перепиской, списками бумаг и файлами фирмы.

**Что внедрено.**

- Отвечает по данным, новостям и исследованиям Bloomberg.
- При разрешении анализирует три месяца собственной переписки Instant Bloomberg со ссылками.
- Учитывает списки бумаг Worksheets.
- Использует сохранённые файлы Bloomberg Drive вместе с рыночными источниками.

**Статус и доступ.** ASKB generally available с 15.10.2026, раньше beta. Профессиональная подписка Bloomberg Terminal/Bloomberg Anywhere, собственный контент включается и подчиняется правам доступа, отдельная retail подписка на ASKB не подтверждена.

**Запуск и важные изменения.** 2024-01-22 earnings-call summaries, 2026-02-23 ASKB beta, 2026-10-15 ASKB GA.

**Технология и границы.** Разговорный/агентный GenAI и LLM summaries. Рассмотренные продуктовые релизы не раскрывают актуальный полный набор моделей, BloombergGPT нельзя автоматически считать движком ASKB. ASKB доступен в профессиональном терминале, отдельные расширения из roadmap могут иметь иной статус. Собственный контент используется только в пределах прав доступа.

<details>
<summary>Источники и подтверждения</summary>

- [Bloomberg: The Next Evolution of ASKB: Your Insights, Bloomberg’s Intelligence, One Conversation](https://webdisclosure.com/press-release/bloomberg-nasdaq-the-next-evolution-of-askb-your-insights-bloombergs-intelligence-one-conversation-eiGHbvbH0WY)
- [Conheça o ASKB](https://www.bloomberg.com.br/blog/conheca-o-askb-a-primeira-visao-do-futuro-do-bloomberg-terminal-na-era-da-ia-agentica/)
- [Bloomberg Launches AI-Powered Earnings Call Summaries](https://www.prnewswire.com/news-releases/bloomberg-launches-ai-powered-earnings-call-summaries-302040670.html)
- [Bloomberg Unveils ASKB Roadmap](https://professional.content.cirrus.bloomberg.com/professional2023/insights/press-announcement/bloomberg-unveils-askb-roadmap-for-clients-to-augment-their-investment-process-with-agentic-ai/)

</details>

<a name="t09"></a>

### LSEG Workspace AI Search и Deep Research

**Кому и зачем.** Великобритания / международная профессиональная система. Сложные инвестиционные вопросы по структурированным и текстовым данным с проверяемым результатом.

**Что внедрено.**

- AI Search ищет по звонкам, раскрытиям, брокерским исследованиям и новостям.
- Deep Research соединяет цены, прогнозы аналитиков, фундаментальные и макроданные с документами.
- Показывает источники и допущения, создаёт графики и экспортирует Excel.
- Доступен в Workspace и Workspace в Microsoft Teams.

**Статус и доступ.** AI Search GA с июля 2026, Deep Research доступен. Подписка Workspace и соответствующие права на контент, коммерческие условия через LSEG, Microsoft Teams является дополнительным местом работы.

**Запуск и важные изменения.** 2026-06 Deep Research release page, 2026-07 AI Search GA.

**Технология и границы.** Генеративный ИИ координирует работу с лицензированными данными. Функции разработаны в партнёрстве LSEG и Microsoft с использованием нескольких моделей, их актуальные версии не раскрыты. Часть расширений данных ещё анонсирована. Доступ к функции и к отдельному источнику зависит от профессиональной подписки.

<details>
<summary>Источники и подтверждения</summary>

- [Your AI, your edge: Building personal productivity with AI](https://www.lseg.com/en/about-us/new-at-lseg/your-ai-your-edge-building-personal-productivity-with-ai)
- [LSEG introduces Deep Research agent in Workspace](https://www.lseg.com/en/data-analytics/products/workspace/updates/lseg-introduces-deep-research-agent-in-workspace)

</details>

<a name="t10"></a>

### FactSet Workstation: Mercury, Transcript Assistant, Pitch Creator

**Кому и зачем.** США / международная профессиональная система. Вопросы к earnings calls и подготовка данных/графиков/слайдов для анализа и инвестиционного банкинга.

**Что внедрено.**

- Transcript Assistant отвечает на вопросы по звонкам о результатах, прогнозам менеджмента и ключевым темам.
- Mercury и Chart Creator создают графики по запросу.
- Pitch Creator помогает с поиском, шаблонами Excel и слайдами PowerPoint.
- Conversational API позволяет встраивать диалог в интерфейсы клиента.

**Статус и доступ.** Поставлены Transcript Assistant и Pitch Creator, Mercury beta стартовала в 2023, API действует, v2 API обозначен beta. FactSet Workstation/коммерческие модули и entitlements, Transcript Assistant выпущен для всех типов фирм, что не равно бесплатному доступу любому физлицу.

**Запуск и важные изменения.** 2023-12-14 Mercury beta, 2024-03-12 Transcript Assistant, 2025-01-15 Pitch Creator.

**Технология и границы.** LLM-агент с диалогом, поиском и построением графиков. Текущие поставщик и версия модели не раскрыты. Transcript Assistant и Pitch Creator выпущены, это не устанавливает одинаковый статус всех интерфейсов Mercury. У Conversational API v2 обозначен beta-статус.

<details>
<summary>Источники и подтверждения</summary>

- [FactSet Launches FactSet Mercury to Supercharge Junior Banker Workflows](https://investor.factset.com/news-releases/news-release-details/factset-launches-factset-mercury-supercharge-junior-banker/)
- [FactSet Releases Transcript Assistant](https://investor.factset.com/news-releases/news-release-details/factset-releases-transcript-assistant-game-changing-ai-tool/)
- [FactSet Launches AI-Powered Pitch Creator](https://investor.factset.com/news-releases/news-release-details/factset-launches-ai-powered-pitch-creator/)
- [Conversational API Powered by FactSet Mercury. v2 beta 2025-08-28; текущая страница прочитана 2026-11-15.](https://developer.factset.com/api-catalog/conversational-api)

</details>

<a name="t11"></a>

### S&P Capital IQ Pro: ChatIQ и Document Intelligence

**Кому и зачем.** США / международная профессиональная система. Сравнить компании и документы, построить screening/chart, подготовить модель или объяснить портфель.

**Что внедрено.**

- ChatIQ сопоставляет несколько раскрытий, звонков, презентаций, новостей и исследований.
- Создаёт выборки и графики по словесному запросу.
- ChatIQ Spreadsheets помогает с моделями Excel и обновляемыми формулами.
- Portfolio Insights объясняет факторы результата и рыночные события в beta.

**Статус и доступ.** Основные функции выпущены, ChatIQ Presentations в Labs, Portfolio Insights beta. Коммерческая подписка Capital IQ Pro и права на модули/данные, Labs/beta могут требовать отдельного доступа.

**Запуск и важные изменения.** 2025-10-22 Document Intelligence2.0/multi-document, 2026-10-06 расширенный ChatIQ.

**Технология и границы.** Диалоговое исследование с генеративным ИИ, LLM-функции анализа документов. Kensho/S&P ecosystem, конкретный актуальный базовая языковая модель в релизах не раскрыт. Presentations нельзя считать функцией общего выпуска, Portfolio Insights в beta. Не подтверждены точные тарифы и доступность для частного российского клиента.

<details>
<summary>Источники и подтверждения</summary>

- [S&P Global Redefines Financial Insights with Multi-Document Research in ChatIQ](https://press.spglobal.com/2025-10-22-S-P-Global-Redefines-Financial-Insights-with-New-AI-Powered-Multi-Document-Research-and-Analysis-Tool-in-Capital-IQ-Pro-ChatIQ)
- [ChatIQ Leads S&P Global’s Latest Capital IQ Pro Update](https://press.spglobal.com/2026-10-06-ChatIQ-Leads-S-P-Globals-Latest-Capital-IQ-Pro-Update-with-Expanded-AI-Powered-Research-Capabilities)

</details>

<a name="t12"></a>

### AlphaSense Generative Search, Deep Research и workflow agents

**Кому и зачем.** США / международная профессиональная система. Исследование инвестиционной идеи, сравнение отрасли, due diligence и повторяющийся мониторинг.

**Что внедрено.**

- Отвечает по раскрытиям, звонкам, брокерским исследованиям, интервью с экспертами и финансовым данным.
- Deep Research выполняет многошаговый анализ.
- Поддерживает ссылки на фрагменты, исследования по расписанию и создание слайдов.
- Enterprise Intelligence добавляет внутренние документы и специализированных агентов.

**Статус и доступ.** Доступен, отдельные коннекторы имеют beta-статус. Коммерческий доступ AlphaSense, внутренние данные и diligence agents требуют Enterprise Intelligence, trial доступен по условиям поставщика.

**Запуск и важные изменения.** 2025-06-10 Deep Research, развитие workflow agents в 2026.

**Технология и границы.** Генеративные модели и многошаговые агентные сценарии. Точные актуальные версии моделей не раскрыты. Для Enterprise Intelligence доступны 13 агентов комплексной проверки, Zoom-коннектор находится в открытой бета-версии. Исполнение брокерских заявок этой функцией не установлено.

<details>
<summary>Источники и подтверждения</summary>

- [AlphaSense Launches Deep Research](https://www.alpha-sense.com/press/alphasense-launches-deep-research-automating-in-depth-analysis-with-agentic-ai-on-high-value-content/)
- [Quick Start Guide to Generative Search](https://help.alpha-sense.com/hc/en-us/articles/42591266633875-Quick-Start-Guide-to-Generative-Search)
- [AlphaSense Product Updates - August 2026](https://help.alpha-sense.com/hc/en-us/articles/54995224793875-AlphaSense-Product-Updates-August-2026)

</details>

## Российские терминалы: что есть внутри, а что подключается снаружи

У российских брокеров ИИ встречается в нескольких местах. Инвест-ассистент Т-Инвестиций и Финс БКС находятся в приложениях. MCP Т-Инвестиций, БКС и Финама соединяют внешнюю модель с брокерскими данными и инструментами. ZipLime является отдельной средой создания и запуска стратегий. Эти сценарии нельзя автоматически переносить на каждое торговое окно соответствующего брокера.

<details>
<summary>Источники и подтверждения</summary>

- [Вселенная AI-ассистентов Т-Банка](https://ai.tbank.ru/assistants/)
- [Тинькофф Инвестиции запустили инвестиционного ассистента на основе искусственного интеллекта](https://www.cnews.ru/news/line/2023-12-22_tinkoff_investitsii_zapustili)
- [Т-Инвестиции: официальный пост об AI Инвест-ассистенте](https://t.me/s/tb_invest_official/10541)
- [Два проекта БКС стали лучшими на GlobalCIO](https://habr.com/ru/companies/bcs_company/articles/992684/)
- [Помощник Финс от БКС: ваш персональный гид в мире финансов](https://globalcio.ru/projects/53411/)
- [БКС Мир инвестиций: голосовой ИИ-ассистент Финс](https://platforms.su/project/2467)
- [Финам запускает платформу ZipLime](https://www.finam.ru/publications/item/finam-zapuskaet-platformu-ziplime-s-pomoshchyu-kotoroy-algotreyderom-mozhet-stat-kazhdyy-20260831-1642/)
- [Как автоматизировать свою стратегию за 10 минут без написания кода](https://www.finam.ru/publications/item/kak-avtomatizirovat-svoyu-strategiyu-za-10-minut-bez-napisaniya-koda-20260706-0900/)
- [ZIPLIME: от идеи до сделки](https://ziplime.finam.ru/home)
- [ZIPLIME: from idea to deal](https://ziplime.limex.com/home)

</details>

| Платформа | Подтверждённый сценарий | Граница |
|---|---|---|
| Т-Инвестиции | Встроенный аналитический ассистент, отдельно T-Invest MCP | Торговые права MCP не устанавливают те же права чата и терминала |
| БКС | Финс в приложении, отдельно Trade API MCP | Роль консультанта и роль внешнего агента различаются |
| FinamTrade | Внешний MCP с портфелем, данными и графиками | Торговля через MCP на 2 ноября 2026 ещё тестируется |
| ZipLime | Генерация кода, бэктест и запуск через Trade API | Отдельная платформа, модели и условия глобального Limex могут отличаться |
| QUIK | Платформа и средства интеграции | Подтверждения встроенной LLM на рассмотренной продуктовой странице нет |
| TRANSAQ | Торговый терминал, программируемые индикаторы и интеграции | Подтверждения встроенной LLM на официальном сайте нет |
| АЛОР | Торговая инфраструктура и API | API позволяет строить внешние приложения, встроенный помощник на языковой модели этой документацией не подтверждён |

По T-Invest MCP, БКС и Finam MCP возможности раскрыты в отдельных инструкциях. У QUIK, TRANSAQ и АЛОР отсутствие подтверждения встроенной LLM относится к перечисленным открытым страницам и не доказывает отсутствие любых пилотов, партнёрских решений или внешних интеграций.

<details>
<summary>Источники и подтверждения</summary>

- [ИИ-агенты в инвестициях: собираем Telegram-ассистента и торгового робота на MCP Т-Инвестиций](https://habr.com/ru/companies/tbank/articles/1086714/)
- [Сбер внедрит ИИ-сервис для управления инвестиционным портфелем](https://www.vedomosti.ru/investments/news/2026/09/11/1228241-sber-ii-servis)
- [T-Invest MCP: официальная документация](https://developer.tbank.ru/invest/mcp)
- [MCP сервер: БКС Торговое API](https://trade-api.bcs.ru/mcp/)
- [За последний месяц сразу три российских брокера разрешили инвесторам использовать ИИ](https://www.bfm.ru/news/617766)
- [MCP Финама, которые превращают вашу LLM в личного аналитика](https://www.finam.ru/publications/item/mcp-finama-kotorye-prevrashchayut-vashu-llm-v-lichnogo-analitika-20261025-1200/)
- [Finam MCP: данные счёта для ИИ-агента](https://broker.finam.ru/landing/mcp/)
- [Член правления Финама представил Finam MCP на SmartLab CONF 2026](https://www.finam.ru/publications/item/chlen-pravleniya-finama-predstavil-finam-mcp-na-smartlab-conf-2026-20261102-1658/)
- [Подключение MCP AI-скринера Финама](https://ai.finam.ru/connection-mcp)
- [Программный комплекс QUIK: ARQA Technologies](https://arqatech.com/ru/products/quik/)
- [TRANSAQ: система брокерского обслуживания, официальный сайт](https://www.transaq.ru/)
- [АЛОР Брокер API: официальная документация](https://alor.dev/docs/)

</details>

[Обзор](README.md) | [Брокеры](brokers.md) | [Самостоятельные сервисы](research-services.md) | [Россия](russia.md) | [Терминалы](terminals.md) | [Фонды](funds.md) | [Источники](sources.md)
