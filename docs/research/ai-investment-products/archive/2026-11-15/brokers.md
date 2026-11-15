# ИИ в мировых брокерских приложениях

Срез на 15 ноября 2026 года.

[Обзор](README.md) | [Мировые брокеры](brokers.md) | [Сервисы](research-services.md) | [Россия](russia.md) | [Терминалы](terminals.md) | [Фонды](funds.md) | [Источники](sources.md)

## Мировые брокерские приложения

Встроенный помощник знает контекст приложения, а внешняя интеграция передаёт выбранному пользователем ИИ-клиенту данные и разрешённые инструменты. У одного брокера могут одновременно существовать оба варианта. Ниже разные инициативы Robinhood и Public разделены по функции, это не отдельные компании.

| Продукт | Что делает | Текущий статус |
|---|---|---|
| [Robinhood Cortex и Digests](#gb01) | Понять движение бумаг/портфеля и подготовить действие | Доступно, Portfolio Digests поэтапно |
| [Robinhood Agents и Agent Apps](#gb02) | Исследовать и торговать через персонального агента | Поэтапный запуск, Agent Loops пока coming soon |
| [Webull Vega и Vega Analyst](#gb03) | Разобрать рынок, опционные данные, портфель и компанию | Доступно, отдельные новые возможности раскатываются |
| [Public Alpha и Research в Agents](#gb04) | Ответить на вопросы о бумагах и собственных позициях, проверить сценарий перед сделкой | Доступно, Alpha описана в старой FAQ, новый акцент на Agents |
| [Public Generated Assets](#gb05) | Превратить инвестиционную гипотезу в собственный индекс | Доступно, crypto/bonds expansion coming soon |
| [eToro Tori](#gb06) | Контекст портфеля, рыночные события и Agent Portfolio в диалоге | Доступно, новый app поэтапно |
| [Moomoo AI и API Skills](#gb07) | Собрать данные рынка, новости/отчётность и вопросы по акциям | Доступно, локальные варианты |
| [Futubull AI Expert Mode и AI Algo Trading](#gb08) | Полный путь исследования, стратегии и исполнения | Запуск подтверждён компанией |
| [TigerAI, ранее TigerGPT](#gb09) | Разобрать акцию, новость, портфель и вопрос об опционах | Доступно, имена TigerGPT/TigerAI сосуществуют в источниках |
| [Interactive Brokers: Ask IBKR, AI Integration, Autonomous Trading](#gb10) | Проанализировать позиции и подготовить или исполнить действие по счёту | Ask IBKR и AI Integration доступны, Autonomous Trading объявлен и документирован с ограничениями |
| [RockFlow Bobby](#gb11) | Исследование и стратегии с исполнением из чата | Доступен по действующей инструкции |
| [Charles Schwab: Portfolio Insights, Charley, MCP](#gb12) | Объяснить изменение портфеля, получить информацию и перейти к действию через диалог | Insights доступно, Charley rollout, MCP ограниченный пилот |
| [SaxoInvestor AI Assistant](#gb13) | Вопросы по портфелю, инструментам и подготовка заявки | Доступен только в новом SaxoInvestor |
| [Groww GR-1 и Groww MCP](#gb14) | Понять движение акций, оценку фондов и собственный портфель | GR-1 встроен и доступен, расширяется покрытие |
| [Zerodha Kite MCP](#gb15) | Проанализировать портфель, позиции и рынок в выбранном ИИ-ассистенте | Доступная техническая интеграция |
| [SoFi Coach](#gb16) | Связать инвестиции с денежными потоками, долгами и финансовыми целями | Доступен всем клиентам по текущей странице |
| [Ant Fortune / Alipay Maxiaocai](#gb17) | Объяснить рынок и отчётность, следить за собственными инвестициями | Работает, обновление приложения 13 ноября 2026 |
| [East Money Miaoxiang](#gb18) | Разобрать акцию, новости и рынок, найти инструменты под запрос | Работает внутри East Money и как самостоятельное приложение |
| [SBI Securities Plus: AI Market Summary](#asa01) | Быстро понять итоги рынка Японии и США, предстоящие события и отчётность | Доступен в SBI Securities Plus по действующей инструкции |
| [Rakuten Securities Investment AI Assistant beta plus](#asa02) | Разобраться в инвестиционных терминах, вопросах начала инвестирования и найти подходящие материалы | Открытая beta с дневным лимитом |
| [Dhan MCP и Dhan Skills](#asa03) | Обсудить рынок и позиции, проверить маржу и выполнить разрешённые действия, построить торговую автоматизацию | Официальные MCP и Skills доступны |
| [Upstox MCP и Agent Skills](#asa04) | Разобрать позиции и рынок через чат или построить и выполнить торговый процесс в coding agent | MCP и Agent Skills доступны, с разными правами |
| [INDmoney MCP](#asa05) | Объединить разные классы активов и объяснить портфель, регулярные инвестиции и рыночные данные | Официальное подключение доступно |
| [DBS digiWealth: GenAI digibot](#asa06) | Получить ответы на вопросы об инвестициях, капитале и страховании, перейти к человеку-консультанту | Инвестиционная информационная функция доступна по текущей справке |
| [Lightyear AI](#gba01) | Быстро понять события вокруг акции и аргументы сторон. | Три аналитические функции доступны, персональные рекомендации и автономное управление описаны как будущие направления |
| [Revolut AIR: инвестиционные вопросы](#gba02) | Спросить о своих инвестициях и причинах изменения стоимости. | Доступен части клиентов, поэтапное внедрение |
| [Trading 212: AI Analysis, AI Chat, AI Search и Agent Skills](#gba03) | Исследовать бумагу и собственный портфель, искать инструменты обычной фразой, отдельный технический канал позволяет агенту работать с API. | Анализ и чат доступны, AI Search внедряется постепенно, API для внешних агентов находится в бета-версии |
| [Scalable: Insights и Agentic Investing](#gba04) | Обсудить инвестиции и работать с брокерским счётом из выбранного AI-ассистента. | Insights работает, Agentic Investing запущен, конкретные действия зависят от платформы агента |
| [Vanguard Digital Advisor: AI Chat](#gba05) | Объяснение персонального финансового плана и проверка сценариев в Digital Advisor. | Бета-версия с ограниченным доступом |
| [Betterment Account Recommender](#gba06) | Помочь выбрать подходящий тип финансового счёта и понять основание рекомендации. | Запущен |
| [FirstradeGPT](#gba08) | Проводить фундаментальное исследование компаний внутри брокерского приложения. | Доступен клиентам |
| [Nordnet: Latest Recap и AI-сводки отчётности](#gba09) | Читать краткие новости по собственным позициям и результаты компаний. | Работают в Швеции, по данным отчёта Q1 2026 внедрение отчётных сводок на остальных североевропейских рынках продолжалось |
| [Avanza: AI-сводки квартальных отчётов](#gba10) | Быстро понять финансовые результаты компании на странице акции. | Работают |
| [XTB: аналитический AI-чат в xStation](#gba11) | Обсудить инструменты, текущий портфель и распределение активов внутри брокерского интерфейса. | Доступен в Чили, европейское внедрение по использованным первичным источникам не установлено |
| [Mirae Asset Securities MAPS: AI-сводки и генеративная аналитика](#asb02) | Быстрое чтение рынка, новостей компаний и аналитики в брокерском приложении | Текущие AI-сервисы перечислены в официальной карточке MAPS, обновлённой 16.10.2026, генеративные отчёты отдельно подтверждены релизом 07.05.2024 |
| [baraka AI](#asb03) | Исследование акций, объяснение движений рынка и финансовых тенденций | Текущая исследовательская AI-функция на официальном сайте и в описании приложения, LLM-архитектура публично не подтверждена |
| [Itaú Investment Intelligence / Inteligência de Investimentos Itaú](#asb04) | Персонализированные инвестиционные вопросы, рекомендации и ограниченные операции в чате | Запущен 05.06.2025 с постепенным расширением, официальный материал, обновлённый 14.05.2026, сообщает примерно 60 тыс. клиентов |
| [CMC Markets: подключение счёта к ChatGPT](#gbb03) | Обсуждать свой CFD-счёт, позиции и рынок в ChatGPT. | Запущено для британских CFD-счетов |
| [ThinkMarkets ChelseaAI в ThinkTrader](#gbb04) | Управлять торговыми действиями в разговоре с AI вместо меню терминала. | По справке доступен на demo и live ThinkTrader, на продуктовой странице также сохранён лист ожидания для доступности на выбранной платформе |
| [Wealthsimple / Penny и AI integrations](#rwb02) | Связать финансовую цель с регулярными инвестициями и подтверждаемыми торговыми действиями | Анонс и список ожидания, запуск планируется в начале 2027 |

<a name="gb01"></a>

### Robinhood Cortex и Digests

**Кому и зачем.** США. Понять движение бумаг/портфеля и подготовить действие.

**Что внедрено.** Диалог о портфеле, исследование бумаг, скрининг, подготовка заявки, сводки по активам и портфелю. [1](https://robinhood.com/us/en/support/articles/cortex/) [2](https://robinhood.com/us/en/support/articles/cortex-digests/) [3](https://robinhood.com/us/en/careers/blog/loop-stays-dumb-so-the-model-can-be-smart/)

**Статус и доступ.** Доступно, Portfolio Digests поэтапно. Подписка Gold: $5 в месяц. Приложение Robinhood. Портфельные сводки не охватывают IRA. Первый запуск или важный этап: Cortex Assistant: начало 2026, точная дата неизвестна. [1](https://robinhood.com/us/en/support/articles/cortex/) [2](https://robinhood.com/us/en/support/articles/cortex-digests/) [3](https://robinhood.com/us/en/careers/blog/loop-stays-dumb-so-the-model-can-be-smart/)

**Технология и границы.** Генеративный диалоговый AI. Название и версия модели в пользовательской справке не раскрыты. Cortex не использует открытый веб-поиск и обсуждения X/Reddit. Подготовленную заявку отправляет пользователь. Портфельные сводки вводятся постепенно. [1](https://robinhood.com/us/en/support/articles/cortex/) [2](https://robinhood.com/us/en/support/articles/cortex-digests/) [3](https://robinhood.com/us/en/careers/blog/loop-stays-dumb-so-the-model-can-be-smart/)


<a name="gb02"></a>

### Robinhood Agents и Agent Apps

**Кому и зачем.** США. Исследовать и торговать через персонального агента.

**Что внедрено.** Агент внутри приложения, память, готовые навыки, графики и таблицы, списки наблюдения и торговые заявки. Отдельный счёт с выделенными средствами. [4](https://robinhood.com/us/en/support/articles/robinhood-agents-overview/) [5](https://robinhood.com/us/en/agents/) [6](https://robinhood.com/newsroom/hood-summit-2026/) [7](https://robinhood.com/us/en/support/articles/trading-with-your-agent/)

**Статус и доступ.** Поэтапный запуск, Agent Loops пока coming soon. Полная версия только в мобильном приложении. Доступ получают постепенно. Диалоги оплачиваются токенами, дополнительные источники данных имеют отдельные подписки. Первый запуск или важный этап: Анонс 29 сентября 2026, поэтапный запуск с конца сентября. [4](https://robinhood.com/us/en/support/articles/robinhood-agents-overview/) [5](https://robinhood.com/us/en/agents/) [6](https://robinhood.com/newsroom/hood-summit-2026/) [7](https://robinhood.com/us/en/support/articles/trading-with-your-agent/)

**Технология и границы.** LLM-агент с инструментами. Выбор сторонних LLM, модели меняются. У встроенных Robinhood Agents подтверждение сделок включено по умолчанию, у внешних MCP-счетов выключено. Настройка меняется, некоторые сделки всё равно требуют согласия. Агент торгует выделенным счётом. Loops по расписанию пока анонсированы. [4](https://robinhood.com/us/en/support/articles/robinhood-agents-overview/) [5](https://robinhood.com/us/en/agents/) [6](https://robinhood.com/newsroom/hood-summit-2026/) [7](https://robinhood.com/us/en/support/articles/trading-with-your-agent/)


<a name="gb03"></a>

### Webull Vega и Vega Analyst

**Кому и зачем.** США, региональные условия различаются. Разобрать рынок, опционные данные, портфель и компанию.

**Что внедрено.** Сводки рынка и списка наблюдения, разбор портфеля и опционной активности, исследовательские отчёты с источниками, подготовка заявки из обычной речи. [8](https://www.webull.com/vega) [9](https://www.webull.com/blog/251-Inside-Webull-s-AI-ToolkitEvery-AI-Feature-You-Can-Actually-Use-Right-Now) [10](https://www.webull.com/ai-features) [11](https://www.webull.com.sg/policy?code=TERMS_OF_SERVICE&hl=en) [12](https://www.sec.gov/Archives/edgar/data/1866364/000121390025113140/ea026489601ex99-1_webull.htm)

**Статус и доступ.** Доступно, отдельные новые возможности раскатываются. Основной Vega бесплатен для американских клиентов по публикации от 20 августа 2026 года. Vega Analyst использует платные кредиты, часть отчётов бесплатна. Первый запуск или важный этап: Vega: конец 2025, Analyst: май 2026. [8](https://www.webull.com/vega) [9](https://www.webull.com/blog/251-Inside-Webull-s-AI-ToolkitEvery-AI-Feature-You-Can-Actually-Use-Right-Now) [10](https://www.webull.com/ai-features) [11](https://www.webull.com.sg/policy?code=TERMS_OF_SERVICE&hl=en) [12](https://www.sec.gov/Archives/edgar/data/1866364/000121390025113140/ea026489601ex99-1_webull.htm)

**Технология и границы.** Генеративный AI/LLM плюс количественные модули. Конкретная модель неизвестна. Доступ и тарифы различаются по регионам и модулям. При подготовке заявки пользователь проверяет условия перед отправкой. Рекламное описание автоматизации не подтверждает автономность каждой функции. [8](https://www.webull.com/vega) [9](https://www.webull.com/blog/251-Inside-Webull-s-AI-ToolkitEvery-AI-Feature-You-Can-Actually-Use-Right-Now) [10](https://www.webull.com/ai-features) [11](https://www.webull.com.sg/policy?code=TERMS_OF_SERVICE&hl=en) [12](https://www.sec.gov/Archives/edgar/data/1866364/000121390025113140/ea026489601ex99-1_webull.htm)


<a name="gb04"></a>

### Public Alpha и Research в Agents

**Кому и зачем.** США. Ответить на вопросы о бумагах и собственных позициях, проверить сценарий перед сделкой.

**Что внедрено.** Вопросы по отчётности, звонкам компаний и рынку, анализ собственных позиций и концентрации, сравнение компаний и разбор будущей сделки. [13](https://help.public.com/en/articles/9354354-what-is-alpha) [14](https://public.com/about-us) [15](https://public.com/ai-agents/research) [16](https://public.com/mcp-trading)

**Статус и доступ.** Доступно, Alpha описана в старой FAQ, новый акцент на Agents. Alpha бесплатна по действующей FAQ и доступна в приложении и браузере. Условия новых Agents нужно проверять отдельно. Первый запуск или важный этап: Alpha в мае 2023, документация Research Agents от 30 июля 2026. [13](https://help.public.com/en/articles/9354354-what-is-alpha) [14](https://public.com/about-us) [15](https://public.com/ai-agents/research) [16](https://public.com/mcp-trading)

**Технология и границы.** Генеративная LLM и агенты с контекстом портфеля. GPT-4 подтвержден для Alpha, актуальная модель Research Agents не названа. GPT-4 раскрыт для Alpha, модель новых Research Agents неизвестна. Подтверждения закрытия Alpha нет. Ответы являются материалом для исследования, без гарантии точности. [13](https://help.public.com/en/articles/9354354-what-is-alpha) [14](https://public.com/about-us) [15](https://public.com/ai-agents/research) [16](https://public.com/mcp-trading)


<a name="gb05"></a>

### Public Generated Assets

**Кому и зачем.** США. Превратить инвестиционную гипотезу в собственный индекс.

**Что внедрено.** Отбор акций по текстовому описанию, объяснение состава, историческое тестирование, изменение весов и покупка индекса через брокерский счёт. [17](https://public.com/generated-asset)

**Статус и доступ.** Доступно, crypto/bonds expansion coming soon. Аккаунт Public. Точный текущий тариф не установлен. Первый запуск или важный этап: Точная дата запуска не установлена. [17](https://public.com/generated-asset)

**Технология и границы.** Многоагентный генеративный AI. Названия базовых моделей не раскрыты. Создаётся собственный индекс акций, а не отдельный зарегистрированный ETF. Исторические результаты гипотетические. Облигации и криптоактивы в этом модуле пока анонсированы. [17](https://public.com/generated-asset)


<a name="gb06"></a>

### eToro Tori

**Кому и зачем.** Израиль/глобальный брокер, доступ зависит от юрисдикции. Контекст портфеля, рыночные события и Agent Portfolio в диалоге.

**Что внедрено.** Память о разговорах, предпочтениях и позициях, текущие обсуждения рынка из X, анализ портфеля, создание и управление Agent Portfolio. [18](https://www.etoro.com/trading/platforms/tori/) [19](https://www.etoro.com/news-and-analysis/press-releases/etoros-ai-investing-companion-tori-gets-real-time-x-intelligence-powered-by-grok-4-2/) [20](https://help.etoro.com/s/article/Introducing-the-new-etoro-app?language=en_GB) [21](https://www.etoro.com/en-us/news-and-analysis/latest-news/press-release/etoro-leverages-ai-to-redefine-social-investing/)

**Статус и доступ.** Доступно, новый app поэтапно. Встроен в eToro. Новое приложение вводится постепенно, etoro AI является временным названием обновления. Единые условия по всем странам не установлены. Первый запуск или важный этап: Первый этап в 2025, перезапуск 16 апреля 2026, обновление приложения в октябре 2026. [18](https://www.etoro.com/trading/platforms/tori/) [19](https://www.etoro.com/news-and-analysis/press-releases/etoros-ai-investing-companion-tori-gets-real-time-x-intelligence-powered-by-grok-4-2/) [20](https://help.etoro.com/s/article/Introducing-the-new-etoro-app?language=en_GB) [21](https://www.etoro.com/en-us/news-and-analysis/latest-news/press-release/etoro-leverages-ai-to-redefine-social-investing/)

**Технология и границы.** Диалоговый LLM-агент. Grok 4.2 явно раскрыт. Набор функций зависит от страны и этапа запуска. Обсуждения в X не равнозначны проверенным фактам. Доказательств улучшения доходности нет. [18](https://www.etoro.com/trading/platforms/tori/) [19](https://www.etoro.com/news-and-analysis/press-releases/etoros-ai-investing-companion-tori-gets-real-time-x-intelligence-powered-by-grok-4-2/) [20](https://help.etoro.com/s/article/Introducing-the-new-etoro-app?language=en_GB) [21](https://www.etoro.com/en-us/news-and-analysis/latest-news/press-release/etoro-leverages-ai-to-redefine-social-investing/)


<a name="gb07"></a>

### Moomoo AI и API Skills

**Кому и зачем.** США/Канада/Япония и другие рынки Futu. Собрать данные рынка, новости/отчётность и вопросы по акциям.

**Что внедрено.** Диалог по акциям и рынку, ежедневные и еженедельные сводки, пересказ раскрытий, поиск бумаг и информации. Через API Skills подключаются внешние агенты. [22](https://invest.us.moomoo.com/ai) [23](https://www.moomoo.com/ca/feature/ai-trading) [24](https://www.moomoo.com/us/newsroom/moomooapiskills) [25](https://ir.futuholdings.com/static-files/2c9ec7c9-cdb5-463d-99d1-f0e353dbeae3)

**Статус и доступ.** Доступно, локальные варианты. Приложение и версия для компьютера. В Канаде предусмотрено ограниченное число бесплатных обращений. Условия других регионов отличаются. Первый запуск или важный этап: AI: 2025, API Skills 2026-04-23. [22](https://invest.us.moomoo.com/ai) [23](https://www.moomoo.com/ca/feature/ai-trading) [24](https://www.moomoo.com/us/newsroom/moomooapiskills) [25](https://ir.futuholdings.com/static-files/2c9ec7c9-cdb5-463d-99d1-f0e353dbeae3)

**Технология и границы.** LLM-помощник и подключение внешних агентов через API. LLM подтверждён, конкретная модель не раскрыта. Ассистент не видит установленную оценку склонности к риску. Прогнозные модули Pattern Finder и Trend Projection нельзя автоматически считать LLM-функциями. [22](https://invest.us.moomoo.com/ai) [23](https://www.moomoo.com/ca/feature/ai-trading) [24](https://www.moomoo.com/us/newsroom/moomooapiskills) [25](https://ir.futuholdings.com/static-files/2c9ec7c9-cdb5-463d-99d1-f0e353dbeae3)


<a name="gb08"></a>

### Futubull AI Expert Mode и AI Algo Trading

**Кому и зачем.** Гонконг. Полный путь исследования, стратегии и исполнения.

**Что внедрено.** Глубокое исследование в диалоге, заявки на акции, опционы и ETF обычным языком, создание, тестирование и запуск торговых стратегий без кода. [26](https://www.futuhk.com/en/about-us/newsroom/futu-announces-q2-2026-results) [27](https://www.prnewswire.com/apac/news-releases/futu-unveils-major-ai-upgrade-making-professional-agentic-investing-accessible-to-all-seize-the-next-rally-with-futu-ai-302827112.html) [25](https://ir.futuholdings.com/static-files/2c9ec7c9-cdb5-463d-99d1-f0e353dbeae3)

**Статус и доступ.** Запуск подтверждён компанией. Платформа Futubull. Текущий тариф и доступность конкретному счёту не установлены. Первый запуск или важный этап: AI: 2025, Expert Mode 2026-07-16. [26](https://www.futuhk.com/en/about-us/newsroom/futu-announces-q2-2026-results) [27](https://www.prnewswire.com/apac/news-releases/futu-unveils-major-ai-upgrade-making-professional-agentic-investing-accessible-to-all-seize-the-next-rally-with-futu-ai-302827112.html) [25](https://ir.futuholdings.com/static-files/2c9ec7c9-cdb5-463d-99d1-f0e353dbeae3)

**Технология и границы.** Встроенный генеративный агент и создание стратегий без кода. Собственный агент, базовая LLM не названа. Возможности гонконгского Futubull не означают тот же набор функций у Moomoo во всех странах. Независимой оценки качества нет. [26](https://www.futuhk.com/en/about-us/newsroom/futu-announces-q2-2026-results) [27](https://www.prnewswire.com/apac/news-releases/futu-unveils-major-ai-upgrade-making-professional-agentic-investing-accessible-to-all-seize-the-next-rally-with-futu-ai-302827112.html) [25](https://ir.futuholdings.com/static-files/2c9ec7c9-cdb5-463d-99d1-f0e353dbeae3)


<a name="gb09"></a>

### TigerAI, ранее TigerGPT

**Кому и зачем.** Сингапур/другие рынки Tiger Brokers. Разобрать акцию, новость, портфель и вопрос об опционах.

**Что внедрено.** Анализ позиций и списка наблюдения, объяснение движения акций и отчётности, ежедневный портфельный отчёт, специализированные агенты. [28](https://www.sec.gov/Archives/edgar/data/1756699/000119312526174855/tigr-20251231.htm) [29](https://www.prnewswire.com/apac/news-releases/tigergpt-pioneering-deepseek-integration-for-ai-chatbot-upgrading-smart-investment-assistance-302378677.html) [30](https://www.itiger.com/about/app/update)

**Статус и доступ.** Доступно, имена TigerGPT/TigerAI сосуществуют в источниках. Приложение Tiger Trade. Единый текущий тариф и полный список стран не установлены. Первый запуск или важный этап: TigerGPT апрель 2023, TigerAI 2024, DeepSeek 2025-02-18. [28](https://www.sec.gov/Archives/edgar/data/1756699/000119312526174855/tigr-20251231.htm) [29](https://www.prnewswire.com/apac/news-releases/tigergpt-pioneering-deepseek-integration-for-ai-chatbot-upgrading-smart-investment-assistance-302378677.html) [30](https://www.itiger.com/about/app/update)

**Технология и границы.** Инвестиционный LLM-помощник. В ранней версии раскрыт OpenAI, в феврале 2025 интегрирован DeepSeek-R1. Текущий набор моделей не раскрыт. TigerAI продолжает TigerGPT, это одна продуктовая линия. Текущая комбинация моделей неизвестна. TradingFront AI для управляющих активами относится к B2B. [28](https://www.sec.gov/Archives/edgar/data/1756699/000119312526174855/tigr-20251231.htm) [29](https://www.prnewswire.com/apac/news-releases/tigergpt-pioneering-deepseek-integration-for-ai-chatbot-upgrading-smart-investment-assistance-302378677.html) [30](https://www.itiger.com/about/app/update)


<a name="gb10"></a>

### Interactive Brokers: Ask IBKR, AI Integration, Autonomous Trading

**Кому и зачем.** США/глобально с исключениями. Проанализировать позиции и подготовить или исполнить действие по счёту.

**Что внедрено.** Вопросы о портфеле, экспозициях и денежных потоках, новости и скринеры, внешние LLM через MCP, инструкции для подтверждения клиентом, автономные заявки в выделенном разделе счёта. [31](https://www.interactivebrokers.com/en/trading/ai-hub.php) [32](https://www.interactivebrokers.com/en/general/about/mediaRelations/6-1-26.php) [33](https://www.interactivebrokers.com/en/general/about/mediaRelations/10-21-26.php) [34](https://www.interactivebrokers.com/en/trading/ai-integrations.php) [35](https://www.interactivebrokers.com/support/faq/content/connecting-ibkr-account-ai-platform-1437187133)

**Статус и доступ.** Ask IBKR и AI Integration доступны, Autonomous Trading объявлен и документирован с ограничениями. Ask IBKR: Client Portal и IBKR Desktop. Подключение внешнего AI без дополнительной платы брокеру, расходы на данные и AI могут сохраняться. Autonomous требует подходящего индивидуального немаржинального счёта и выполнения условий допуска. Первый запуск или важный этап: Интеграция Claude с 1 июня 2026, Autonomous Trading представлен 21 октября 2026, дата первого выпуска Ask IBKR неизвестна. [31](https://www.interactivebrokers.com/en/trading/ai-hub.php) [32](https://www.interactivebrokers.com/en/general/about/mediaRelations/6-1-26.php) [33](https://www.interactivebrokers.com/en/general/about/mediaRelations/10-21-26.php) [34](https://www.interactivebrokers.com/en/trading/ai-integrations.php) [35](https://www.interactivebrokers.com/support/faq/content/connecting-ibkr-account-ai-platform-1437187133)

**Технология и границы.** Встроенная портфельная аналитика с AI и внешние LLM-агенты. Модель Ask IBKR не названа. Внешние подключения: Claude, ChatGPT, Grok и Perplexity, Gemini заявлен как будущий. Обычная интеграция требует подтверждения каждой заявки. Официальные страницы расходятся по географии Autonomous, включая Великобританию, доступ нужно проверять для конкретного счёта. FAQ отдельно исключает автономную торговлю через ChatGPT на октябрь 2026 года. Размер AI Partition ограничен, детальные лимиты размера и частоты заявок пока планируются. [31](https://www.interactivebrokers.com/en/trading/ai-hub.php) [32](https://www.interactivebrokers.com/en/general/about/mediaRelations/6-1-26.php) [33](https://www.interactivebrokers.com/en/general/about/mediaRelations/10-21-26.php) [34](https://www.interactivebrokers.com/en/trading/ai-integrations.php) [35](https://www.interactivebrokers.com/support/faq/content/connecting-ibkr-account-ai-platform-1437187133)


<a name="gb11"></a>

### RockFlow Bobby

**Кому и зачем.** Международный retail-сервис, точная карта доступа неизвестна. Исследование и стратегии с исполнением из чата.

**Что внедрено.** Голосовой и текстовый анализ рынка и позиций, заявки и условные поручения, опционные комбинации, создание портфеля. [36](https://help.rockflow.ai/docs/innvative-products/rockflow-bobby/) [37](https://kr-asia.com/rockflows-bobby-is-an-ai-agent-that-trades-on-your-worldview-and-its-here)

**Статус и доступ.** Доступен по действующей инструкции. Приложение RockFlow. Текущий тариф и точная карта доступности неизвестны. Первый запуск или важный этап: Не позднее мая 2025, точная дата неизвестна. [36](https://help.rockflow.ai/docs/innvative-products/rockflow-bobby/) [37](https://kr-asia.com/rockflows-bobby-is-an-ai-agent-that-trades-on-your-worldview-and-its-here)

**Технология и границы.** Агент, сочетающий LLM и заданные рабочие сценарии. Применение LLM подтверждено интервью основателя, конкретная модель не раскрыта. Операционные инструкции требуют повторного подтверждения. Интервью основателя описывает архитектуру, но не является независимым испытанием эффективности. [36](https://help.rockflow.ai/docs/innvative-products/rockflow-bobby/) [37](https://kr-asia.com/rockflows-bobby-is-an-ai-agent-that-trades-on-your-worldview-and-its-here)


<a name="gb12"></a>

### Charles Schwab: Portfolio Insights, Charley, MCP

**Кому и зачем.** США. Объяснить изменение портфеля, получить информацию и перейти к действию через диалог.

**Что внедрено.** Сводки портфеля и новостей с комментариями аналитиков, разговор с Charley, подключение Claude к данным, исследованию и торговым действиям. [38](https://pressroom.aboutschwab.com/press-releases/press-release/2026/Charles-Schwab-Launches-AI-Powered-Capability-That-Helps-Investors-Understand-Portfolio-Performance-and-Market-Activity/default.aspx) [39](https://pressroom.aboutschwab.com/press-releases/press-release/2026/Meet-Charley-Schwabs-New-AI-Powered-Assistant-Designed-to-Help-Clients-Get-Answers-and-Take-Action/default.aspx) [40](https://pressroom.aboutschwab.com/press-releases/press-release/2026/Schwab-Announces-Platform-Enhancements-Including-MCP-Server-to-Connect-Clients-AI-Platforms-With-Their-Schwab-Accounts/default.aspx)

**Статус и доступ.** Insights доступно, Charley rollout, MCP ограниченный пилот. Подходящие розничные клиенты США. Charley вводится постепенно. MCP доступен выбранным участникам пилота, торговые действия требуют счёта с доступом к thinkorswim. Первый запуск или важный этап: Portfolio Insights 5 мая 2026, анонс Charley 30 сентября, пилот MCP 12 ноября 2026. [38](https://pressroom.aboutschwab.com/press-releases/press-release/2026/Charles-Schwab-Launches-AI-Powered-Capability-That-Helps-Investors-Understand-Portfolio-Performance-and-Market-Activity/default.aspx) [39](https://pressroom.aboutschwab.com/press-releases/press-release/2026/Meet-Charley-Schwabs-New-AI-Powered-Assistant-Designed-to-Help-Clients-Get-Answers-and-Take-Action/default.aspx) [40](https://pressroom.aboutschwab.com/press-releases/press-release/2026/Schwab-Announces-Platform-Enhancements-Including-MCP-Server-to-Connect-Clients-AI-Platforms-With-Their-Schwab-Accounts/default.aspx)

**Технология и границы.** Генеративный AI/LLM. Для Charley подтверждена LLM без названия, MCP-пилот использует Claude. thinkorswim Assistant на 12 ноября 2026 года ещё ожидается. Пилот MCP не является общедоступной функцией. Покрытие Portfolio Insights расширено относительно первоначальных акций S&P 500. [38](https://pressroom.aboutschwab.com/press-releases/press-release/2026/Charles-Schwab-Launches-AI-Powered-Capability-That-Helps-Investors-Understand-Portfolio-Performance-and-Market-Activity/default.aspx) [39](https://pressroom.aboutschwab.com/press-releases/press-release/2026/Meet-Charley-Schwabs-New-AI-Powered-Assistant-Designed-to-Help-Clients-Get-Answers-and-Take-Action/default.aspx) [40](https://pressroom.aboutschwab.com/press-releases/press-release/2026/Schwab-Announces-Platform-Enhancements-Including-MCP-Server-to-Connect-Clients-AI-Platforms-With-Their-Schwab-Accounts/default.aspx)


<a name="gb13"></a>

### SaxoInvestor AI Assistant

**Кому и зачем.** Дания, международная платформа, для клиентов Великобритании подтверждён английский язык. Вопросы по портфелю, инструментам и подготовка заявки.

**Что внедрено.** Позиции, операции, дивиденды, расходы и результаты, поиск инструментов, списки наблюдения, ценовые уведомления и заполнение торговой заявки. [41](https://www.help.saxo/hc/en-us/articles/39490128562589-Using-the-AI-Assistant-in-the-new-SaxoInvestor)

**Статус и доступ.** Доступен только в новом SaxoInvestor. Только новый SaxoInvestor. На других платформах Saxo помощник пока отсутствует. Для клиентов Великобритании указан английский. Отдельный тариф неизвестен. Первый запуск или важный этап: Дата первого запуска неизвестна, справка обновлена 22 октября 2026. [41](https://www.help.saxo/hc/en-us/articles/39490128562589-Using-the-AI-Assistant-in-the-new-SaxoInvestor)

**Технология и границы.** Диалоговый AI. Техническое семейство и название модели не раскрыты. Помощник не отправляет заявку: это делает клиент. Персональные инвестиционные рекомендации и оценка пригодности стратегии исключены. Техническое семейство модели не раскрыто. [41](https://www.help.saxo/hc/en-us/articles/39490128562589-Using-the-AI-Assistant-in-the-new-SaxoInvestor)


<a name="gb14"></a>

### Groww GR-1 и Groww MCP

**Кому и зачем.** Индия. Понять движение акций, оценку фондов и собственный портфель.

**Что внедрено.** Вопросы с учётом портфеля и новостей, объясняющие карточки по акциям, разбор фондов MF Prime, уведомления, списки наблюдения и подготовка заявки. [42](https://groww.in/updates/gr-1-ai-investing-assistant-groww) [43](https://groww.in/updates/groww-mcp)

**Статус и доступ.** GR-1 встроен и доступен, расширяется покрытие. Приложение Groww. Карточки GR-1 охватывают 750 акций с дальнейшим расширением, функции фондов связаны с MF Prime. MCP ограничен акциями и срочными инструментами, часть функций требует разрешений и подписки на внешний AI. Первый запуск или важный этап: MCP представлен 4 августа 2025, GR-1 beta в феврале 2026, описание запуска от 23 октября 2026. [42](https://groww.in/updates/gr-1-ai-investing-assistant-groww) [43](https://groww.in/updates/groww-mcp)

**Технология и границы.** Встроенный диалоговый AI и внешняя LLM через MCP. Модель GR1 неизвестна, Claude4Sonnet лишь рекомендация для MCP. GR-1 не исполняет заявки автоматически и требует явного подтверждения. Рекомендация Claude для MCP не раскрывает модель GR-1. Покрытие карточек ещё не охватывает все акции. [42](https://groww.in/updates/gr-1-ai-investing-assistant-groww) [43](https://groww.in/updates/groww-mcp)


<a name="gb15"></a>

### Zerodha Kite MCP

**Кому и зачем.** Индия. Проанализировать портфель, позиции и рынок в выбранном ИИ-ассистенте.

**Что внедрено.** Данные маржи, прибыли и убытков, котировок и позиций, анализ портфеля, рыночных экспозиций и опционных позиций через внешний AI. [44](https://zerodha.com/z-connect/general/connect-your-zerodha-account-to-ai-assistants-with-kite-mcp)

**Статус и доступ.** Доступная техническая интеграция. Без дополнительной платы Zerodha. Выбранный сторонний AI может требовать платной подписки. Первый запуск или важный этап: 2025-05-20. [44](https://zerodha.com/z-connect/general/connect-your-zerodha-account-to-ai-assistants-with-kite-mcp)

**Технология и границы.** Внешняя LLM с доступом к инструментам брокера. Пользователь выбирает модель в совместимом клиенте, например Claude, Cursor или Windsurf. Основной режим: чтение и анализ. Официальная страница одновременно исключает обычные заявки и упоминает исключение для GTT, универсальная торговля через MCP не подтверждена. [44](https://zerodha.com/z-connect/general/connect-your-zerodha-account-to-ai-assistants-with-kite-mcp)


<a name="gb16"></a>

### SoFi Coach

**Кому и зачем.** США. Связать инвестиции с денежными потоками, долгами и финансовыми целями.

**Что внедрено.** Общая картина связанных финансовых счетов, инвестиционные цели и портфель, отдельная карточка подтверждения брокерского поручения в чате. [45](https://investors.sofi.com/news/news-details/2026/Introducing-SoFi-Coach-An-AI-Powered-Financial-Guide-to-Help-Members-Get-Their-Money-Right/default.aspx) [46](https://www.sofi.com/terms-of-use/) [47](https://www.sofi.com/is-sofi-coach-safe-and-is-it-worth-it/)

**Статус и доступ.** Доступен всем клиентам по текущей странице. Бесплатно для участников SoFi в приложении по текущей странице. Первоначальный запуск для Plus не отражает нынешний доступ. Первый запуск или важный этап: 2 июня 2026, сначала для SoFi Plus. [45](https://investors.sofi.com/news/news-details/2026/Introducing-SoFi-Coach-An-AI-Powered-Financial-Guide-to-Help-Members-Get-Their-Money-Right/default.aspx) [46](https://www.sofi.com/terms-of-use/) [47](https://www.sofi.com/is-sofi-coach-safe-and-is-it-worth-it/)

**Технология и границы.** Генеративный финансовый чат. Базовая LLM не раскрыта. Текущие условия предусматривают торговую карточку с обязательным подтверждением точных параметров. Это подготовка поручения, без автономной торговли и персональной рекомендации. [45](https://investors.sofi.com/news/news-details/2026/Introducing-SoFi-Coach-An-AI-Powered-Financial-Guide-to-Help-Members-Get-Their-Money-Right/default.aspx) [46](https://www.sofi.com/terms-of-use/) [47](https://www.sofi.com/is-sofi-coach-safe-and-is-it-worth-it/)


<a name="gb17"></a>

### Ant Fortune / Alipay Maxiaocai

**Кому и зачем.** Китай. Объяснить рынок и отчётность, следить за собственными инвестициями.

**Что внедрено.** Рыночные объяснения и визуальные сводки отчётов, персональный AI-экран с учётом позиций и списка наблюдения, объяснение важных событий. [48](https://www.businesswire.com/news/home/20240905719583/en/Ant-Group-Unveils-AI-Financial-Manager-at-Shanghais-INCLUSION-Conference) [49](https://m.app.mi.com/details?id=com.antfortune.wealth)

**Статус и доступ.** Работает, обновление приложения 13 ноября 2026. Alipay и Ant Fortune для китайского рынка. Приложение распространяется бесплатно, отдельные продуктовые комиссии и условия AI не установлены. Первый запуск или важный этап: Обновлённая публичная версия представлена 2024-09-06, точная дата самого раннего запуска не установлена. [48](https://www.businesswire.com/news/home/20240905719583/en/Ant-Group-Unveils-AI-Financial-Manager-at-Shanghais-INCLUSION-Conference) [49](https://m.app.mi.com/details?id=com.antfortune.wealth)

**Технология и границы.** Генеративный финансовый помощник. Собственные фундаментальные модели Ant, точная текущая версия не раскрыта. Старая статистика аудитории не является текущей. Функции размещения сделок этим набором источников не подтверждены. Maxiaocai для частного пользователя нужно отличать от институциональных версий. [48](https://www.businesswire.com/news/home/20240905719583/en/Ant-Group-Unveils-AI-Financial-Manager-at-Shanghais-INCLUSION-Conference) [49](https://m.app.mi.com/details?id=com.antfortune.wealth)


<a name="gb18"></a>

### East Money Miaoxiang

**Кому и зачем.** Китай. Разобрать акцию, новости и рынок, найти инструменты под запрос.

**Что внедрено.** Диалоговые ответы, анализ котировок и новостей, скрининг акций, объяснение финансовых и отраслевых факторов. В 2026 году добавлены MiaoxiangClaw и каталог навыков. [50](https://www.eastmoney.com/) [51](https://static.cninfo.com.cn/finalpage/2026-08-22/1225491772.PDF) [52](https://app.meizu.com/apps/public/detail?package_name=com.eastmoney.innovation.android)

**Статус и доступ.** Работает внутри East Money и как самостоятельное приложение. Главная страница East Money предлагает бесплатное использование встроенной модели, есть отдельные Miaoxiang и исследовательский помощник. Тарифы расширенных возможностей неизвестны. Первый запуск или важный этап: Точная дата запуска неизвестна, актуальные раскрытия 2026 года. [50](https://www.eastmoney.com/) [51](https://static.cninfo.com.cn/finalpage/2026-08-22/1225491772.PDF) [52](https://app.meizu.com/apps/public/detail?package_name=com.eastmoney.innovation.android)

**Технология и границы.** Финансовая большая языковая модель и приложение. Собственная модель под маркой Miaoxiang, точная базовая версия неизвестна. Корпоративное раскрытие подтверждает работу в новостях, котировках и списках наблюдения, но не качество рекомендаций. Наличие AI в экосистеме не доказывает автоматическую торговлю или те же функции в Choice Terminal. [50](https://www.eastmoney.com/) [51](https://static.cninfo.com.cn/finalpage/2026-08-22/1225491772.PDF) [52](https://app.meizu.com/apps/public/detail?package_name=com.eastmoney.innovation.android)


<a name="asa01"></a>

### SBI Securities Plus: AI Market Summary

**Кому и зачем.** Япония. Быстро понять итоги рынка Японии и США, предстоящие события и отчётность.

**Что внедрено.** Утренняя и вечерняя сводки с дополнительными обновлениями в течение дня. Обзор японского и американского рынка. Календарь событий и значимых публикаций результатов компаний. [148](https://search.sbisec.co.jp/v2/popwin/guide/tool/sbi_app/05_market/ai.html)

**Статус и доступ.** Доступен в SBI Securities Plus по действующей инструкции. Раздел Find и домашний экран после входа в приложение SBI Securities Plus. Отдельный тариф функции в инструкции не указан. Первый запуск или важный этап: Точная дата запуска не раскрыта в инструкции. [148](https://search.sbisec.co.jp/v2/popwin/guide/tool/sbi_app/05_market/ai.html)

**Технология и границы.** Генерация рыночных сводок языковой моделью. Gemini от Google, контент готовит AlpacaTech на основе отобранных новостей и данных MINKABU. Готовые информационные сводки, а не персональная инвестиционная рекомендация или торговый агент. Покрытие ограничено условиями отбора бумаг и источников, модель не раскрыта до версии. [148](https://search.sbisec.co.jp/v2/popwin/guide/tool/sbi_app/05_market/ai.html)


<a name="asa02"></a>

### Rakuten Securities Investment AI Assistant beta plus

**Кому и зачем.** Япония. Разобраться в инвестиционных терминах, вопросах начала инвестирования и найти подходящие материалы.

**Что внедрено.** Ответы на вопросы об инвестициях и деньгах. Поиск материалов инвестиционного медиа Toushiru. Объяснения простым языком с уточняющим диалогом. [149](https://www.rakuten-sec.co.jp/assistant/)

**Статус и доступ.** Открытая beta с дневным лимитом. Веб-чат доступен круглосуточно, beta с дневным лимитом, который возобновляется примерно в 08:30. Отдельная цена не указана. Первый запуск или важный этап: Доступен не позднее 2024, обновление до GPT-4.1 25.07.2025. [149](https://www.rakuten-sec.co.jp/assistant/)

**Технология и границы.** LLM-диалог по инвестиционным и образовательным материалам брокера. GPT-4.1 раскрыт на действующем лендинге, ранее GPT-3.5 и GPT-4o. Помощник соединяет инвестиционное обучение и навигацию по материалам брокера. Чтение личного портфеля, персональные рекомендации и отправка заявок не подтверждены. [149](https://www.rakuten-sec.co.jp/assistant/)


<a name="asa03"></a>

### Dhan MCP и Dhan Skills

**Кому и зачем.** Индия. Обсудить рынок и позиции, проверить маржу и выполнить разрешённые действия, построить торговую автоматизацию.

**Что внедрено.** MCP получает котировки, глубину рынка, опционные цепочки, позиции и средства. Расчёт маржи, размещение, изменение и отмена заявок. Skills помогают агенту написать автоматизацию по API, включая данные и торговые действия. [150](https://dhan.co/blog/trading-strategies/why-trade-intraday-with-claude-try-dhan-mcp-skills/) [151](https://github.com/dhan-oss/dhanhq-skills/blob/main/skills/dhanhq/SKILL.md)

**Статус и доступ.** Официальные MCP и Skills доступны. Активный счёт Dhan и совместимый AI-клиент с авторизацией, права предоставляются в рамках сессии. Рыночные Data API требуют активного плана данных, торговые операции через SDK требуют разрешённого статического IP по инструкции Skill. Точная цена MCP в использованных первичных источниках не указана. Первый запуск или важный этап: Подтверждены официальной публикацией 13.08.2026, точный первый запуск не установлен. [150](https://dhan.co/blog/trading-strategies/why-trade-intraday-with-claude-try-dhan-mcp-skills/) [151](https://github.com/dhan-oss/dhanhq-skills/blob/main/skills/dhanhq/SKILL.md)

**Технология и границы.** Внешние LLM вызывают инструменты MCP, coding agents используют документацию Skills и SDK для автоматизации. Модель определяется внешним клиентом, названы Claude, Claude Code, Codex, Cursor и другие совместимые клиенты. MCP предоставляет инструменты данных и торговли, Skills помогают программному агенту создавать автоматизацию через SDK. Права и процедура подтверждения зависят от клиентского сценария. [150](https://dhan.co/blog/trading-strategies/why-trade-intraday-with-claude-try-dhan-mcp-skills/) [151](https://github.com/dhan-oss/dhanhq-skills/blob/main/skills/dhanhq/SKILL.md)


<a name="asa04"></a>

### Upstox MCP и Agent Skills

**Кому и зачем.** Индия. Разобрать позиции и рынок через чат или построить и выполнить торговый процесс в coding agent.

**Что внедрено.** MCP читает holdings, позиции, результат, средства и рыночные данные. Agent Skill размещает, изменяет, отменяет и закрывает заявки, включая GTT и многошаговые опционные комбинации. SDK предоставляет данные и проверку маржи, Skill предусматривает подтверждения и тестовую среду. [152](https://upstox.com/developer/api-documentation/announcements/agent-skills-launch/) [153](https://upstox.com/developer/api-documentation/mcp-integration/)

**Статус и доступ.** MCP и Agent Skills доступны, с разными правами. MCP бесплатен для активного счёта Upstox, требует ежедневной повторной авторизации и совместимого AI-клиента. Agent Skill требует отдельной установки, Python SDK, токен и подходящие разрешения. Тариф AI-клиента и рыночных данных определяется отдельно. Первый запуск или важный этап: Agent Skills 2026-06-06, точный первый запуск MCP не установлен. [152](https://upstox.com/developer/api-documentation/announcements/agent-skills-launch/) [153](https://upstox.com/developer/api-documentation/mcp-integration/)

**Технология и границы.** Read-only MCP для диалога, LLM coding agent с SDK для торговых действий. Внешний AI выбирается пользователем, Skill совместим с Claude Code, Codex и Agent Skills средами. MCP работает только на чтение. Торговые действия относятся к отдельному Agent Skill с SDK, это другая среда, чем обычный чат-коннектор. [152](https://upstox.com/developer/api-documentation/announcements/agent-skills-launch/) [153](https://upstox.com/developer/api-documentation/mcp-integration/)


<a name="asa05"></a>

### INDmoney MCP

**Кому и зачем.** Индия. Объединить разные классы активов и объяснить портфель, регулярные инвестиции и рыночные данные.

**Что внедрено.** Совокупный капитал, распределение и позиции по активам. Вопросы по регулярным покупкам акций и фондов. Индийские и американские котировки, опционные цепочки и сравнение фондов. 14 документированных возможностей, многошаговый анализ через Claude. [154](https://www.indmoney.com/mcp)

**Статус и доступ.** Официальное подключение доступно. Бесплатно для клиентов INDmoney, вход и согласие через INDmoney. Нужен совместимый AI-клиент, чьи платные функции могут иметь собственные условия. Первую настройку рекомендуют с компьютера. Первый запуск или важный этап: Точная дата первого запуска не указана на продуктовой странице. [154](https://www.indmoney.com/mcp)

**Технология и границы.** Внешняя LLM использует инструменты портфельных и рыночных данных. Основной документированный клиент Claude, конкретную модель выбирает пользователь. Строго чтение: нельзя разместить сделку, погасить инвестицию, изменить план регулярных покупок или настройки. В импортированных счетах других брокеров может не хватать первоначальной стоимости вложений, внешние американские счета не покрываются как собственный US account INDmoney. [154](https://www.indmoney.com/mcp)


<a name="asa06"></a>

### DBS digiWealth: GenAI digibot

**Кому и зачем.** Сингапур, другие банковские функции также в Гонконге и Тайване. Получить ответы на вопросы об инвестициях, капитале и страховании, перейти к человеку-консультанту.

**Что внедрено.** Естественный диалог и уточняющие вопросы по инвестиционным темам. Интеграция в digiWealth. Персонализированные ответы после входа, связь с wealth planning manager для более детального совета. [155](https://www.dbs.com.sg/personal/digital-banking/digibot) [156](https://www.dbs.com/NewsPrinter.page?locale=en&newsId=mqdetosw)

**Статус и доступ.** Инвестиционная информационная функция доступна по текущей справке. DBS/POSB digibank mobile и online, для персонализированных GenAI ответов нужен вход. Точная отдельная цена инвестиционного чата не указана. Первый запуск или важный этап: Интеграция с digiWealth анонсирована с августа2026, точный первый день фактического запуска не установлен. [155](https://www.dbs.com.sg/personal/digital-banking/digibot) [156](https://www.dbs.com/NewsPrinter.page?locale=en&newsId=mqdetosw)

**Технология и границы.** Генеративный диалог в финансовом приложении. Название и версия базовой LLM не раскрыты в рассмотренных продуктовых материалах. Здесь подтверждена информационная помощь по инвестициям в банковском приложении. Автономный выбор и исполнение биржевых сделок не подтверждены. Покрытие зависит от страны и конкретной функции digiWealth. [155](https://www.dbs.com.sg/personal/digital-banking/digibot) [156](https://www.dbs.com/NewsPrinter.page?locale=en&newsId=mqdetosw)


<a name="gba01"></a>

### Lightyear AI

**Кому и зачем.** Великобритания / Эстония, европейский розничный рынок. Быстро понять события вокруг акции и аргументы сторон.

**Что внедрено.** Lightning Updates: новости о резких движениях бумаг из портфеля и списка наблюдения. Why Did It Move: объяснение выбранного периода на графике через новости и события. Bulls Say / Bears Say: аргументы за и против инвестиции на основе внешних источников. [157](https://lightyear.com/en-hu/lightyear-ai) [158](https://lightyear.com/en-es/blog/lightyear-closes-dollar23m-series-b)

**Статус и доступ.** Три аналитические функции доступны, персональные рекомендации и автономное управление описаны как будущие направления. В приложении Lightyear, при запуске компания указала отсутствие подписки и платного доступа к этим трём функциям. Первый запуск или важный этап: 2025-07-23. [157](https://lightyear.com/en-hu/lightyear-ai) [158](https://lightyear.com/en-es/blog/lightyear-closes-dollar23m-series-b)

**Технология и границы.** Генеративные сводки и объяснение движения цены. Базовая модель и её поставщик не раскрыты в рассмотренных материалах. Текущие инструменты дают информацию. Advice at scale и Self-driving money на сайте относятся к будущему и требуют соответствующих разрешений. Личные и портфельные данные, по заявлению Lightyear, поставщикам моделей не передаются. [157](https://lightyear.com/en-hu/lightyear-ai) [158](https://lightyear.com/en-es/blog/lightyear-closes-dollar23m-series-b)


<a name="gba02"></a>

### Revolut AIR: инвестиционные вопросы

**Кому и зачем.** Великобритания, доступ зависит от рынка и этапа внедрения Revolut. Спросить о своих инвестициях и причинах изменения стоимости.

**Что внедрено.** Ответы с использованием состава активов, истории операций и внешних рыночных данных. Проактивные объяснения прошлых движений бумаг, которыми клиент владеет или за которыми следит. [159](https://help.revolut.com/en-GB/help/profile-and-plan/getting-started-with-air/) [160](https://www.revolut.com/legal/rita-disclaimer/)

**Статус и доступ.** Доступен части клиентов, поэтапное внедрение. Через AIR в приложении Revolut, функция появляется по мере внедрения. Отдельный тариф инвестиционных ответов не установлен по открытым материалам. Первый запуск или важный этап: Точная первоначальная дата не установлена. [159](https://help.revolut.com/en-GB/help/profile-and-plan/getting-started-with-air/) [160](https://www.revolut.com/legal/rita-disclaimer/)

**Технология и границы.** Разговорный генеративный ассистент с персональным финансовым контекстом. Конкретная базовая LLM не названа. AIR не может разместить, изменить или отменить поручение по финансовому инструменту. Нельзя переносить на AIR возможности отдельного сервиса Revolut X для криптоактивов. AI Support и AIR описаны в правилах как разные помощники. [159](https://help.revolut.com/en-GB/help/profile-and-plan/getting-started-with-air/) [160](https://www.revolut.com/legal/rita-disclaimer/)


<a name="gba03"></a>

### Trading 212: AI Analysis, AI Chat, AI Search и Agent Skills

**Кому и зачем.** Великобритания / Европа, типы счетов и рынки различаются. Исследовать бумагу и собственный портфель, искать инструменты обычной фразой, отдельный технический канал позволяет агенту работать с API.

**Что внедрено.** AI Analysis: причины движения цены, новости, фундаментальные показатели и риски, отдельный обзор портфеля. AI Chat: сравнение инструментов, вопросы о портфеле и истории счёта. AI Search преобразует фразу в фильтры и объясняет результаты. Официальные Agent Skills: позиции, история и создание/управление рыночными, лимитными и стоп-поручениями через API. [161](https://helpcentre.trading212.com/hc/en-us/articles/28908866191005-AI-Analysis-on-Trading-212) [162](https://helpcentre.trading212.com/hc/en-us/articles/34746261653277-The-AI-Chatbot-Analyser) [163](https://helpcentre.trading212.com/hc/en-us/articles/40606617501981-What-is-AI-Search-and-how-do-I-use-it) [164](https://helpcentre.trading212.com/hc/en-us/articles/38710364614685-What-can-I-ask-AI-Chat-about-my-account-history) [165](https://github.com/trading212-labs/agent-skills)

**Статус и доступ.** Анализ и чат доступны, AI Search внедряется постепенно, API для внешних агентов находится в бета-версии. Нативные функции находятся на страницах инструментов, портфеля и поиска. История счёта в чате поддерживает Invest, ISA и SIPP, внешний API поддерживает Invest и Stocks ISA, в тестовом и реальном режимах. Первый запуск или важный этап: Точные первые даты нативных функций не установлены, публичные Agent Skills опубликованы в 2026 году. [161](https://helpcentre.trading212.com/hc/en-us/articles/28908866191005-AI-Analysis-on-Trading-212) [162](https://helpcentre.trading212.com/hc/en-us/articles/34746261653277-The-AI-Chatbot-Analyser) [163](https://helpcentre.trading212.com/hc/en-us/articles/40606617501981-What-is-AI-Search-and-how-do-I-use-it) [164](https://helpcentre.trading212.com/hc/en-us/articles/38710364614685-What-can-I-ask-AI-Chat-about-my-account-history) [165](https://github.com/trading212-labs/agent-skills)

**Технология и границы.** Генеративная аналитика, разговорный поиск и подключение внешней LLM через API. Поставщик нативных моделей не раскрыт, внешние Agent Skills совместимы, в частности, с Claude Code, Codex CLI и OpenClaw. Чат не даёт указаний купить, продать или держать. История CFD и криптосчетов и текущий денежный остаток в указанной функции истории не поддерживаются. Нельзя приписывать нативному чату торговые права Agent Skills: это отдельное подключение с API-ключом и его разрешениями. У API статус beta. [161](https://helpcentre.trading212.com/hc/en-us/articles/28908866191005-AI-Analysis-on-Trading-212) [162](https://helpcentre.trading212.com/hc/en-us/articles/34746261653277-The-AI-Chatbot-Analyser) [163](https://helpcentre.trading212.com/hc/en-us/articles/40606617501981-What-is-AI-Search-and-how-do-I-use-it) [164](https://helpcentre.trading212.com/hc/en-us/articles/38710364614685-What-can-I-ask-AI-Chat-about-my-account-history) [165](https://github.com/trading212-labs/agent-skills)


<a name="gba04"></a>

### Scalable: Insights и Agentic Investing

**Кому и зачем.** Германия, европейские клиенты Scalable с учётом доступности сервиса. Обсудить инвестиции и работать с брокерским счётом из выбранного AI-ассистента.

**Что внедрено.** Обзор позиций, диверсификации и сценариев портфеля. Поиск инструментов и работа со списками наблюдения и ценовыми уведомлениями. Подготовка сделок и создание/изменение планов регулярных инвестиций через MCP/CLI. [166](https://de.scalable.capital/newsroom/agentic-investing) [167](https://help.scalable.capital/de-AT/agentic-investing-aac939f8/welche-funktionen-unterst%C3%BCtzt-das-scalable-mcp-mit-ihren-73428605)

**Статус и доступ.** Insights работает, Agentic Investing запущен, конкретные действия зависят от платформы агента. Нужны счёт Scalable и совместимый внешний ассистент для MCP/CLI. Есть четыре уровня доступа: без доступа, чтение, ограниченные изменения и полный доступ. Детские счета не поддерживаются. Первый запуск или важный этап: Insights: август 2025, Agentic Investing: 2026-08-25. [166](https://de.scalable.capital/newsroom/agentic-investing) [167](https://help.scalable.capital/de-AT/agentic-investing-aac939f8/welche-funktionen-unterst%C3%BCtzt-das-scalable-mcp-mit-ihren-73428605)

**Технология и границы.** Нативный разговорный помощник и подключение внешних LLM через MCP/CLI. Для внешнего подключения компания называет ChatGPT, Claude и Grok. Базовая модель нативного Insights по первичным источникам не установлена. Даже при полном доступе покупка или продажа требует отдельного явного подтверждения после предварительного просмотра. Для регулярных инвестиционных планов действует такой же двухэтапный порядок. Разрешение распространяется на подключённых агентов и портфели, собственные правила AI-платформы могут дополнительно ограничивать действия. [166](https://de.scalable.capital/newsroom/agentic-investing) [167](https://help.scalable.capital/de-AT/agentic-investing-aac939f8/welche-funktionen-unterst%C3%BCtzt-das-scalable-mcp-mit-ihren-73428605)


<a name="gba05"></a>

### Vanguard Digital Advisor: AI Chat

**Кому и зачем.** США. Объяснение персонального финансового плана и проверка сценариев в Digital Advisor.

**Что внедрено.** Диалог о целях, финансовом плане и стратегии клиента. Сценарии «что, если» и финансовое обучение на основе базы знаний Vanguard. [168](https://personal1.vanguard.com/pdf/vanguard-digital-advice-brochure.pdf)

**Статус и доступ.** Бета-версия с ограниченным доступом. Ограниченная группа клиентов Digital Advisor, дальнейшее расширение доступа запланировано. Отдельная стоимость AI Chat в рассмотренном раскрытии не указана. Первый запуск или важный этап: Сентябрь 2026. [168](https://personal1.vanguard.com/pdf/vanguard-digital-advice-brochure.pdf)

**Технология и границы.** Генеративный разговорный слой поверх детерминированного цифрового консультирования. В брошюре прямо указаны large language models, конкретный поставщик и версия не названы. Чат не меняет алгоритм советов Digital Advisor, не ребалансирует портфель и не совершает сделки. Данные разговора сами по себе не меняют профиль клиента. Это не универсальный автономный управляющий Vanguard. [168](https://personal1.vanguard.com/pdf/vanguard-digital-advice-brochure.pdf)


<a name="gba06"></a>

### Betterment Account Recommender

**Кому и зачем.** США. Помочь выбрать подходящий тип финансового счёта и понять основание рекомендации.

**Что внедрено.** Механизм правил использует доход, активы, занятость, налоговый статус и сведения о подключённых счетах. Генеративный AI формулирует персональное объяснение уже полученной рекомендации. [169](https://www.prnewswire.com/news-releases/betterment-launches-ai-enabled-account-recommender-advancing-enterprise-ai-strategy-302707654.html) [170](https://www.betterment.com/adv)

**Статус и доступ.** Запущен. Необязательный инструмент на платформе Betterment. Для персонализации используются данные профиля и счетов, отдельная плата за функцию в рассмотренных материалах не указана. Первый запуск или важный этап: 2026-03-09. [169](https://www.prnewswire.com/news-releases/betterment-launches-ai-enabled-account-recommender-advancing-enterprise-ai-strategy-302707654.html) [170](https://www.betterment.com/adv)

**Технология и границы.** LLM объясняет результат рекомендательного механизма с заданными правилами. Актуальный Form ADV прямо указывает сторонние LLM, поставщики и версии не названы. Тип счёта рекомендует механизм с заданными правилами, разработанными консультантами. LLM составляет объяснение после этого шага. Клиент сам решает, какой счёт открыть, из этой функции не следует участие LLM в отборе бумаг или управлении портфелем. [169](https://www.prnewswire.com/news-releases/betterment-launches-ai-enabled-account-recommender-advancing-enterprise-ai-strategy-302707654.html) [170](https://www.betterment.com/adv)


<a name="gba08"></a>

### FirstradeGPT

**Кому и зачем.** США. Проводить фундаментальное исследование компаний внутри брокерского приложения.

**Что внедрено.** Вопросы о показателях компании, сегментах бизнеса и исторических данных. Сравнение компаний, таблицы/графики и уточняющие вопросы. [174](https://www.firstrade.com/press/pr20240620) [175](https://help.firstrade.info/en/articles/9457471-firstradegpt-how-tos)

**Статус и доступ.** Доступен клиентам. Клиенты Firstrade: веб-версия через Research & Tools, мобильная через Explore. Интерфейс помощника на английском, отдельная цена в рассмотренных материалах не указана. Первый запуск или важный этап: Июнь 2024: страница 20 июня, в тексте релиза 18 июня. [174](https://www.firstrade.com/press/pr20240620) [175](https://help.firstrade.info/en/articles/9457471-firstradegpt-how-tos)

**Технология и границы.** LLM-ассистент по финансовым данным через FinChat.io. В раскрытии запуска указаны модели OpenAI и Anthropic через FinChat.io, конкретные версии не названы. FirstradeGPT не имеет доступа к инвестиционному счёту пользователя. Нельзя описывать его как анализатор личного портфеля или торгового агента. Сведения и ответы не являются персональным инвестиционным советом. [174](https://www.firstrade.com/press/pr20240620) [175](https://help.firstrade.info/en/articles/9457471-firstradegpt-how-tos)


<a name="gba09"></a>

### Nordnet: Latest Recap и AI-сводки отчётности

**Кому и зачем.** Швеция, внедрение на других рынках Северной Европы. Читать краткие новости по собственным позициям и результаты компаний.

**Что внедрено.** Latest Recap: новости по принадлежащим клиенту бумагам в обзоре счёта приложения. К новостям добавлен макроэкономический контекст. Сводки квартальных отчётов на сайте и в приложении. [176](https://nordnetab.com/wp-content/uploads/2026/04/1Q-2026-Sve.pdf)

**Статус и доступ.** Работают в Швеции, по данным отчёта Q1 2026 внедрение отчётных сводок на остальных североевропейских рынках продолжалось. Сводки отчётности были доступны всем шведским клиентам по состоянию на Q1 2026. Из рассмотренного отчёта нельзя установить завершение внедрения во всех остальных странах к ноябрю. Отдельная цена не раскрыта. Первый запуск или важный этап: Первый квартал 2026: внедрение подтверждено квартальным отчётом. [176](https://nordnetab.com/wp-content/uploads/2026/04/1Q-2026-Sve.pdf)

**Технология и границы.** AI-генерация кратких новостей и сводок отчётности. Генеративная функция названа прямо, архитектура, базовая LLM и её поставщик не раскрыты. Подтверждён именно слой кратких текстовых материалов. Квартальный отчёт не даёт основания называть его чат-советником или самостоятельным торговым агентом. [176](https://nordnetab.com/wp-content/uploads/2026/04/1Q-2026-Sve.pdf)


<a name="gba10"></a>

### Avanza: AI-сводки квартальных отчётов

**Кому и зачем.** Швеция. Быстро понять финансовые результаты компании на странице акции.

**Что внедрено.** Краткие AI-сводки квартальных отчётов в разделе отчётности на странице акции. По инструкции февраля 2026 покрывается большинство компаний, торгующихся в Северной Европе, дальнейшее расширение рынков планируется. [177](https://blogg.avanza.se/6-smarta-verktyg-for-rapportperioden/) [178](https://investors.avanza.se/files/mfn/1980071a-f0cf-4488-a9dc-bff2da7f5f5e/avanza-har-sveriges-nojdaste-sparare-for-16e-aret-i-rad.pdf)

**Статус и доступ.** Работают. В интерфейсе Avanza: страница акции, обзор, раздел отчётов. Отдельная плата за AI-сводки в рассмотренных материалах не указана. Первый запуск или важный этап: 2025: год запуска подтверждён декабрьским релизом. [177](https://blogg.avanza.se/6-smarta-verktyg-for-rapportperioden/) [178](https://investors.avanza.se/files/mfn/1980071a-f0cf-4488-a9dc-bff2da7f5f5e/avanza-har-sveriges-nojdaste-sparare-for-16e-aret-i-rad.pdf)

**Технология и границы.** AI-генерация сводок корпоративной отчётности. Поставщик модели и конкретная LLM не раскрыты в рассмотренных первичных материалах. Подтверждены текстовые сводки. Наличие этой функции не подтверждает LLM в управлении Avanza Auto или автоматическое исполнение торговых решений. [177](https://blogg.avanza.se/6-smarta-verktyg-for-rapportperioden/) [178](https://investors.avanza.se/files/mfn/1980071a-f0cf-4488-a9dc-bff2da7f5f5e/avanza-har-sveriges-nojdaste-sparare-for-16e-aret-i-rad.pdf)


<a name="gba11"></a>

### XTB: аналитический AI-чат в xStation

**Кому и зачем.** Польша, подтверждённый первый клиентский рынок - Чили. Обсудить инструменты, текущий портфель и распределение активов внутри брокерского интерфейса.

**Что внедрено.** Сравнение акций, ETF, валют и других доступных инструментов. Разбор текущего портфеля и предложения распределения активов с учётом профиля клиента. Объяснение финансовых показателей и новостей на базе данных LSEG/Reuters. [179](https://www.xtb.com/cl/blog/asistente-de-inversiones-con-ia) [180](https://www.xtb.com/cl/formacion/guia-chatbot-inversiones-xtb)

**Статус и доступ.** Доступен в Чили, европейское внедрение по использованным первичным источникам не установлено. Бесплатно для клиентов XTB в Чили, в веб-версии и мобильной xStation. Не следует считать наличие чата доказательством такой же доступности клиентам других юридических лиц XTB. Первый запуск или важный этап: Июль–август 2026: релиз 15 июля сообщает о доступности, инструкция 3 августа описывает августовский запуск. [179](https://www.xtb.com/cl/blog/asistente-de-inversiones-con-ia) [180](https://www.xtb.com/cl/formacion/guia-chatbot-inversiones-xtb)

**Технология и границы.** Разговорный AI-анализ с персональным контекстом счёта. Поставщик и версия LLM не раскрыты, источники рыночных данных - LSEG и Reuters. Инструкция оставляет выбор и исполнение сделки за пользователем: после ответа он находит инструмент и сам решает, подавать ли поручение. XTBot для обслуживания клиентов является другим продуктом и не доказывает инвестиционные функции. Точные даты запуска в двух официальных публикациях расходятся. [179](https://www.xtb.com/cl/blog/asistente-de-inversiones-con-ia) [180](https://www.xtb.com/cl/formacion/guia-chatbot-inversiones-xtb)


<a name="asb02"></a>

### Mirae Asset Securities MAPS: AI-сводки и генеративная аналитика

**Кому и зачем.** Южная Корея. Быстрое чтение рынка, новостей компаний и аналитики в брокерском приложении.

**Что внедрено.** Market NOW / AI Market Summary. AI Issue Check. AI Business Summary. AI-генерация черновиков аналитических отчётов, графиков и таблиц с проверкой аналитиком перед публикацией. [209](https://play.google.com/store/apps/details?id=com.miraeasset.trade&hl=en) [210](https://securities.miraeasset.com/newir/view/pc/kr/about/newsView.jsp?seq=571)

**Статус и доступ.** Текущие AI-сервисы перечислены в официальной карточке MAPS, обновлённой 16.10.2026, генеративные отчёты отдельно подтверждены релизом 07.05.2024. Корейское брокерское приложение MAPS (прежнее название M-STOCK), текущая Google Play карточка официального разработчика Mirae Asset Securities. Тариф и индивидуальные права на AI-модули отдельно не раскрыты. Первый запуск или важный этап: 2024-05-07 для первых AI company-analysis reports, дата запуска текущих модулей MAPS не установлена. [209](https://play.google.com/store/apps/details?id=com.miraeasset.trade&hl=en) [210](https://securities.miraeasset.com/newir/view/pc/kr/about/newsView.jsp?seq=571)

**Технология и границы.** AI-сводки в текущем приложении, генеративный AI в подготовке аналитических отчётов подтверждён отдельно. Собственные AI agents в релизе 2024, базовая LLM и версия не раскрыты. Релиз не позволяет автоматически приписать тот же стек каждому модулю MAPS 2026. Текущая карточка приложения подтверждает клиентскую AI-поверхность, но не называет каждый модуль LLM. Старый релиз доказывает GenAI-производство контента с редактурой аналитика. Это не доказательство диалогового автономного трейдера или AI-исполнения ордеров. [209](https://play.google.com/store/apps/details?id=com.miraeasset.trade&hl=en) [210](https://securities.miraeasset.com/newir/view/pc/kr/about/newsView.jsp?seq=571)


<a name="asb03"></a>

### baraka AI

**Кому и зачем.** ОАЭ, ориентирован на розничных инвесторов GCC. Исследование акций, объяснение движений рынка и финансовых тенденций.

**Что внедрено.** Персональный AI investment research assistant. Рыночные сведения и AI insights. Позиционируется как доступный круглосуточно. [211](https://akhbaraka.com/features) [209](https://play.google.com/store/apps/details?id=com.miraeasset.trade&hl=en)

**Статус и доступ.** Текущая исследовательская AI-функция на официальном сайте и в описании приложения, LLM-архитектура публично не подтверждена. Внутри baraka для подходящих клиентов GCC, точный тариф AI и индивидуальная доступность по странам не установлены. Текущая официальная Android-карточка перечисляет BARAKA AI. Первый запуск или важный этап: Дата первого запуска не раскрыта. [211](https://akhbaraka.com/features) [209](https://play.google.com/store/apps/details?id=com.miraeasset.trade&hl=en)

**Технология и границы.** Инвестиционный AI-ассистент, принадлежность к LLM не раскрыта. Провайдер, модель и прямое раскрытие LLM/GenAI не найдены в проверенных первичных страницах. В строгий список подтверждённых LLM не включать: установлен AI-продукт, но не раскрыта его архитектура. Старый поисковый снимок landing упоминал coming soon Android, текущая Google Play карточка уже перечисляет AI. Это подтверждает актуальное описание Android, но не личное тестирование функции или доступность каждому клиенту. AI-исполнение ордеров не подтверждено. [211](https://akhbaraka.com/features) [209](https://play.google.com/store/apps/details?id=com.miraeasset.trade&hl=en)


<a name="asb04"></a>

### Itaú Investment Intelligence / Inteligência de Investimentos Itaú

**Кому и зачем.** Бразилия. Персонализированные инвестиционные вопросы, рекомендации и ограниченные операции в чате.

**Что внедрено.** Диалог об инвестициях и характеристиках продуктов. Рекомендации с учётом профиля и целей. Операции CDB-DI через инвестиционный раздел Super App. Возможность обратиться к человеку-специалисту. [212](https://www.itau.com.br/relacoes-com-investidores/noticias/itau-lanca-agente-de-investimentos-baseado-em-inteligencia-artificial-generativa/?lang=en) [213](https://feito-itau.cloud.itau.com.br/pioneira-ia-do-itau-democratiza-acesso-ao-mundo-dos-investimentos/)

**Статус и доступ.** Запущен 05.06.2025 с постепенным расширением, официальный материал, обновлённый 14.05.2026, сообщает примерно 60 тыс. клиентов. Для выбранных клиентов Itaú в Super App, без отдельной платы за агента. При запуске 10 тыс. клиентов, позднейший официальный материал сообщает около 60 тыс. и расширение в 2026. Всеобщий GA для всей базы на дату среза не подтверждён. Первый запуск или важный этап: 2025-06-05. [212](https://www.itau.com.br/relacoes-com-investidores/noticias/itau-lanca-agente-de-investimentos-baseado-em-inteligencia-artificial-generativa/?lang=en) [213](https://feito-itau.cloud.itau.com.br/pioneira-ia-do-itau-democratiza-acesso-ao-mundo-dos-investimentos/)

**Технология и границы.** Явно заявленный GenAI-агент поверх собственных моделей инвестиционного подбора. GenAI раскрыт, провайдер LLM и версии не раскрыты, инвестиционные рекомендации продолжают опираться на собственные модели и алгоритмы Itaú. CDB-DI - ограниченный класс банковских инвестиционных продуктов, а не универсальное исполнение торговых стратегий. Размер аудитории является заявлением банка в датированном материале, а не измерением на 15.11.2026. Продуктовый подбор банка ограничивает универсальность рекомендаций. [212](https://www.itau.com.br/relacoes-com-investidores/noticias/itau-lanca-agente-de-investimentos-baseado-em-inteligencia-artificial-generativa/?lang=en) [213](https://feito-itau.cloud.itau.com.br/pioneira-ia-do-itau-democratiza-acesso-ao-mundo-dos-investimentos/)


<a name="gbb03"></a>

### CMC Markets: подключение счёта к ChatGPT

**Кому и зачем.** Великобритания. Обсуждать свой CFD-счёт, позиции и рынок в ChatGPT.

**Что внедрено.** Сводка баланса, стоимости счёта, открытых позиций и поручений. Поиск рынков, текущие или отложенные котировки и графики по историческим ценам. [225](https://www.cmcmarkets.com/group/press-releases/cmc-markets-connects-client-accounts-and-market-data-with-chatgpt) [226](https://www.cmcmarkets.com/en-gb/trading-platforms/ai-integrations)

**Статус и доступ.** Запущено для британских CFD-счетов. Официальное приложение CMC Markets в ChatGPT, подключение поддерживаемого британского CFD-счёта. Счета spread betting не поддерживаются, отдельная плата за коннектор в рассмотренных материалах не указана. Первый запуск или важный этап: 2026-09-24. [225](https://www.cmcmarkets.com/group/press-releases/cmc-markets-connects-client-accounts-and-market-data-with-chatgpt) [226](https://www.cmcmarkets.com/en-gb/trading-platforms/ai-integrations)

**Технология и границы.** Внешняя LLM получает брокерские и рыночные данные через официальное подключение. ChatGPT, конкретная версия модели не зафиксирована в документах CMC. Подключение работает только на чтение. Оно не позволяет подавать, изменять или отменять поручения, открывать/закрывать позиции, переводить деньги или менять счёт. Доступность реального времени зависит от разрешений на рыночные данные, возможны цены с задержкой 15 минут. [225](https://www.cmcmarkets.com/group/press-releases/cmc-markets-connects-client-accounts-and-market-data-with-chatgpt) [226](https://www.cmcmarkets.com/en-gb/trading-platforms/ai-integrations)


<a name="gbb04"></a>

### ThinkMarkets ChelseaAI в ThinkTrader

**Кому и зачем.** Международный брокер, правовые условия зависят от юридического лица. Управлять торговыми действиями в разговоре с AI вместо меню терминала.

**Что внедрено.** Просмотр счёта, позиций, рыночных данных и торговой истории. По команде пользователя: рыночные и отложенные поручения, закрытие позиций, изменение stop loss / take profit. [227](https://www.thinkmarkets.com/en/help-centre/ai-trading/) [228](https://www.thinkmarkets.com/getmedia/94e7b202-2e04-460b-8daf-56397a30876a/TM_AI_Supplementary_Terms_UK.pdf?ext=.pdf) [229](https://www.thinkmarkets.com/en/ai-trading/chelsea-ai/)

**Статус и доступ.** По справке доступен на demo и live ThinkTrader, на продуктовой странице также сохранён лист ожидания для доступности на выбранной платформе. Поддерживаемые demo/live счета ThinkTrader. Есть доступ только на чтение и полный доступ, брокер не взимает отдельную плату за ChelseaAI, у внешнего ассистента могут быть свои тарифы. Географию нужно проверять по обслуживающему юридическому лицу. Первый запуск или важный этап: Публичные инструкции и правовые условия: июнь 2026, точная дата первого запуска не установлена. [227](https://www.thinkmarkets.com/en/help-centre/ai-trading/) [228](https://www.thinkmarkets.com/getmedia/94e7b202-2e04-460b-8daf-56397a30876a/TM_AI_Supplementary_Terms_UK.pdf?ext=.pdf) [229](https://www.thinkmarkets.com/en/ai-trading/chelsea-ai/)

**Технология и границы.** Внешние LLM выполняют явно запрошенные операции через официальный MCP-сервер. Открытый MCP-интерфейс: Claude, ChatGPT и другие совместимые ассистенты, конкретную модель выбирает клиент. Не работает автономно, по расписанию или сигналам, не рекомендует сделки и не переводит средства. Британские дополнительные условия прямо требуют проверить и подтвердить каждое поручение перед отправкой. Лист ожидания на продуктовой странице означает, что доступность для всех платформ и клиентов нельзя считать универсальной. [227](https://www.thinkmarkets.com/en/help-centre/ai-trading/) [228](https://www.thinkmarkets.com/getmedia/94e7b202-2e04-460b-8daf-56397a30876a/TM_AI_Supplementary_Terms_UK.pdf?ext=.pdf) [229](https://www.thinkmarkets.com/en/ai-trading/chelsea-ai/)


<a name="rwb02"></a>

### Wealthsimple / Penny и AI integrations

**Кому и зачем.** Канада. Связать финансовую цель с регулярными инвестициями и подтверждаемыми торговыми действиями.

**Что планируется.** Планируются вопросы о диверсификации и действия по финансовой цели. Покупка и продажа акций и ETF, регулярные инвестиции. Отдельное подключение счетов к Claude и ChatGPT. Проверка и подтверждение клиентом перед торговым или денежным действием. [236](https://newsroom.wealthsimple.com/wealthsimple-announces-ai-assistant-penny-and-11-more-releases-at-wealthsimple-presents-something-good-is-going-to-happen) [237](https://www.wealthsimple.com/en-ca/presents/something-good) [238](https://www.wealthsimple.com/en-ca/financial-assistant-notify-me)

**Статус и доступ.** Анонс и список ожидания, запуск планируется в начале 2027. Список ожидания, фактический общий доступ не подтверждён. География канадского финансового сервиса, тариф AI не объявлен. Первый запуск или важный этап: Анонс 5 ноября 2026, продуктовая страница указывает начало 2027. [236](https://newsroom.wealthsimple.com/wealthsimple-announces-ai-assistant-penny-and-11-more-releases-at-wealthsimple-presents-something-good-is-going-to-happen) [237](https://www.wealthsimple.com/en-ca/presents/something-good) [238](https://www.wealthsimple.com/en-ca/financial-assistant-notify-me)

**Технология и границы.** Диалоговый агентный AI, архитектура встроенной модели не раскрыта. Модель Penny неизвестна, отдельно анонсированы внешние подключения Claude и ChatGPT. Ноябрьская презентация не означает запуск перечисленных AI-функций. Страница продукта явно относит помощника и подключения к началу 2027. Выход обычного торгового Wealthsimple Pro в конце 2026 не устанавливает наличие в нём Penny. [236](https://newsroom.wealthsimple.com/wealthsimple-announces-ai-assistant-penny-and-11-more-releases-at-wealthsimple-presents-something-good-is-going-to-happen) [237](https://www.wealthsimple.com/en-ca/presents/something-good) [238](https://www.wealthsimple.com/en-ca/financial-assistant-notify-me)

[Обзор](README.md) | [Мировые брокеры](brokers.md) | [Сервисы](research-services.md) | [Россия](russia.md) | [Терминалы](terminals.md) | [Фонды](funds.md) | [Источники](sources.md)
