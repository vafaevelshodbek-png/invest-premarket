# ИИ в розничных и профессиональных терминалах

Срез на 15 ноября 2026 года.

[Обзор](README.md) | [Мировые брокеры](brokers.md) | [Сервисы](research-services.md) | [Россия](russia.md) | [Терминалы](terminals.md) | [Фонды](funds.md) | [Источники](sources.md)

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
| [QuantWheel QW Intelligence и MCP](#t07) | Поиск опционных возможностей, анализ позиций, рыночных потоков и торгового журнала | QW Intelligence и MCP описаны как доступные, часть automation остаётся coming soon, документы по исполнению расходятся |
| [Questrade Pro Intelligence и Questrade MCP](#rwb01) | Исследовать бумагу в терминале и подготовить действие из внешнего AI-клиента | Questrade Pro в открытой beta, Intelligence и MCP документированы как доступные |

<a name="t01"></a>

### TradingView AI Copilot

**Кому и зачем.** Международная платформа. Анализ инструмента, настройка рабочего места, скрининг и разработка индикаторов/стратегий.

**Что внедрено.** Учитывает открытый график и финансовые данные TradingView. Меняет индикаторы и разметку, создаёт уведомления и списки наблюдения. Генерирует Pine Script и объясняет результаты бэктеста. Подбирает инструменты по условиям, заданным обычным языком. [115](https://www.tradingview.com/support/solutions/43000795131-getting-started-with-ai-copilot/) [116](https://www.tradingview.com/blog/en/ai-copilot-now-on-tradingview-61231/) [117](https://www.tradingview.com/blog/en/ai-copilot-claude-chatgpt-deepseek-62292/)

**Статус и доступ.** Доступен как native add-on, прежнее расширение beta более не поддерживается активно. Любой платный план Essential/Plus/Premium/Ultimate плюс отдельный ежемесячный add-on, web и desktop, mobile пока не поддерживается. Первый запуск или важный этап: 2026-04-02 public beta расширения, 2026-09-28 native. [115](https://www.tradingview.com/support/solutions/43000795131-getting-started-with-ai-copilot/) [116](https://www.tradingview.com/blog/en/ai-copilot-now-on-tradingview-61231/) [117](https://www.tradingview.com/blog/en/ai-copilot-claude-chatgpt-deepseek-62292/)

**Технология и границы.** LLM/генеративный ИИ с инструментами платформы. Обновление 09.11.2026 называет DeepSeek V4.1 Flash, GPT-6 Luna, Claude Sonnet 5.5, модель выбирается для чата. Есть месячный лимит использования, поставщик предупреждает об ошибках. Исполнение брокерских заявок этой справкой не подтверждено. Доступность конкретного российского аккаунта не проверена. [115](https://www.tradingview.com/support/solutions/43000795131-getting-started-with-ai-copilot/) [116](https://www.tradingview.com/blog/en/ai-copilot-now-on-tradingview-61231/) [117](https://www.tradingview.com/blog/en/ai-copilot-claude-chatgpt-deepseek-62292/)


<a name="t02"></a>

### TrendSpider Sidekick AI

**Кому и зачем.** США / международная платформа. Связать анализ рынка с созданием сканера, индикатора, теста и алерта.

**Что внедрено.** Исследует графики, финансовые показатели, отчётность и звонки по результатам. Создаёт и запускает сканеры и бэктесты, пишет индикаторы. Готовит уведомления и торговых роботов. Получает данные о позициях через поддерживаемое подключение брокера и SignalStack. [118](https://trendspider.com/product/sidekick-ai-trading-assistant) [119](https://trendspider.reamaze.com/kb/sidekick/trendspider-sidekick)

**Статус и доступ.** Доступен. 25 сообщений в месяц включены в каждую подписку TrendSpider, отдельные Sidekick пакеты Basic $49, Plus $129, Max $349 в месяц добавляют лимиты и модели. Первый запуск или важный этап: Точная первоначальная дата не установлена. [118](https://trendspider.com/product/sidekick-ai-trading-assistant) [119](https://trendspider.reamaze.com/kb/sidekick/trendspider-sidekick)

**Технология и границы.** Многомодельный LLM-агент с инструментами платформы. Поддерживаются модели Anthropic, OpenAI и Google, доступный набор обновляется и зависит от тарифа. Базовая подписка оплачивается отдельно от дополнительных пакетов Sidekick. Доступ к позициям требует поддерживаемого подключения. Бэктест не устанавливает будущую доходность. [118](https://trendspider.com/product/sidekick-ai-trading-assistant) [119](https://trendspider.reamaze.com/kb/sidekick/trendspider-sidekick)


<a name="t03"></a>

### MetaTrader 5 AI Assistant и MCP

**Кому и зачем.** Международная платформа через брокеров. Анализ рынка и счёта, исследование стратегии, разработка MQL5 и операции через инструменты.

**Что внедрено.** Читает котировки, открытые позиции и торговую историю. Настраивает графики, тестирует и оптимизирует Expert Advisors. Генерирует/исправляет MQL5 код. Может выполнять поддерживаемые торговые операции при разрешении пользователя. [120](https://www.metatrader5.com/en/terminal/help/mcp_and_ai) [121](https://www.metatrader5.com/en/news/2453) [122](https://www.metaquotes.com/en/company/news/5567)

**Статус и доступ.** Встроен в выпущенную desktop-платформу. Обновлённая desktop-версия MT5 и вход в MQL5.community, MQL5 lite бесплатно, альтернативные провайдеры по своим ключам/условиям. Первый запуск или важный этап: 2026-07-24, build 6060, MetaEditor text/code assistant с 2023-06-14. [120](https://www.metatrader5.com/en/terminal/help/mcp_and_ai) [121](https://www.metatrader5.com/en/news/2453) [122](https://www.metaquotes.com/en/company/news/5567)

**Технология и границы.** LLM-агент с доступом к MCP инструментам терминала и MetaEditor. Бесплатная MQL5 lite по умолчанию, доступны собственные ключи моделей OpenAI, Anthropic, Google и других провайдеров. Торговлю, web и shell можно ограничить отдельно, поддерживаемые инструменты зависят от терминала и брокера. Факт native LLM в MT5 нельзя автоматически переносить на MT4, web/mobile и любого брокера. [120](https://www.metatrader5.com/en/terminal/help/mcp_and_ai) [121](https://www.metatrader5.com/en/news/2453) [122](https://www.metaquotes.com/en/company/news/5567)


<a name="t04"></a>

### Koyfin Compare Matrix и AI Summary

**Кому и зачем.** США / международный сервис. Сравнить содержание раскрытий компаний по конкурентам и кварталам, объяснить атрибуцию портфеля.

**Что внедрено.** Сравнивает одну компанию по кварталам или несколько компаний между собой. Отвечает по отчётности, звонкам, новостям и релизам. Показывает ссылки на источники в ячейках и экспортирует CSV. AI Summary объясняет причины отклонения результата модельного портфеля от бенчмарка на тарифе Advisor Pro. [123](https://www.koyfin.com/help/release-notes/compare-matrix-beta/) [124](https://www.koyfin.com/help/release-notes/attribution-in-model-portfolios/)

**Статус и доступ.** Compare Matrix beta, AI Summary в attribution доступен Advisor Pro. Compare Matrix находится в Research Tools, beta с месячной token-квотой, конкретный тариф для beta не указан. AI Summary в attribution требует Advisor Pro. Первый запуск или важный этап: 2026-10-01 Compare Matrix, 2026-09-01 attribution AI Summary. [123](https://www.koyfin.com/help/release-notes/compare-matrix-beta/) [124](https://www.koyfin.com/help/release-notes/attribution-in-model-portfolios/)

**Технология и границы.** LLM прямо подтверждена для Compare Matrix, генерация текста для AI Summary. Поставщик и версия LLM не раскрыты в рассмотренных инструкциях. Beta лимиты временные, обновление ответа расходует квоту. Нельзя объявлять весь Koyfin LLM-продуктом или автоматически относить advisor AI Summary к розничному тарифу. [123](https://www.koyfin.com/help/release-notes/compare-matrix-beta/) [124](https://www.koyfin.com/help/release-notes/attribution-in-model-portfolios/)


<a name="t05"></a>

### Trade Ideas AI Assistant, отдельно Holly AI Signals

**Кому и зачем.** США. Создать рыночный сканер по описанию и объяснить открытый график.

**Что внедрено.** Создаёт окно Alert или список Top List по текстовому запросу. Объясняет открытый график. Дополняется инструментом OddsMaker для проверки условий. [125](https://forums.trade-ideas.com/ai-assistant-for-trading/) [126](https://www.trade-ideas.com/cms_static/PDF/Trade%20Ideas_Leveraging_AI_Maximize_First_Impression_Brief.pdf)

**Статус и доступ.** AI Assistant доступен, конкретная LLM не подтверждена. AI Assistant включён в TI Pro на всех планах Trade Ideas, Holly AI Signals и OddsMaker относятся к TI Premium. Первый запуск или важный этап: AI Assistant подтверждён текущей страницей, точная дата первичного запуска не установлена. [125](https://forums.trade-ideas.com/ai-assistant-for-trading/) [126](https://www.trade-ideas.com/cms_static/PDF/Trade%20Ideas_Leveraging_AI_Maximize_First_Impression_Brief.pdf)

**Технология и границы.** Диалоговый AI Assistant, отдельно Holly Signals на алгоритмах и машинном обучении. LLM-архитектура и базовая модель помощника не раскрыты. AI Assistant и Holly Signals решают разные задачи. Данные и исполнение у брокера имеют собственные условия. [125](https://forums.trade-ideas.com/ai-assistant-for-trading/) [126](https://www.trade-ideas.com/cms_static/PDF/Trade%20Ideas_Leveraging_AI_Maximize_First_Impression_Brief.pdf)


<a name="t06"></a>

### TradeStation MCP

**Кому и зачем.** США. Разбирать позиции и пользоваться функциями брокерской экосистемы из диалога.

**Что внедрено.** Подключает внешнего ИИ-ассистента к брокерскому счёту TradeStation. Поддерживает заявленные сценарии анализа позиций и торговой автоматизации. [127](https://www.tradestation.com/press-and-news/tradestation-securities-releases-mcp-connection-allowing-users-to-connect-trading-accounts-with-third-party-ai-platforms/) [128](https://www.monexgroup.jp/jp/news_release/irnews/auto_20260115534412/pdfFile.pdf) [129](https://help.tradestation.com/10_00/eng/tradestationhelp/default/releasenotes_archives.htm)

**Статус и доступ.** Выпущен для клиентов с условиями доступа. Нужен брокерский счёт, соблюдение требований к нему и необходимых разрешений, на запуске требовалась подписка Claude Pro. Первый запуск или важный этап: 2026-01-13. [127](https://www.tradestation.com/press-and-news/tradestation-securities-releases-mcp-connection-allowing-users-to-connect-trading-accounts-with-third-party-ai-platforms/) [128](https://www.monexgroup.jp/jp/news_release/irnews/auto_20260115534412/pdfFile.pdf) [129](https://help.tradestation.com/10_00/eng/tradestationhelp/default/releasenotes_archives.htm)

**Технология и границы.** Подключение брокерского аккаунта к внешней LLM через MCP. На запуске Claude от Anthropic, расширение списка AI-платформ анонсировано. Официальный MCP подключает внешний AI-клиент. Встроенный Self-Help отвечает о функциях платформы, его инвестиционные исследовательские возможности отдельно не установлены. [127](https://www.tradestation.com/press-and-news/tradestation-securities-releases-mcp-connection-allowing-users-to-connect-trading-accounts-with-third-party-ai-platforms/) [128](https://www.monexgroup.jp/jp/news_release/irnews/auto_20260115534412/pdfFile.pdf) [129](https://help.tradestation.com/10_00/eng/tradestationhelp/default/releasenotes_archives.htm)


<a name="t07"></a>

### QuantWheel QW Intelligence и MCP

**Кому и зачем.** Международный сервис с фокусом на опционы США. Поиск опционных возможностей, анализ позиций, рыночных потоков и торгового журнала.

**Что внедрено.** Переводит словесный запрос в скринер с заданными фильтрами. Учитывает рынок и собственные позиции на подходящем платном плане. Передаёт внешнему ассистенту данные экспозиции к гамме, потоков, портфеля и журнала через MCP. [130](https://quantwheel.com/how-to/qw-intelligence-overview) [131](https://quantwheel.com/mcp) [132](https://quantwheel.com/)

**Статус и доступ.** QW Intelligence и MCP описаны как доступные, часть automation остаётся coming soon, документы по исполнению расходятся. Встроенный портфельный чат доступен на Wheel или Quant, есть демо. MCP включён в платные планы, набор инструментов и квоты зависят от плана. Первый запуск или важный этап: QW Intelligence подтверждён help от 2026-04-27, точный первый запуск неизвестен. [130](https://quantwheel.com/how-to/qw-intelligence-overview) [131](https://quantwheel.com/mcp) [132](https://quantwheel.com/)

**Технология и границы.** Встроенный диалоговый ИИ и внешняя LLM через MCP. Поставщик встроенной модели не раскрыт, MCP поддерживает Claude, ChatGPT и совместимые клиенты. Справка встроенного чата ограничивает его исследованием без отправки сделок. Страница MCP описывает инструменты заявок, которые пользователь должен отдельно включить. Автоматические торговые агенты ещё анонсированы. [130](https://quantwheel.com/how-to/qw-intelligence-overview) [131](https://quantwheel.com/mcp) [132](https://quantwheel.com/)


<a name="rwb01"></a>

### Questrade Pro Intelligence и Questrade MCP

**Кому и зачем.** Канада. Исследовать бумагу в терминале и подготовить действие из внешнего AI-клиента.

**Что внедрено.** Intelligence отвечает на вопросы об акции, секторе и теме внутри браузерного терминала. Отдельный MCP использует позиции и историю брокерского счёта. MCP готовит заявку, а подтверждение приходит в приложение через Push Approval. [233](https://www.questrade.com/disclosure/legal-notice-and-disclosures/questrade-ai-assistant-important-disclosures-and-risk-information) [234](https://invest.questrade.com/questrade-pro) [235](https://wealth.questrade.com/mcp)

**Статус и доступ.** Questrade Pro в открытой beta, Intelligence и MCP документированы как доступные. Pro работает в браузере, Intelligence временно доступен для бесплатной пробы. MCP требует счёт, совместимый AI-клиент и настройку прав, подтверждения через приложение версии 2.0.0 и новее. Первый запуск или важный этап: Точные первые даты не установлены, текущие документы относятся к платформе 2026. [233](https://www.questrade.com/disclosure/legal-notice-and-disclosures/questrade-ai-assistant-important-disclosures-and-risk-information) [234](https://invest.questrade.com/questrade-pro) [235](https://wealth.questrade.com/mcp)

**Технология и границы.** Встроенный генеративный LLM-помощник и отдельное подключение внешних моделей. Intelligence предоставляется Boosted.ai, раскрыты инфраструктурные провайдеры OpenAI и Anthropic, конкретная модель не названа. Intelligence является информационным инструментом и не соединён с исполнением заявок. Торговые действия относятся к отдельному MCP, каждая заявка требует подтверждения. Автоматическое распознавание графических паттернов является другой функцией и не доказывает использование LLM. [233](https://www.questrade.com/disclosure/legal-notice-and-disclosures/questrade-ai-assistant-important-disclosures-and-risk-information) [234](https://invest.questrade.com/questrade-pro) [235](https://wealth.questrade.com/mcp)

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

**Что внедрено.** MCP-доступ к базе Cbonds. Запросы по облигациям естественным языком. Использование финансовых данных внутри внешнего ИИ-ассистента. [110](https://cbonds.ru/api/) [111](https://cbonds.ru/news/4114583/)

**Статус и доступ.** MCP описан как запущенный, интеграция с GigaCowork отдельно анонсирована. Требуется доступ к Cbonds API, стоимость и права уточняются у поставщика. Наличие подписки на сайт само по себе не доказывает доступ к API. Первый запуск или важный этап: Дата первого запуска MCP не раскрыта, договорённость с GigaCowork объявлена 2 октября 2026. [110](https://cbonds.ru/api/) [111](https://cbonds.ru/news/4114583/)

**Технология и границы.** Доступ внешней LLM к структурированным финансовым данным через MCP. Модель выбирает пользователь в совместимом ассистенте, страница перечисляет YandexGPT, ГигаЧат и ChatGPT. Профессиональный поставщик данных, а не массовый розничный торговый терминал. Договорённость об интеграции с GigaCowork не подтверждает её завершение. [110](https://cbonds.ru/api/) [111](https://cbonds.ru/news/4114583/)


<a name="t08"></a>

### Bloomberg Terminal: ASKB и GenAI summaries

**Кому и зачем.** США / международная профессиональная система. Анализ компаний и рынков с собственной перепиской, списками бумаг и файлами фирмы.

**Что внедрено.** Отвечает по данным, новостям и исследованиям Bloomberg. При разрешении анализирует три месяца собственной переписки Instant Bloomberg со ссылками. Учитывает списки бумаг Worksheets. Использует сохранённые файлы Bloomberg Drive вместе с рыночными источниками. [133](https://webdisclosure.com/press-release/bloomberg-nasdaq-the-next-evolution-of-askb-your-insights-bloombergs-intelligence-one-conversation-eiGHbvbH0WY) [134](https://www.bloomberg.com.br/blog/conheca-o-askb-a-primeira-visao-do-futuro-do-bloomberg-terminal-na-era-da-ia-agentica/) [135](https://www.prnewswire.com/news-releases/bloomberg-launches-ai-powered-earnings-call-summaries-302040670.html) [136](https://professional.content.cirrus.bloomberg.com/professional2023/insights/press-announcement/bloomberg-unveils-askb-roadmap-for-clients-to-augment-their-investment-process-with-agentic-ai/)

**Статус и доступ.** ASKB generally available с 15.10.2026, раньше beta. Профессиональная подписка Bloomberg Terminal/Bloomberg Anywhere, собственный контент включается и подчиняется правам доступа, отдельная retail подписка на ASKB не подтверждена. Первый запуск или важный этап: 2024-01-22 earnings-call summaries, 2026-02-23 ASKB beta, 2026-10-15 ASKB GA. [133](https://webdisclosure.com/press-release/bloomberg-nasdaq-the-next-evolution-of-askb-your-insights-bloombergs-intelligence-one-conversation-eiGHbvbH0WY) [134](https://www.bloomberg.com.br/blog/conheca-o-askb-a-primeira-visao-do-futuro-do-bloomberg-terminal-na-era-da-ia-agentica/) [135](https://www.prnewswire.com/news-releases/bloomberg-launches-ai-powered-earnings-call-summaries-302040670.html) [136](https://professional.content.cirrus.bloomberg.com/professional2023/insights/press-announcement/bloomberg-unveils-askb-roadmap-for-clients-to-augment-their-investment-process-with-agentic-ai/)

**Технология и границы.** Разговорный/агентный GenAI и LLM summaries. Рассмотренные продуктовые релизы не раскрывают актуальный полный набор моделей, BloombergGPT нельзя автоматически считать движком ASKB. ASKB доступен в профессиональном терминале, отдельные расширения из roadmap могут иметь иной статус. Собственный контент используется только в пределах прав доступа. [133](https://webdisclosure.com/press-release/bloomberg-nasdaq-the-next-evolution-of-askb-your-insights-bloombergs-intelligence-one-conversation-eiGHbvbH0WY) [134](https://www.bloomberg.com.br/blog/conheca-o-askb-a-primeira-visao-do-futuro-do-bloomberg-terminal-na-era-da-ia-agentica/) [135](https://www.prnewswire.com/news-releases/bloomberg-launches-ai-powered-earnings-call-summaries-302040670.html) [136](https://professional.content.cirrus.bloomberg.com/professional2023/insights/press-announcement/bloomberg-unveils-askb-roadmap-for-clients-to-augment-their-investment-process-with-agentic-ai/)


<a name="t09"></a>

### LSEG Workspace AI Search и Deep Research

**Кому и зачем.** Великобритания / международная профессиональная система. Сложные инвестиционные вопросы по структурированным и текстовым данным с проверяемым результатом.

**Что внедрено.** AI Search ищет по звонкам, раскрытиям, брокерским исследованиям и новостям. Deep Research соединяет цены, прогнозы аналитиков, фундаментальные и макроданные с документами. Показывает источники и допущения, создаёт графики и экспортирует Excel. Доступен в Workspace и Workspace в Microsoft Teams. [137](https://www.lseg.com/en/about-us/new-at-lseg/your-ai-your-edge-building-personal-productivity-with-ai) [138](https://www.lseg.com/en/data-analytics/products/workspace/updates/lseg-introduces-deep-research-agent-in-workspace)

**Статус и доступ.** AI Search GA с июля 2026, Deep Research доступен. Подписка Workspace и соответствующие права на контент, коммерческие условия через LSEG, Microsoft Teams является дополнительным местом работы. Первый запуск или важный этап: 2026-06 Deep Research release page, 2026-07 AI Search GA. [137](https://www.lseg.com/en/about-us/new-at-lseg/your-ai-your-edge-building-personal-productivity-with-ai) [138](https://www.lseg.com/en/data-analytics/products/workspace/updates/lseg-introduces-deep-research-agent-in-workspace)

**Технология и границы.** Генеративный ИИ координирует работу с лицензированными данными. Функции разработаны в партнёрстве LSEG и Microsoft с использованием нескольких моделей, их актуальные версии не раскрыты. Часть расширений данных ещё анонсирована. Доступ к функции и к отдельному источнику зависит от профессиональной подписки. [137](https://www.lseg.com/en/about-us/new-at-lseg/your-ai-your-edge-building-personal-productivity-with-ai) [138](https://www.lseg.com/en/data-analytics/products/workspace/updates/lseg-introduces-deep-research-agent-in-workspace)


<a name="t10"></a>

### FactSet Workstation: Mercury, Transcript Assistant, Pitch Creator

**Кому и зачем.** США / международная профессиональная система. Вопросы к earnings calls и подготовка данных/графиков/слайдов для анализа и инвестиционного банкинга.

**Что внедрено.** Transcript Assistant отвечает на вопросы по звонкам о результатах, прогнозам менеджмента и ключевым темам. Mercury и Chart Creator создают графики по запросу. Pitch Creator помогает с поиском, шаблонами Excel и слайдами PowerPoint. Conversational API позволяет встраивать диалог в интерфейсы клиента. [139](https://investor.factset.com/news-releases/news-release-details/factset-launches-factset-mercury-supercharge-junior-banker/) [140](https://investor.factset.com/news-releases/news-release-details/factset-releases-transcript-assistant-game-changing-ai-tool/) [141](https://investor.factset.com/news-releases/news-release-details/factset-launches-ai-powered-pitch-creator/) [142](https://developer.factset.com/api-catalog/conversational-api)

**Статус и доступ.** Поставлены Transcript Assistant и Pitch Creator, Mercury beta стартовала в 2023, API действует, v2 API обозначен beta. FactSet Workstation/коммерческие модули и entitlements, Transcript Assistant выпущен для всех типов фирм, что не равно бесплатному доступу любому физлицу. Первый запуск или важный этап: 2023-12-14 Mercury beta, 2024-03-12 Transcript Assistant, 2025-01-15 Pitch Creator. [139](https://investor.factset.com/news-releases/news-release-details/factset-launches-factset-mercury-supercharge-junior-banker/) [140](https://investor.factset.com/news-releases/news-release-details/factset-releases-transcript-assistant-game-changing-ai-tool/) [141](https://investor.factset.com/news-releases/news-release-details/factset-launches-ai-powered-pitch-creator/) [142](https://developer.factset.com/api-catalog/conversational-api)

**Технология и границы.** LLM-агент с диалогом, поиском и построением графиков. Текущие поставщик и версия модели не раскрыты. Transcript Assistant и Pitch Creator выпущены, это не устанавливает одинаковый статус всех интерфейсов Mercury. У Conversational API v2 обозначен beta-статус. [139](https://investor.factset.com/news-releases/news-release-details/factset-launches-factset-mercury-supercharge-junior-banker/) [140](https://investor.factset.com/news-releases/news-release-details/factset-releases-transcript-assistant-game-changing-ai-tool/) [141](https://investor.factset.com/news-releases/news-release-details/factset-launches-ai-powered-pitch-creator/) [142](https://developer.factset.com/api-catalog/conversational-api)


<a name="t11"></a>

### S&P Capital IQ Pro: ChatIQ и Document Intelligence

**Кому и зачем.** США / международная профессиональная система. Сравнить компании и документы, построить screening/chart, подготовить модель или объяснить портфель.

**Что внедрено.** ChatIQ сопоставляет несколько раскрытий, звонков, презентаций, новостей и исследований. Создаёт выборки и графики по словесному запросу. ChatIQ Spreadsheets помогает с моделями Excel и обновляемыми формулами. Portfolio Insights объясняет факторы результата и рыночные события в beta. [143](https://press.spglobal.com/2025-10-22-S-P-Global-Redefines-Financial-Insights-with-New-AI-Powered-Multi-Document-Research-and-Analysis-Tool-in-Capital-IQ-Pro-ChatIQ) [144](https://press.spglobal.com/2026-10-06-ChatIQ-Leads-S-P-Globals-Latest-Capital-IQ-Pro-Update-with-Expanded-AI-Powered-Research-Capabilities)

**Статус и доступ.** Основные функции выпущены, ChatIQ Presentations в Labs, Portfolio Insights beta. Коммерческая подписка Capital IQ Pro и права на модули/данные, Labs/beta могут требовать отдельного доступа. Первый запуск или важный этап: 2025-10-22 Document Intelligence2.0/multi-document, 2026-10-06 расширенный ChatIQ. [143](https://press.spglobal.com/2025-10-22-S-P-Global-Redefines-Financial-Insights-with-New-AI-Powered-Multi-Document-Research-and-Analysis-Tool-in-Capital-IQ-Pro-ChatIQ) [144](https://press.spglobal.com/2026-10-06-ChatIQ-Leads-S-P-Globals-Latest-Capital-IQ-Pro-Update-with-Expanded-AI-Powered-Research-Capabilities)

**Технология и границы.** GenAI conversational research, LLM-функции анализа документов. Kensho/S&P ecosystem, конкретный актуальный foundation model в релизах не раскрыт. Presentations нельзя считать обычной GA-функцией, Portfolio Insights в beta. Не подтверждены точные тарифы и доступность для частного российского клиента. [143](https://press.spglobal.com/2025-10-22-S-P-Global-Redefines-Financial-Insights-with-New-AI-Powered-Multi-Document-Research-and-Analysis-Tool-in-Capital-IQ-Pro-ChatIQ) [144](https://press.spglobal.com/2026-10-06-ChatIQ-Leads-S-P-Globals-Latest-Capital-IQ-Pro-Update-with-Expanded-AI-Powered-Research-Capabilities)


<a name="t12"></a>

### AlphaSense Generative Search, Deep Research и workflow agents

**Кому и зачем.** США / международная профессиональная система. Исследование инвестиционной идеи, сравнение отрасли, due diligence и повторяющийся мониторинг.

**Что внедрено.** Отвечает по раскрытиям, звонкам, брокерским исследованиям, интервью с экспертами и финансовым данным. Deep Research выполняет многошаговый анализ. Поддерживает ссылки на фрагменты, исследования по расписанию и создание слайдов. Enterprise Intelligence добавляет внутренние документы и специализированных агентов. [145](https://www.alpha-sense.com/press/alphasense-launches-deep-research-automating-in-depth-analysis-with-agentic-ai-on-high-value-content/) [146](https://help.alpha-sense.com/hc/en-us/articles/42591266633875-Quick-Start-Guide-to-Generative-Search) [147](https://help.alpha-sense.com/hc/en-us/articles/54995224793875-AlphaSense-Product-Updates-August-2026)

**Статус и доступ.** Доступен, отдельные коннекторы имеют beta-статус. Коммерческий доступ AlphaSense, внутренние данные и diligence agents требуют Enterprise Intelligence, trial доступен по условиям поставщика. Первый запуск или важный этап: 2025-06-10 Deep Research, развитие workflow agents в 2026. [145](https://www.alpha-sense.com/press/alphasense-launches-deep-research-automating-in-depth-analysis-with-agentic-ai-on-high-value-content/) [146](https://help.alpha-sense.com/hc/en-us/articles/42591266633875-Quick-Start-Guide-to-Generative-Search) [147](https://help.alpha-sense.com/hc/en-us/articles/54995224793875-AlphaSense-Product-Updates-August-2026)

**Технология и границы.** Генеративные модели и многошаговые агентные сценарии. Точные актуальные версии моделей не раскрыты. Для Enterprise Intelligence доступны 13 агентов комплексной проверки, Zoom-коннектор находится в открытой бета-версии. Исполнение брокерских заявок этой функцией не установлено. [145](https://www.alpha-sense.com/press/alphasense-launches-deep-research-automating-in-depth-analysis-with-agentic-ai-on-high-value-content/) [146](https://help.alpha-sense.com/hc/en-us/articles/42591266633875-Quick-Start-Guide-to-Generative-Search) [147](https://help.alpha-sense.com/hc/en-us/articles/54995224793875-AlphaSense-Product-Updates-August-2026)

## Российские терминалы: что есть внутри, а что подключается снаружи

У российских брокеров ИИ встречается в нескольких местах. Инвест-ассистент Т-Инвестиций и Финс БКС находятся в приложениях. MCP Т-Инвестиций, БКС и Финама соединяют внешнюю модель с брокерскими данными и инструментами. ZipLime является отдельной средой создания и запуска стратегий. Эти сценарии нельзя автоматически переносить на каждое торговое окно соответствующего брокера. [83](https://ai.tbank.ru/assistants/) [84](https://www.cnews.ru/news/line/2023-12-22_tinkoff_investitsii_zapustili) [85](https://t.me/s/tb_invest_official/10541) [89](https://habr.com/ru/companies/bcs_company/articles/992684/) [90](https://globalcio.ru/projects/53411/) [91](https://platforms.su/project/2467) [101](https://www.finam.ru/publications/item/finam-zapuskaet-platformu-ziplime-s-pomoshchyu-kotoroy-algotreyderom-mozhet-stat-kazhdyy-20260831-1642/) [102](https://www.finam.ru/publications/item/kak-avtomatizirovat-svoyu-strategiyu-za-10-minut-bez-napisaniya-koda-20260706-0900/) [103](https://ziplime.finam.ru/home) [104](https://ziplime.limex.com/home)

| Платформа | Подтверждённый сценарий | Граница |
|---|---|---|
| Т-Инвестиции | Встроенный аналитический ассистент, отдельно T-Invest MCP | Торговые права MCP не устанавливают те же права чата и терминала |
| БКС | Финс в приложении, отдельно Trade API MCP | Роль консультанта и роль внешнего агента различаются |
| FinamTrade | Внешний MCP с портфелем, данными и графиками | Торговля через MCP на 2 ноября 2026 ещё тестируется |
| ZipLime | Генерация кода, бэктест и запуск через Trade API | Отдельная платформа, модели и условия глобального Limex могут отличаться |
| QUIK | Платформа и средства интеграции | Подтверждения встроенной LLM на рассмотренной продуктовой странице нет |
| TRANSAQ | Торговый терминал, программируемые индикаторы и интеграции | Подтверждения встроенной LLM на официальном сайте нет |
| АЛОР | Торговая инфраструктура и API | API позволяет строить внешние приложения, native LLM-помощник этой документацией не подтверждён |

По T-Invest MCP, БКС и Finam MCP возможности раскрыты в отдельных инструкциях. У QUIK, TRANSAQ и АЛОР отсутствие подтверждения встроенной LLM относится к перечисленным открытым страницам и не доказывает отсутствие любых пилотов, партнёрских решений или внешних интеграций. [86](https://habr.com/ru/companies/tbank/articles/1086714/) [87](https://www.vedomosti.ru/investments/news/2026/09/11/1228241-sber-ii-servis) [88](https://developer.tbank.ru/invest/mcp) [92](https://trade-api.bcs.ru/mcp/) [93](https://www.bfm.ru/news/617766) [94](https://www.finam.ru/publications/item/mcp-finama-kotorye-prevrashchayut-vashu-llm-v-lichnogo-analitika-20261025-1200/) [95](https://broker.finam.ru/landing/mcp/) [96](https://www.finam.ru/publications/item/chlen-pravleniya-finama-predstavil-finam-mcp-na-smartlab-conf-2026-20261102-1658/) [97](https://ai.finam.ru/connection-mcp) [239](https://arqatech.com/ru/products/quik/), [240](https://www.transaq.ru/), [241](https://alor.dev/docs/).

[Обзор](README.md) | [Мировые брокеры](brokers.md) | [Сервисы](research-services.md) | [Россия](russia.md) | [Терминалы](terminals.md) | [Фонды](funds.md) | [Источники](sources.md)
