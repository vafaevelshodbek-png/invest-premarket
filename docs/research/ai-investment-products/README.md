# ИИ в инвестиционных продуктах

Мировые B2C-сервисы, Россия и терминалы. Срез на 15 ноября 2026 года. **94 инициативы и 241 источник**. Несколько инициатив одного бренда могут быть отдельными кейсами. В каталог включены работающие функции, beta, пилоты, планы и отдельно обозначенные случаи, где использование LLM не подтверждено.

[Обзор](README.md) | [Брокеры](brokers.md) | [Самостоятельные сервисы](research-services.md) | [Россия](russia.md) | [Терминалы](terminals.md) | [Фонды](funds.md) | [Источники](sources.md)

## На этой странице

- [Материалы исследования](#материалы-исследования)
- [Главное](#главное)
- [Какие задачи уже решают продукты](#какие-задачи-уже-решают-продукты)
- [Как устроен каталог](#как-устроен-каталог)
- [Что показывает сравнение продуктов](#что-показывает-сравнение-продуктов)
- [Какие кейсы стоит разобрать первыми](#какие-кейсы-стоит-разобрать-первыми)
- [Что уже выпущено, а что ещё обещают](#что-уже-выпущено-а-что-ещё-обещают)
- [Границы доступности и доказательств](#границы-доступности-и-доказательств)
- [Термины простыми словами](#термины-простыми-словами)
- [Связь с проектом](#связь-с-проектом)

## Материалы исследования

| Раздел | Что представлено |
|---|---|
| [Мировые брокерские приложения](brokers.md) | 40 инициатив: встроенные помощники, внешние подключения, агентные действия и финансовое планирование |
| [Самостоятельные сервисы](research-services.md) | 18 кейсов анализа бумаг, отчётности, личного портфеля и финансовых целей |
| [Россия](russia.md) | 18 кейсов в этом разделе и отдельный [Cbonds](terminals.md#ru11) среди профессиональных систем |
| [Терминалы](terminals.md) | 8 розничных платформ и 6 профессиональных систем, включая сравнение российских терминалов |
| [Фонды](funds.md) | 4 кейса применения ИИ внутри инвестиционного процесса, включая планируемую линейку |
| [Источники](sources.md) | 241 ссылка с названием, датой публикации или обращения |
| [Сравнительный каталог CSV](catalog.csv) | Все 94 кейса, функции, модели, доступ, ограничения и ссылки |
| [Исходный PDF](archive/2026-11-15/assets/report.pdf) | Исторический экспорт до редактуры, 59 страниц. Актуальный текст исследования размещён на этих страницах |
| [Исходный интерактивный HTML](archive/2026-11-15/assets/research.html) | Исторический экспорт до редактуры с поиском и фильтрами. Обозначения и структура сохранены как в исходнике |

## Главное

Языковые модели уже встроены в инвестиционные продукты на нескольких уровнях. Они объясняют рыночные события, ищут факты в раскрытиях компаний, подбирают бумаги по запросу, анализируют портфель и помогают создавать торговые стратегии. В наиболее развитых сценариях ассистент получает доступ к инструментам брокера и может выполнять действия в пределах выданных прав. При этом функция анализа, подготовка поручения и автономное исполнение остаются разными возможностями продукта.

Содержательное различие между сервисами определяется тем, к каким данным и действиям подключён помощник. У Quartr это первичные IR-документы компаний. У Magnifi это инвестиционные счета пользователя. У WarrenAI это инструменты работы с финансовыми данными Investing.com. Composer by SoFi создаёт стратегию, которую затем исполняет обычный движок правил. Поэтому одинаковая кнопка чата может вести к совершенно разной работе.

<details>
<summary>Источники и подтверждения</summary>

- [Quartr mobile app](https://quartr.com/products/mobile-app)
- [AI Portfolio Analysis & Investing Tools](https://magnifi.com/product)
- [WarrenAI Analyst Mode: FAQ](https://www.investing-support.com/hc/en-us/articles/51200196137361-WarrenAI-Analyst-Mode-FAQ)
- [Introducing Composer by SoFi](https://investors.sofi.com/news/news-details/2026/Introducing-Composer-by-SoFi-AI-Powered-Investing-From-Idea-to-Execution/)

</details>

В 2026 году заметно расширился слой персональной аналитики. Google Finance позволяет загрузить портфель и задать исследование по расписанию. Perplexity Personal CFO объединяет финансовые счета через Plaid в режиме чтения. Yahoo Finance встраивает вопросы и объяснения непосредственно в страницы бумаг и портфеля. Это делает контекст собственных активов самостоятельным направлением развития, наряду с общим поиском по рынку. [Our latest Google Finance upgrades, including a new app](https://blog.google/products-and-platforms/products/search/google-finance-updates-june-2026/), [Computer is Now Your Personal CFO. Обновление 2026-11-12.](https://www.perplexity.ai/en-GB/hub/blog/plaid-integration-provides-full-view-of-personal-finances), [Yahoo Scout exits beta](https://unified.www.yahooinc.com/press/after-delivering-more-than-3-billion-answers-yahoo-scout-exits-beta-to-underpin-all-of-yahoo-search).

В России есть отдельные внедрения внутри брокерских продуктов, независимые помощники и подключения брокерских инструментов к внешним моделям. Эти формы разобраны отдельно ниже. Профессиональные терминалы также выделены отдельно: Bloomberg, LSEG, FactSet и S&P Capital IQ обслуживают преимущественно организации и профессионалов, их нельзя считать обычными B2C-приложениями.

Доступ зависит от страны, тарифа, версии приложения и выданных прав, beta и анонсы обозначены в карточках. Наличие функции не подтверждает точность ответа или доходность. Название и версию языковой модели многие поставщики не раскрывают.

## Какие задачи уже решают продукты

| Задача инвестора | Что делает ИИ | Что смотреть в продукте |
|---|---|---|
| Понять движение цены | Собирает новости и факторы в объяснение | Дата события, ссылки и различие между фактом и гипотезой |
| Изучить компанию | Ищет и сопоставляет отчётность, transcripts, KPI | Переход к исходному документу и точному месту |
| Найти подходящие бумаги | Переводит запрос в условия поиска и сравнение | Возможность увидеть и исправить фильтры |
| Разобраться в своём портфеле | Учитывает позиции, концентрацию, комиссии и события | Реальный источник позиций, свежесть и охват счетов |
| Проверить инвестиционную идею | Формирует сценарии и тестируемые правила | Допущения, бэктест и редактирование результата |
| Выполнить действие | Вызывает брокерские инструменты по предоставленным правам | Подтверждение поручения, разрешённые операции и ограничения |

Эта таблица служит способом сравнения кейсов. Она не означает, что каждый перечисленный ниже продукт закрывает весь путь инвестора.

В карточках разделены выпущенные функции, поэтапные запуски, beta, пилоты и планы. Дата публикации подтверждения и дата первого запуска могут различаться. Для закрытых аккаунтов доступ и качество ответов отдельно не проверялись.

## Как устроен каталог

Каждая из 94 инициатив имеет одну основную карточку. Раздел выбирается по очереди правил ниже. Функции, страна и способ доступа сравниваются внутри карточек, поэтому один продукт не учитывается повторно из-за нескольких признаков.

| Основное место | Какие инициативы сюда относятся | Число карточек |
|---|---|---|
| Профессиональные системы в разделе терминалов | Системы для организаций и специалистов, включая российский Cbonds | 6 |
| Россия | Остальные продукты российского инвестиционного рынка, включая фонд AIIQ и самостоятельные сервисы | 18 |
| Фонды | Зарубежные фонды и планируемая линейка, где ИИ участвует в инвестиционном процессе | 4 |
| Розничные терминалы | Инициативы внутри торговых и аналитических рабочих платформ, включая брокерскую платформу Questrade Pro | 8 |
| Мировые брокерские приложения | Остальные инициативы брокеров и банков для частного инвестора, включая внешние подключения к счёту | 40 |
| Самостоятельные сервисы | Исследование бумаг, сводный портфель, финансовые цели и создание стратегий вне основного интерфейса брокера | 18 |

Это правило размещения материалов, а не утверждение, что рынок состоит из непересекающихся типов компаний. Composer by SoFi остаётся в самостоятельных сервисах как отдельная среда создания стратегий. AIIQ находится в России, Cbonds в профессиональных системах. Ссылки на них из других разделов служат сравнению и не добавляют карточек. Несколько инициатив Robinhood или Public отражают разные функции одного бренда, а не разные компании.

## Что показывает сравнение продуктов

### ИИ становится способом пользоваться продуктом

Самые содержательные функции создают объект, с которым инвестор продолжает работать. TradingView меняет график и генерирует Pine Script, TrendSpider создаёт сканер и бэктест, Koyfin заполняет сравнительную матрицу. Composer формирует редактируемые правила стратегии. В этих кейсах диалог заменяет часть ручных действий с интерфейсом. Это аналитический вывод из сравнения функций, а не измеренная оценка удобства.

<details>
<summary>Источники и подтверждения</summary>

- [Getting started with AI Copilot](https://www.tradingview.com/support/solutions/43000795131-getting-started-with-ai-copilot/)
- [AI Copilot comes to TradingView](https://www.tradingview.com/blog/en/ai-copilot-now-on-tradingview-61231/)
- [New in AI Copilot: use Claude, ChatGPT, or DeepSeek](https://www.tradingview.com/blog/en/ai-copilot-claude-chatgpt-deepseek-62292/)
- [Sidekick AI Trading Assistant](https://trendspider.com/product/sidekick-ai-trading-assistant)
- [TrendSpider Sidekick AI](https://trendspider.reamaze.com/kb/sidekick/trendspider-sidekick)
- [Compare Matrix (Beta)](https://www.koyfin.com/help/release-notes/compare-matrix-beta/)
- [Attribution in Model Portfolios](https://www.koyfin.com/help/release-notes/attribution-in-model-portfolios/)
- [Introducing Composer by SoFi](https://investors.sofi.com/news/news-details/2026/Introducing-Composer-by-SoFi-AI-Powered-Investing-From-Idea-to-Execution/)
- [What is Trade with AI?](https://help.composer.trade/article/254-what-is-trade-with-ai)
- [Create with AI feature](https://help.composer.trade/article/108-create-with-ai)

</details>

### Контекст портфеля становится отдельным слоем

Вопрос «что происходит с рынком?» отличается от «что это меняет для моих позиций?». Magnifi и Perplexity подключают счета, Google Finance принимает файлы и изображения с позициями, Public Research использует данные портфеля. В России Firewire совмещает импорт отчётов и расчётные инструменты, а брокерские MCP получают позиции непосредственно из инфраструктуры брокера. Степень персонализации нужно оценивать по источнику и полноте данных, а не по обращению к пользователю по имени.

<details>
<summary>Источники и подтверждения</summary>

- [AI Portfolio Analysis & Investing Tools](https://magnifi.com/product)
- [Magnifi Pricing](https://magnifi.com/pricing)
- [Magnifi investment intelligence on linked self-directed assets](https://www.prnewswire.com/news-releases/magnifi-now-providing-ai-powered-investment-intelligence-on-over-2b-of-linked-self-directed-assets-302183080.html)
- [Computer is Now Your Personal CFO. Обновление 2026-11-12.](https://www.perplexity.ai/en-GB/hub/blog/plaid-integration-provides-full-view-of-personal-finances)
- [Perplexity Finance](https://www.perplexity.ai/finance)
- [Computer Connects to 20+ New Licensed Finance Data Sources](https://www.perplexity.ai/en-GB/hub/blog/computer-connects-to-20-new-licensed-finance-data-sources)
- [Our latest Google Finance upgrades, including a new app](https://blog.google/products-and-platforms/products/search/google-finance-updates-june-2026/)
- [Use Google Finance](https://support.google.com/websearch/answer/16490185?hl=en)
- [What is Alpha?](https://help.public.com/en/articles/9354354-what-is-alpha)
- [About Public](https://public.com/about-us)
- [Research: Public Agents](https://public.com/ai-agents/research)
- [Public MCP Server for trading on AI platforms](https://public.com/mcp-trading)
- [ИИ-Ко-пилот и автономный риск-офицер портфеля](https://help.fire-wire.ru/copilot)
- [Firewire: аналитика инвестиций и трекинг портфелей](https://fire-wire.ru/)
- [ИИ-агенты в инвестициях: собираем Telegram-ассистента и торгового робота на MCP Т-Инвестиций](https://habr.com/ru/companies/tbank/articles/1086714/)
- [Сбер внедрит ИИ-сервис для управления инвестиционным портфелем](https://www.vedomosti.ru/investments/news/2026/09/11/1228241-sber-ii-servis)
- [T-Invest MCP: официальная документация](https://developer.tbank.ru/invest/mcp)

</details>

### Генерация стратегии и решение о каждой сделке устроены по-разному

Composer by SoFi использует AI для создания стратегии, после чего действует движок утверждённых правил. ZipLime также разделяет генерацию кода, проверку на истории и исполнение. Robinhood Agents и IBKR Autonomous Trading описывают более прямой доступ агента к брокерским действиям, с выделенными средствами и условиями допуска. Эти подходы нельзя объединять в один класс «ИИ сам торгует»: различается, кто формирует решение во время исполнения и какие ограничения действуют.

<details>
<summary>Источники и подтверждения</summary>

- [Introducing Composer by SoFi](https://investors.sofi.com/news/news-details/2026/Introducing-Composer-by-SoFi-AI-Powered-Investing-From-Idea-to-Execution/)
- [What is Trade with AI?](https://help.composer.trade/article/254-what-is-trade-with-ai)
- [Create with AI feature](https://help.composer.trade/article/108-create-with-ai)
- [Финам запускает платформу ZipLime](https://www.finam.ru/publications/item/finam-zapuskaet-platformu-ziplime-s-pomoshchyu-kotoroy-algotreyderom-mozhet-stat-kazhdyy-20260831-1642/)
- [Как автоматизировать свою стратегию за 10 минут без написания кода](https://www.finam.ru/publications/item/kak-avtomatizirovat-svoyu-strategiyu-za-10-minut-bez-napisaniya-koda-20260706-0900/)
- [ZIPLIME: от идеи до сделки](https://ziplime.finam.ru/home)
- [ZIPLIME: from idea to deal](https://ziplime.limex.com/home)
- [Robinhood Agents overview](https://robinhood.com/us/en/support/articles/robinhood-agents-overview/)
- [Robinhood Agents: Build Your AI Trading Agent](https://robinhood.com/us/en/agents/)
- [Robinhood Puts the Power of Hedge Funds in Every Trader’s Pocket](https://robinhood.com/newsroom/hood-summit-2026/)
- [Trading with your agent](https://robinhood.com/us/en/support/articles/trading-with-your-agent/)
- [IBKR AI Hub](https://www.interactivebrokers.com/en/trading/ai-hub.php)
- [IBKR Integrates AI into Client Portfolios](https://www.interactivebrokers.com/en/general/about/mediaRelations/6-1-26.php)
- [Interactive Brokers Introduces Autonomous Trading](https://www.interactivebrokers.com/en/general/about/mediaRelations/10-21-26.php)
- [IBKR AI Integration and Autonomous Trading](https://www.interactivebrokers.com/en/trading/ai-integrations.php)
- [Connecting Your IBKR Account to an AI Platform](https://www.interactivebrokers.com/support/faq/content/connecting-ibkr-account-ai-platform-1437187133)

</details>

Подтверждение каждой заявки тоже не является универсальным свойством ИИ-инвестирования. У встроенных Robinhood Agents оно включено по умолчанию, но может отключаться, для внешних MCP-счетов настройки другие. У RockFlow Bobby инструкция требует повторного подтверждения операции. У T-Invest MCP это зависит от клиентского сценария и прав токена. В практическом сравнении нужно фиксировать конкретный интерфейс и режим, а не переносить правило одной функции на весь бренд.

<details>
<summary>Источники и подтверждения</summary>

- [Robinhood Agents overview](https://robinhood.com/us/en/support/articles/robinhood-agents-overview/)
- [Robinhood Agents: Build Your AI Trading Agent](https://robinhood.com/us/en/agents/)
- [Robinhood Puts the Power of Hedge Funds in Every Trader’s Pocket](https://robinhood.com/newsroom/hood-summit-2026/)
- [Trading with your agent](https://robinhood.com/us/en/support/articles/trading-with-your-agent/)
- [Guide to Bobby](https://help.rockflow.ai/docs/innvative-products/rockflow-bobby/)
- [RockFlow’s Bobby is an AI agent that trades on your worldview](https://kr-asia.com/rockflows-bobby-is-an-ai-agent-that-trades-on-your-worldview-and-its-here)
- [ИИ-агенты в инвестициях: собираем Telegram-ассистента и торгового робота на MCP Т-Инвестиций](https://habr.com/ru/companies/tbank/articles/1086714/)
- [Сбер внедрит ИИ-сервис для управления инвестиционным портфелем](https://www.vedomosti.ru/investments/news/2026/09/11/1228241-sber-ii-servis)
- [T-Invest MCP: официальная документация](https://developer.tbank.ru/invest/mcp)

</details>

### Источники данных важнее названия модели для понимания функции

Модель может быть одинаковой, а продуктовые возможности разными. Quartr ограничивает анализ первичными материалами компаний, Seeking Alpha опирается на свои исследования и рейтинги, Bloomberg добавляет переписку и файлы организации. Внешние модели через Fiscal.ai получают структурированные финансовые данные. Это объясняет различие покрытия и проверяемости, хотя само наличие ссылки ещё не гарантирует корректный вывод.

<details>
<summary>Источники и подтверждения</summary>

- [Quartr launches AI Chat for Finance on Mobile](https://quartr.com/newsroom/press-release/quartr-launches-its-ai-chat-for-finance-on-mobile-drawing-exclusively-from-first-party-ir-material)
- [Quartr mobile app](https://quartr.com/products/mobile-app)
- [What is Ask Seeking Alpha or Ask SA?](https://help.seekingalpha.com/what-is-ask-seeking-alpha-or-ask-sa)
- [Introducing the research analyst Ask Seeking Alpha](https://seekingalpha.com/article/4829617-introducing-the-cutting-edge-research-analyst-ask-seeking-alpha)
- [Ask Seeking Alpha AI: New Features For PRO Subscribers](https://seekingalpha.com/article/4846603-new-updates-to-ask-seeking-alpha)
- [Bloomberg: The Next Evolution of ASKB: Your Insights, Bloomberg’s Intelligence, One Conversation](https://webdisclosure.com/press-release/bloomberg-nasdaq-the-next-evolution-of-askb-your-insights-bloombergs-intelligence-one-conversation-eiGHbvbH0WY)
- [Conheça o ASKB](https://www.bloomberg.com.br/blog/conheca-o-askb-a-primeira-visao-do-futuro-do-bloomberg-terminal-na-era-da-ia-agentica/)
- [Bloomberg Launches AI-Powered Earnings Call Summaries](https://www.prnewswire.com/news-releases/bloomberg-launches-ai-powered-earnings-call-summaries-302040670.html)
- [Bloomberg Unveils ASKB Roadmap](https://professional.content.cirrus.bloomberg.com/professional2023/insights/press-announcement/bloomberg-unveils-askb-roadmap-for-clients-to-augment-their-investment-process-with-agentic-ai/)
- [Fiscal Terminal](https://fiscal.ai/products/terminal/)
- [Fiscal.ai Help Center](https://fiscal.ai/help/)
- [Fiscal.ai MCP / Connectors](https://docs.fiscal.ai/docs/guides/mcp-integration)
- [FinChat is now Fiscal.ai](https://fiscal.ai/blog/series-a-announcement/)

</details>

Точные модели раскрываются выборочно. У eToro Tori назван Grok 4.2, у Firewire GigaChat, TradingView и TrendSpider дают выбор моделей разных поставщиков. У Public ранняя Alpha связана с GPT-4, но из этого не следует, что все современные Agents работают только на нём. У FinGPT Финуслуг раскрыто восемь агентов, но не базовая фундаментальная модель. Название продукта, протокола MCP или голосового движка не следует принимать за название LLM.

<details>
<summary>Источники и подтверждения</summary>

- [Tori: Your AI Agent](https://www.etoro.com/trading/platforms/tori/)
- [Tori gets real-time X intelligence, powered by Grok 4.2](https://www.etoro.com/news-and-analysis/press-releases/etoros-ai-investing-companion-tori-gets-real-time-x-intelligence-powered-by-grok-4-2/)
- [Introducing the new etoro app](https://help.etoro.com/s/article/Introducing-the-new-etoro-app?language=en_GB)
- [eToro Leverages AI to Redefine Social Investing](https://www.etoro.com/en-us/news-and-analysis/latest-news/press-release/etoro-leverages-ai-to-redefine-social-investing/)
- [ИИ-Ко-пилот и автономный риск-офицер портфеля](https://help.fire-wire.ru/copilot)
- [Firewire: аналитика инвестиций и трекинг портфелей](https://fire-wire.ru/)
- [Getting started with AI Copilot](https://www.tradingview.com/support/solutions/43000795131-getting-started-with-ai-copilot/)
- [AI Copilot comes to TradingView](https://www.tradingview.com/blog/en/ai-copilot-now-on-tradingview-61231/)
- [New in AI Copilot: use Claude, ChatGPT, or DeepSeek](https://www.tradingview.com/blog/en/ai-copilot-claude-chatgpt-deepseek-62292/)
- [Sidekick AI Trading Assistant](https://trendspider.com/product/sidekick-ai-trading-assistant)
- [TrendSpider Sidekick AI](https://trendspider.reamaze.com/kb/sidekick/trendspider-sidekick)
- [What is Alpha?](https://help.public.com/en/articles/9354354-what-is-alpha)
- [About Public](https://public.com/about-us)
- [Research: Public Agents](https://public.com/ai-agents/research)
- [Public MCP Server for trading on AI platforms](https://public.com/mcp-trading)
- [FinGPT: личный финансовый AI-ассистент](https://finuslugi.ru/landing/fingpt)
- [Ученики Летово предложили AI-решения для развития сервисов Московской биржи](https://finuslugi.ru/presscenter/pressrelease/letovoii)
- [Финансовый помощник FinGPT: зачем инвестору нейросеть](https://finuslugi.ru/navigator/investirovat/stat_finansovyj_pomoshchnik_fingpt_revolyuciya_v_investiciyakh_zachem_investoru_nejroset)

</details>

### В России представлены несколько форм внедрения

Есть встроенная консультация в приложении, внешнее подключение брокерских инструментов, самостоятельный анализ сводного портфеля и создание торговой стратегии. Планы Сбера добавляют ещё одну инициативу агентного доступа. При этом ВТБ «Интеллект» и «Индекс AI» Альфа-Инвестиций относятся к реальным инвестиционным AI-сценариям, но их опубликованные описания не устанавливают использование языковой модели. Это различие сохраняет смысл вопроса о LLM, не исключая другие формы ИИ из картины рынка.

<details>
<summary>Источники и подтверждения</summary>

- [Вселенная AI-ассистентов Т-Банка](https://ai.tbank.ru/assistants/)
- [Тинькофф Инвестиции запустили инвестиционного ассистента на основе искусственного интеллекта](https://www.cnews.ru/news/line/2023-12-22_tinkoff_investitsii_zapustili)
- [Т-Инвестиции: официальный пост об AI Инвест-ассистенте](https://t.me/s/tb_invest_official/10541)
- [Два проекта БКС стали лучшими на GlobalCIO](https://habr.com/ru/companies/bcs_company/articles/992684/)
- [Помощник Финс от БКС: ваш персональный гид в мире финансов](https://globalcio.ru/projects/53411/)
- [БКС Мир инвестиций: голосовой ИИ-ассистент Финс](https://platforms.su/project/2467)
- [ИИ-агенты в инвестициях: собираем Telegram-ассистента и торгового робота на MCP Т-Инвестиций](https://habr.com/ru/companies/tbank/articles/1086714/)
- [Сбер внедрит ИИ-сервис для управления инвестиционным портфелем](https://www.vedomosti.ru/investments/news/2026/09/11/1228241-sber-ii-servis)
- [T-Invest MCP: официальная документация](https://developer.tbank.ru/invest/mcp)
- [ИИ-Ко-пилот и автономный риск-офицер портфеля](https://help.fire-wire.ru/copilot)
- [Firewire: аналитика инвестиций и трекинг портфелей](https://fire-wire.ru/)
- [Финам запускает платформу ZipLime](https://www.finam.ru/publications/item/finam-zapuskaet-platformu-ziplime-s-pomoshchyu-kotoroy-algotreyderom-mozhet-stat-kazhdyy-20260831-1642/)
- [Как автоматизировать свою стратегию за 10 минут без написания кода](https://www.finam.ru/publications/item/kak-avtomatizirovat-svoyu-strategiyu-za-10-minut-bez-napisaniya-koda-20260706-0900/)
- [ZIPLIME: от идеи до сделки](https://ziplime.finam.ru/home)
- [ZIPLIME: from idea to deal](https://ziplime.limex.com/home)
- [К брокерскому счету в СберИнвестициях можно будет подключить внешних ИИ-агентов](https://axenix.cnews.ru/news/line/2026-10-08_k_brokerskomu_schetu_v_sberinvestitsiyah)
- [ВТБ: Интеллект](https://www.vtb.ru/personal/investicii/intellect/)
- [Брокер ВТБ запустил сервис для инвестиций на основе ИИ](https://www.vedomosti.ru/kapital/investments/news/2025/12/15/1163421-investitsii-na-osnove)
- [AI в личных финансах и инвестициях: Альфа Инвестор](https://alfabank.ru/alfa-investor/t/ai-v-lichnyh-finansah-i-investitsiyah/)

</details>

### Языковая модель может сопровождать уже существующий инвестиционный движок

У PortfolioPilot чат вызывает портфельные расчёты, сравнение фондов и сценарии, но не получает полномочий торговать. Mezzi использует контекст нескольких счетов для налоговых и портфельных вопросов. Origin связывает инвестиции с пенсией, денежными потоками и целями. Здесь продуктовая ценность состоит в постановке вопроса и объяснении расчётного результата, языковая модель не обязана заменять количественную модель распределения активов.

<details>
<summary>Источники и подтверждения</summary>

- [PortfolioPilot Tutorial: AI Assistant](https://portfoliopilot.com/help/tutorials/tutorial-ai-assistant)
- [How PortfolioPilot AI works](https://portfoliopilot.com/technology)
- [PortfolioPilot product and plan FAQ](https://portfoliopilot.com/)
- [What Mezzi Does and What It Doesn't](https://support.mezzi.com/articles/4231112703-what-mezzi-does-and-what-it-doesn-t)
- [Mezzi Pricing & Plans](https://www.mezzi.com/pricing)
- [Mezzi product updates and releases. Последнее обновление 2026-11-06.](https://www.mezzi.com/whats-new)
- [Valerie Baldinger. Generative AI and Retail Investment](https://valeriebaldinger.github.io/files/generative_ai_and_retail_investment.pdf)
- [Origin: Introducing AI Advisor](https://support.useorigin.com/hc/en-us/articles/39417344659341-Introducing-AI-Advisor-Your-Personal-Financial-Guide)
- [What LLMs does AI Advisor use?](https://support.useorigin.com/hc/en-us/articles/39417044720397-What-LLM-s-does-AI-Advisor-use)
- [Origin AI Advisor Disclaimers and Limitations](https://support.useorigin.com/hc/en-us/articles/20957761151757-AI-Advisor-Disclaimers-and-Limitations)

</details>

У Mezzi есть дополнительное свидетельство фактического использования: рабочая статья Валери Балдингер от 8 ноября 2026 связывает диалоги инвесторов с данными об их последующих операциях. Это позволяет отличать наличие описанной функции от реального поведения пользователей. Работа относится к конкретной платформе и выборке, автор раскрывает сотрудничество с компанией, а результаты не устанавливают качество всех AI-продуктов. [Valerie Baldinger. Generative AI and Retail Investment](https://valeriebaldinger.github.io/files/generative_ai_and_retail_investment.pdf).

### ИИ может работать внутри фонда без клиентского чата

Intelligent Alpha Atlas ETF использует LLM в процессе формирования портфеля. Defiance AIED добавил LLM-сигнал новостных катализаторов к количественной momentum-стратегии в октябре 2026. Evolve ARTI применяет технологию Boosted.ai для ранжирования компаний, связанных с развитием ИИ. Российский AIIQ использует систему агентов, но не раскрывает точный LLM-стек. В каждом случае роль человека и модели описана отдельно.

<details>
<summary>Источники и подтверждения</summary>

- [Intelligent Alpha Atlas ETF: Summary Prospectus](https://www.sec.gov/Archives/edgar/data/1592900/000159290026004964/intelligentalphaatlasetf.htm)
- [Intelligent Alpha Atlas ETF: Annual Shareholder Report and Financial Statements](https://www.sec.gov/Archives/edgar/data/1592900/000159290026004195/ck0001592900-20260630.htm)
- [Intelligent Alpha and first ETF launch](https://etfarchitect.com/wp-content/uploads/compliance/etf/press_release/LIVR_Launch.pdf)
- [Defiance LLM Catalyst Momentum ETF: Prospectus](https://www.sec.gov/Archives/edgar/data/1547950/000121390026110382/ea0308745-01_497.htm)
- [Defiance LLM Catalyst Momentum ETF](https://www.defianceetfs.com/aied/)
- [Evolve Artificial Intelligence Fund Begins Trading Today on TSX](https://evolveetfs.com/2024/03/evolve-artificial-intelligence-fund-begins-trading-today-on-tsx/)
- [Evolve Artificial Intelligence Fund: May 29, 2026 factsheet](https://evolveetfs.com/wp-content/uploads/2026/05/ARTI-overview_APR_30_2026-EN.pdf)
- [Московская биржа: о начале торгов ценными бумагами 7 октября 2026 года](https://www.moex.com/n104889)
- [УК Первая: как устроен фонд Искусственный интеллект](https://t.me/am_first/2001)
- [Коммерсантъ: управляющая компания Первая запустила фонд под управлением ИИ](https://www.kommersant.ru/doc/9008884)

</details>

Поэтому «фонд инвестирует в сектор AI» и «фонд использует LLM в управлении» являются разными характеристиками. ARTI совмещает обе, само наличие AI в названии другого фонда этого не доказывает. Исторические показатели стратегии до добавления LLM также не характеризуют эффективность нового компонента.

<details>
<summary>Источники и подтверждения</summary>

- [Evolve Artificial Intelligence Fund Begins Trading Today on TSX](https://evolveetfs.com/2024/03/evolve-artificial-intelligence-fund-begins-trading-today-on-tsx/)
- [Evolve Artificial Intelligence Fund: May 29, 2026 factsheet](https://evolveetfs.com/wp-content/uploads/2026/05/ARTI-overview_APR_30_2026-EN.pdf)
- [Defiance LLM Catalyst Momentum ETF: Prospectus](https://www.sec.gov/Archives/edgar/data/1547950/000121390026110382/ea0308745-01_497.htm)
- [Defiance LLM Catalyst Momentum ETF](https://www.defianceetfs.com/aied/)

</details>

## Какие кейсы стоит разобрать первыми

Для предметного знакомства с продуктами полезно выбрать разные сценарии. Это подборка для изучения функций, доступность аккаунта и качество результата оцениваются отдельно.

| Что хочется понять | Основной кейс | С чем сравнить |
|---|---|---|
| Универсальный помощник внутри брокера | Robinhood Cortex и Agents | Webull Vega, eToro Tori, Groww GR-1 |
| Анализ первичных документов | Quartr mobile | Seeking Alpha, Koyfin Compare Matrix |
| Персональная работа со счетами | PortfolioPilot и Mezzi | Magnifi, Perplexity Personal CFO, Firewire |
| Стратегия из словесной идеи | Composer by SoFi | ZipLime, Futubull AI Algo Trading |
| Работа ИИ в графическом терминале | TradingView AI Copilot | TrendSpider Sidekick, MetaTrader 5 |
| Профессиональная исследовательская среда | Bloomberg ASKB | LSEG Deep Research, Capital IQ ChatIQ, AlphaSense |
| Российский встроенный ассистент | Т-Инвестиции | БКС Финс, FinGPT Финуслуг |
| Сводный портфель российского инвестора | Snowball Income | Firewire, HADL, Bonds-Lab для облигаций |
| Внешний агент с данными российского брокера | T-Invest MCP | БКС Trade API MCP, Finam MCP |
| Массовый китайский инвестиционный интерфейс | Ant Fortune Maxiaocai | East Money Miaoxiang |
| LLM внутри инвестиционных решений фонда | Intelligent Alpha Atlas ETF | Defiance AIED, Evolve ARTI, AIIQ в России с нераскрытым LLM-стеком |

Подробные функции, источники и условия каждого кейса приведены в карточках соответствующего раздела. Эта подборка не ранжирует продукты по доходности, точности или коммерческому успеху.

## Что уже выпущено, а что ещё обещают

У одной компании могут одновременно работать базовый помощник и тестироваться более сложные действия. Поэтому статус имеет смысл указывать для функции, а не только для бренда. Например, обычная аналитика портфеля Сбера сама по себе не подтверждает выпуск обещанного Invest AI, существование Bloomberg ASKB не означает автоматическую поставку всей его roadmap.

| Инициатива | Уже есть на дату среза | Beta, пилот или план |
|---|---|---|
| Robinhood Agents | Поэтапный доступ к агенту и торговым инструментам | Agent Loops для непрерывной работы и расписаний обозначены как будущие функции |
| Interactive Brokers | Ask IBKR и подключения внешних моделей | Autonomous Trading документирован с отдельным допуском, сведения о географии противоречивы |
| Schwab | Portfolio Insights, раскатка Charley | MCP для выбранных клиентов, thinkorswim Assistant ожидается |
| Public Generated Assets | Генерация инвестируемых корзин акций | Расширение на криптоактивы и облигации заявлено как будущее |
| Финам MCP | Чтение, аналитические инструменты и графики | Торговля тестируется, часть интерактивных приложений планируется |
| СберИнвестиции | Общий запуск перечисленных функций не подтверждён | Invest AI до конца 2026, внешние агенты поэтапно с 2027 |
| Koyfin | Работают функции платформы и отдельный AI Summary для консультантов | Compare Matrix имеет beta-статус |
| Capital IQ Pro | Работают ChatIQ и многоисточниковый анализ | Presentations в Labs, Portfolio Insights в beta |
| QuantWheel | Аналитический чат и MCP | Некоторые торговые агенты обозначены как будущие функции, права исполнения зависят от интерфейса |
| Wealthsimple | Ноябрьская презентация Penny и список ожидания | Помощник и внешние AI-подключения ожидаются в начале 2027 |
| Intelligent Alpha | Действующий Atlas ETF | Другие четыре описанные стратегии по документам 31 октября ещё не начали операции |

Статусы в таблице опираются на справки и релизы соответствующих функций.

<details>
<summary>Источники и подтверждения</summary>

- [Robinhood Agents overview](https://robinhood.com/us/en/support/articles/robinhood-agents-overview/)
- [Robinhood Agents: Build Your AI Trading Agent](https://robinhood.com/us/en/agents/)
- [Robinhood Puts the Power of Hedge Funds in Every Trader’s Pocket](https://robinhood.com/newsroom/hood-summit-2026/)
- [Trading with your agent](https://robinhood.com/us/en/support/articles/trading-with-your-agent/)
- [IBKR AI Hub](https://www.interactivebrokers.com/en/trading/ai-hub.php)
- [IBKR Integrates AI into Client Portfolios](https://www.interactivebrokers.com/en/general/about/mediaRelations/6-1-26.php)
- [Interactive Brokers Introduces Autonomous Trading](https://www.interactivebrokers.com/en/general/about/mediaRelations/10-21-26.php)
- [IBKR AI Integration and Autonomous Trading](https://www.interactivebrokers.com/en/trading/ai-integrations.php)
- [Connecting Your IBKR Account to an AI Platform](https://www.interactivebrokers.com/support/faq/content/connecting-ibkr-account-ai-platform-1437187133)
- [Schwab Launches AI-Powered Portfolio Insights](https://pressroom.aboutschwab.com/press-releases/press-release/2026/Charles-Schwab-Launches-AI-Powered-Capability-That-Helps-Investors-Understand-Portfolio-Performance-and-Market-Activity/default.aspx)
- [Meet Charley](https://pressroom.aboutschwab.com/press-releases/press-release/2026/Meet-Charley-Schwabs-New-AI-Powered-Assistant-Designed-to-Help-Clients-Get-Answers-and-Take-Action/default.aspx)
- [Schwab Announces MCP Server and thinkorswim Assistant](https://pressroom.aboutschwab.com/press-releases/press-release/2026/Schwab-Announces-Platform-Enhancements-Including-MCP-Server-to-Connect-Clients-AI-Platforms-With-Their-Schwab-Accounts/default.aspx)
- [Generated Assets](https://public.com/generated-asset)
- [MCP Финама, которые превращают вашу LLM в личного аналитика](https://www.finam.ru/publications/item/mcp-finama-kotorye-prevrashchayut-vashu-llm-v-lichnogo-analitika-20261025-1200/)
- [Finam MCP: данные счёта для ИИ-агента](https://broker.finam.ru/landing/mcp/)
- [Член правления Финама представил Finam MCP на SmartLab CONF 2026](https://www.finam.ru/publications/item/chlen-pravleniya-finama-predstavil-finam-mcp-na-smartlab-conf-2026-20261102-1658/)
- [Подключение MCP AI-скринера Финама](https://ai.finam.ru/connection-mcp)
- [Сбер внедрит ИИ-сервис для управления инвестиционным портфелем](https://www.vedomosti.ru/investments/news/2026/09/11/1228241-sber-ii-servis)
- [К брокерскому счету в СберИнвестициях можно будет подключить внешних ИИ-агентов](https://axenix.cnews.ru/news/line/2026-10-08_k_brokerskomu_schetu_v_sberinvestitsiyah)
- [Compare Matrix (Beta)](https://www.koyfin.com/help/release-notes/compare-matrix-beta/)
- [Attribution in Model Portfolios](https://www.koyfin.com/help/release-notes/attribution-in-model-portfolios/)
- [S&P Global Redefines Financial Insights with Multi-Document Research in ChatIQ](https://press.spglobal.com/2025-10-22-S-P-Global-Redefines-Financial-Insights-with-New-AI-Powered-Multi-Document-Research-and-Analysis-Tool-in-Capital-IQ-Pro-ChatIQ)
- [ChatIQ Leads S&P Global’s Latest Capital IQ Pro Update](https://press.spglobal.com/2026-10-06-ChatIQ-Leads-S-P-Globals-Latest-Capital-IQ-Pro-Update-with-Expanded-AI-Powered-Research-Capabilities)
- [How to use QW Intelligence](https://quantwheel.com/how-to/qw-intelligence-overview)
- [Options Trading MCP for Claude and ChatGPT](https://quantwheel.com/mcp)
- [Agentic Options Trading Platform](https://quantwheel.com/)
- [Wealthsimple announces AI assistant Penny](https://newsroom.wealthsimple.com/wealthsimple-announces-ai-assistant-penny-and-11-more-releases-at-wealthsimple-presents-something-good-is-going-to-happen)
- [Wealthsimple Presents: Something Good Just Happened](https://www.wealthsimple.com/en-ca/presents/something-good)
- [Wealthsimple financial assistant waitlist FAQ](https://www.wealthsimple.com/en-ca/financial-assistant-notify-me)
- [Intelligent Alpha ETFs: Prospectus and SAI effective October 31, 2026](https://www.sec.gov/Archives/edgar/data/1592900/000159290026004781/ck0001592900-20261023.htm)

</details>

## Границы доступности и доказательств

Обзор содержит внедрения, технические интеграции, пилоты, планы и несколько пограничных примеров. Число карточек не равно числу независимых компаний или количеству доказанных LLM-внедрений. Несколько функций одного брокера могут использовать общий слой данных, но иметь разные права и интерфейс.

Неизвестные модель, дата и тариф отмечены явно. Для ряда функций описание ограничивается заявлением поставщика. Наличие справки, релиза или свежего приложения не устанавливает фактическую надёжность, долю активных пользователей, экономический эффект или дополнительную доходность. В частности, бэктест, маркетинговая статистика и популярность продукта отвечают на другие вопросы, чем качество инвестиционного решения.

География компании, покрытие рынка и доступность клиенту из России различаются. Российская локализация зарубежного сервиса не делает его российским продуктом, существование функции за рубежом не подтверждает её доступность конкретному российскому аккаунту. У профессиональных терминалов права на источники и модули сохраняются и при работе через ИИ.

## Термины простыми словами

| Термин | Что означает в этом исследовании |
|---|---|
| ИИ, AI | Искусственный интеллект. Общий термин сам по себе не подтверждает использование языковой модели |
| LLM, GenAI | Большая языковая модель и генеративный ИИ: создают текст, объяснения, код и другие результаты по запросу |
| Агент | Помощник, который использует подключённые инструменты и может выполнять несколько шагов. Права на торговлю проверяются отдельно |
| MCP | Протокол подключения ассистента к данным и инструментам. Это способ доступа, а не модель и не самостоятельное разрешение на сделки |
| API, SDK, CLI, Skills | Программный интерфейс, набор инструментов разработчика, командная строка и готовые инструкции для агента |
| B2C, retail | Продукты для частного пользователя. Профессиональные системы выделены отдельно |
| Beta, rollout, GA, roadmap | Тестовая версия, поэтапное внедрение, общий выпуск и план развития. План не подтверждает доступность функции |
| RAG, grounding | Поиск в подключённых материалах и привязка ответа к данным. Наличие ссылки не гарантирует правильность вывода |
| IR, transcripts, KPI | Материалы компании для инвесторов, расшифровки встреч и звонков, ключевые показатели |
| Скрининг, сканер | Поиск бумаг по заданным условиям. Условия могут быть сформированы из обычной фразы |
| Бэктест, momentum | Проверка правил стратегии на истории и стратегия, учитывающая направление движения цен |
| ETF, ISIN, тикер | Биржевой фонд, международный идентификатор бумаги и её короткое биржевое обозначение. Буквы в названии фонда являются тикером, а не кодом карточки |
| CFD, опционы | Контракты на разницу цен и инструменты с правом купить или продать актив по условиям контракта |
| IRA, ISA, SIPP | Особые типы инвестиционных и пенсионных счетов в США и Великобритании. Условия зависят от юрисдикции |
| HHI, TWR, XIRR | Показатель концентрации и способы расчёта доходности: с учётом времени или денежных потоков |
| Due diligence, workflow | Комплексная проверка и последовательность рабочих действий |
| Personal CFO | Помощник по личным финансам. Название не устанавливает полномочий финансового консультанта |
| GCC, ОАЭ | Совет сотрудничества арабских государств Персидского залива и Объединённые Арабские Эмираты |
| US, UK, CAD | США, Великобритания и канадский доллар. Страна компании не означает доступность сервиса во всех странах |

## Связь с проектом

Исследование дополняет [разбор текущих способов и аналогов](../investment-processes/current-methods-summary.md). Оно используется в [формировании новых вариантов](https://github.com/vafaevelshodbek-png/invest-premarket/issues/18), [сравнении вклада AI](https://github.com/vafaevelshodbek-png/invest-premarket/issues/22), [проверке данных](https://github.com/vafaevelshodbek-png/invest-premarket/issues/19) и [выборе команды](https://github.com/vafaevelshodbek-png/invest-premarket/issues/2). Пользовательский контекст раскрыт в [CJM частного инвестора](../investment-processes/retail-investors-summary.md), технические права и ограничения в [исследовании API/MCP](../invest-api/README.md).

Каталог описывает существующие продукты, а не предлагает 94 идеи для команды. Он не подтверждает пользовательский спрос, преимущество AI, доходность или доступ конкретного аккаунта. [Публикация исследования](https://github.com/vafaevelshodbek-png/invest-premarket/pull/62).

[Каталог исследований](../README.md) | [Задача о текущих способах и аналогах](https://github.com/vafaevelshodbek-png/invest-premarket/issues/32) | [Исследования в Wiki](https://github.com/vafaevelshodbek-png/invest-premarket/wiki/Research)
