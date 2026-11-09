# Возможности API и MCP: полный справочник

[Краткий обзор](README.md)

Основа: документальное решение из [№30](https://github.com/vafaevelshodbek-png/invest-premarket/issues/30) от 7 ноября 2026 года. Аудит и дополнения выполнены 9 ноября. Все исходные направления матрицы сохранены. [Исправления и ограничения проверки](maintenance/audit.md) отделены от справочника.

Подтверждение по документации не означает доступ команды к конкретному счёту, наличие нужной истории или успешное выполнение запроса. Названия методов ниже относятся к API, если прямо не указан MCP.

<a name="capabilities"></a>

## Данные и действия

<a name="accounts"></a>

<details>
<summary>Счета и доступные квоты</summary>

| Поле | Содержание |
|---|---|
| Методы или группа | UsersService: GetAccounts, GetUserTariff |
| Данные или действие | Счета пользователя и доступные лимиты |
| Ограничения | Нужны идентифицированный клиент, брокерский счет и действующий токен. Область доступа зависит от токена |
| Основания | [Введение в API](https://developer.tbank.ru/invest/intro/intro), [Токены и права](https://developer.tbank.ru/invest/intro/intro/token), [Тариф и квоты](https://developer.tbank.ru/invest/api/users-service-get-user-tariff), [Счета пользователя](https://developer.tbank.ru/invest/services/accounts/users). По документации |
| Что проверить | Доступные типы счетов и реальные квоты команды. Не проверено |

</details>

<a name="instruments"></a>

<details>
<summary>Поиск и параметры инструментов</summary>

| Поле | Содержание |
|---|---|
| Методы или группа | InstrumentsService: FindInstrument, GetInstrumentBy, Shares, Bonds, Etfs и другие типы |
| Данные или действие | Поиск, идентификаторы, параметры, лотность и свойства инструмента |
| Ограничения | Найденная бумага не обязательно доступна для торговли через API или данному пользователю |
| Основания | [Каталог инструментов](https://developer.tbank.ru/invest/api/instruments-service), [Контракты инструментов](https://developer.tbank.ru/invest/services/instruments/methods), [Доступность инструментов](https://developer.tbank.ru/invest/services/instruments/faq_instruments). По документации |
| Что проверить | api_trade_available_flag, нужный класс инструмента, доступ аккаунта и торговый статус. Не проверено |

</details>

<a name="schedule"></a>

<details>
<summary>Расписание и торговые статусы</summary>

| Поле | Содержание |
|---|---|
| Методы или группа | TradingSchedules и торговые статусы |
| Данные или действие | Календарь площадки и текущая возможность торговать |
| Ограничения | Расписание доступно на неделю вперед, прошлое расписание недоступно. Приостановки требуют проверки текущего статуса |
| Основания | [Особенности справочных данных](https://developer.tbank.ru/invest/services/instruments/head-instruments), [Рыночные данные](https://developer.tbank.ru/invest/services/quotes/marketdata). По документации |
| Что проверить | Календарь нужного рынка и инструмента, поведение при остановке торгов. Не проверено |

</details>

<a name="candles"></a>

<details>
<summary>Исторические свечи</summary>

| Поле | Содержание |
|---|---|
| Методы или группа | MarketDataService: GetCandles |
| Данные или действие | Исторические OHLCV-свечи и время |
| Ограничения | Окно одного запроса и limit зависят от интервала. Общая глубина зависит от инструмента |
| Основания | [Начало истории свечей](https://developer.tbank.ru/invest/services/quotes/faq_marketdata/), [Контракт GetCandles](https://developer.tbank.ru/invest/api/market-data-service-get-candles). По документации |
| Что проверить | Начало истории, пропуски, полнота, завершенность свечи и пригодность для эксперимента. Не проверено |

</details>

<a name="quotes"></a>

<details>
<summary>Текущие цены, стакан, сделки и индикаторы</summary>

| Поле | Содержание |
|---|---|
| Методы или группа | GetLastPrices, GetOrderBook, GetLastTrades, GetTechAnalysis |
| Данные или действие | Последние цены, снимок стакана, сделки, технические индикаторы |
| Ограничения | GetLastTrades гарантирует последний час. Наличие текущего стакана не подтверждает доступ к его историческому архиву |
| Основания | [Рыночные данные](https://developer.tbank.ru/invest/services/quotes/marketdata). По документации |
| Что проверить | Поля, глубина стакана, задержка, поддержка нужного инструмента и история для бэктеста. Не проверено |

</details>

<a name="streams"></a>

<details>
<summary>Обновления рынка и счёта</summary>

| Поле | Содержание |
|---|---|
| Методы или группа | Рыночные потоки и потоки состояния счета |
| Данные или действие | Обновления котировок, позиций, портфеля и заявок |
| Ограничения | Есть квоты подписок и соединений. Данные разных сервисов приходят с разными задержками |
| Основания | [Лимиты](https://developer.tbank.ru/invest/intro/intro/limits), [Операции и потоки](https://developer.tbank.ru/invest/services/operations/methods), [Поручения и предварительные расчёты](https://developer.tbank.ru/invest/services/orders/methods), [Порядок обновления данных](https://developer.tbank.ru/invest/intro/developer/speedup), [WebSocket](https://developer.tbank.ru/invest/intro/developer/protocols/ws). По документации |
| Что проверить | Восстановление соединения, пропуски, порядок событий, частота и задержка. Не проверено |

</details>

<a name="portfolio"></a>

<details>
<summary>Портфель, позиции и остатки</summary>

| Поле | Содержание |
|---|---|
| Методы или группа | OperationsService: GetPortfolio, GetPositions |
| Данные или действие | Состав и оценка портфеля, позиции и остатки |
| Ограничения | Только разрешенные токеном счета. Это текущие данные, а не готовая полная история снимков портфеля |
| Основания | [Токены и права](https://developer.tbank.ru/invest/intro/intro/token), [Операции и потоки](https://developer.tbank.ru/invest/services/operations/methods). По документации |
| Что проверить | Доступные счета, блокировки активов, качество полей и необходимость своего накопления снимков. Не проверено |

</details>

<a name="operations"></a>

<details>
<summary>История операций</summary>

| Поле | Содержание |
|---|---|
| Методы или группа | GetOperationsByCursor |
| Данные или действие | Пагинируемая история операций, фильтры и связанные суммы |
| Ограничения | По умолчанию 100, максимум 1000 операций в странице. ID могут изменяться, корпоративные действия могут нарушать полноту истории |
| Основания | [История операций с пагинацией](https://developer.tbank.ru/invest/api/operations-service-get-operations-by-cursor), [Особенности истории операций](https://developer.tbank.ru/invest/services/operations/operations_problems). По документации |
| Что проверить | Самая ранняя доступная дата, сверка комиссий и выплат, дубли и сопоставление с отчетом. Не проверено |

</details>

<a name="reports"></a>

<details>
<summary>Брокерские отчёты и иностранные доходы</summary>

| Поле | Содержание |
|---|---|
| Методы или группа | GetBrokerReport, GetDividendsForeignIssuer |
| Данные или действие | Брокерский отчет и справка об иностранных доходах |
| Ограничения | Брокерский отчет формируется через задачу и затем читается постранично. Sandbox не предоставляет содержательные реальные отчеты |
| Основания | [Операции и потоки](https://developer.tbank.ru/invest/services/operations/methods), [Различия контуров](https://developer.tbank.ru/invest/intro/developer/sandbox/url_difference), [Контракт брокерского отчёта](https://developer.tbank.ru/invest/api/operations-service-get-broker-report). По документации |
| Что проверить | Нужные поля и период, сроки формирования, доступ конкретного счета. Не проверено |

</details>

<a name="payments"></a>

<details>
<summary>События выплат и отчётности</summary>

| Поле | Содержание |
|---|---|
| Методы или группа | GetDividends, GetBondCoupons, GetAccruedInterests, GetAssetReports |
| Данные или действие | События дивидендов, график купонов, НКД и календарь отчетности |
| Ограничения | Календарь и параметры инструмента не подтверждают фактическое поступление денег конкретному владельцу |
| Основания | [Каталог инструментов](https://developer.tbank.ru/invest/api/instruments-service), [Контракты инструментов](https://developer.tbank.ru/invest/services/instruments/methods). По документации |
| Что проверить | Покрытие бумаг и сопоставление объявленного события с операцией выплаты. Не проверено |

</details>

<a name="news"></a>

<details>
<summary>Новости</summary>

| Поле | Содержание |
|---|---|
| Методы или группа | News |
| Данные или действие | Текущие новости и пагинация |
| Ограничения | История ограничена 24 часами. Архив для исторического теста отдельно не подтвержден |
| Основания | [Особенности справочных данных](https://developer.tbank.ru/invest/services/instruments/head-instruments). По документации |
| Что проверить | Состав источников, поля и объем доступного текста, сопоставление с эмитентом, условия сохранения. Не проверено |

</details>

<a name="fundamentals"></a>

<details>
<summary>Фундаментальные показатели</summary>

| Поле | Содержание |
|---|---|
| Методы или группа | GetAssetFundamentals |
| Данные или действие | Фундаментальные показатели компании |
| Ограничения | Не все активы покрыты. Ноль трактуется как отсутствие, обновление может запаздывать |
| Основания | [Особенности справочных данных](https://developer.tbank.ru/invest/services/instruments/head-instruments). По документации |
| Что проверить | Нужные показатели и периоды, точная дата публикации, сравнимость и полнота. Не проверено |

</details>

<a name="forecasts"></a>

<details>
<summary>Прогнозы аналитиков</summary>

| Поле | Содержание |
|---|---|
| Методы или группа | GetConsensusForecasts |
| Данные или действие | Мнения аналитиков по инструменту |
| Ограничения | Наличие метода не подтверждает наличие исторических версий прогнозов, нужных для честного ретротеста |
| Основания | [Каталог инструментов](https://developer.tbank.ru/invest/api/instruments-service). По документации для метода, не проверено для исторического покрытия |
| Что проверить | Поля ответа, авторы, даты, старые версии и покрытие инструментов. Не проверено |

</details>

<a name="orders"></a>

<details>
<summary>Торговые поручения</summary>

| Поле | Содержание |
|---|---|
| Методы или группа | OrdersService: PostOrder, CancelOrder, ReplaceOrder, GetOrderState, GetOrders |
| Данные или действие | Выставление, отмена, замена и контроль заявок |
| Ограничения | Изменяющие операции требуют соответствующих прав. Ответ о принятии не равен полному исполнению |
| Основания | [Токены и права](https://developer.tbank.ru/invest/intro/intro/token), [Поручения и предварительные расчёты](https://developer.tbank.ru/invest/services/orders/methods). По документации |
| Что проверить | Поддержка типов поручений, отказы, частичное исполнение и защита от повторной отправки. Не проверено |

</details>

<a name="order-estimate"></a>

<details>
<summary>Предварительная стоимость и доступные лоты</summary>

| Поле | Содержание |
|---|---|
| Методы или группа | GetOrderPrice, GetMaxLots |
| Данные или действие | Предварительная стоимость лимитной заявки, комиссии и доступное число лотов |
| Ограничения | Это предварительный расчет при текущих данных и состоянии счета. Условия могут измениться до исполнения |
| Основания | [Поручения и предварительные расчёты](https://developer.tbank.ru/invest/services/orders/methods). По документации |
| Что проверить | НКД, валюта, лотность, комиссии, обеспечение и свежесть расчета. Не проверено |

</details>

<a name="stop-orders"></a>

<details>
<summary>Стоп-заявки</summary>

| Поле | Содержание |
|---|---|
| Методы или группа | StopOrdersService: PostStopOrder, GetStopOrders, CancelStopOrder |
| Данные или действие | Стоп-заявки и управление ими |
| Ограничения | Нужны права, подходящий инструмент и корректные параметры. Стоп-условие не гарантирует цену исполнения |
| Основания | [Стоп-заявки](https://developer.tbank.ru/invest/services/stop-orders/stoporders). По документации |
| Что проверить | Поддерживаемый тип, время действия, состояние и поведение при изменении рынка. Не проверено |

</details>

<a name="sandbox"></a>

<details>
<summary>Песочница</summary>

| Поле | Содержание |
|---|---|
| Методы или группа | SandboxService: OpenSandboxAccount, SandboxPayIn, GetSandboxPortfolio, PostSandboxOrder и другие |
| Данные или действие | Виртуальный счет, тестовые средства и обработка поручений |
| Ограничения | Поведение отличается от prod, часть отчетов и выплат отсутствует. Успех в sandbox не доказывает prod-доступ |
| Основания | [Поведение песочницы](https://developer.tbank.ru/invest/intro/developer/sandbox), [Различия контуров](https://developer.tbank.ru/invest/intro/developer/sandbox/url_difference), [Методы песочницы](https://developer.tbank.ru/invest/api/sandbox-service). По документации |
| Что проверить | Ограничения конкретного метода и текущей версии. Не проверено |

</details>

<a name="mcp"></a>

<details>
<summary>Инструменты MCP</summary>

| Поле | Содержание |
|---|---|
| Методы или группа | T-Invest MCP |
| Данные или действие | Доступ агента к документированным группам данных и операций |
| Ограничения | Нужны MCP-клиент, токен, доверие к TLS и совместимая с инструментами модель. Полный актуальный manifest нами не получен |
| Основания | [Документация MCP](https://developer.tbank.ru/invest/mcp), [Пример разработчика MCP](https://habr.com/ru/companies/tbank/articles/1086714/). По документации для описанных групп, не проверено для набора tools |
| Что проверить | tools/list, реальные имена, схемы, права, размер ответов, квоты и доступ в выбранном контуре. Не проверено |

</details>

<a name="archives"></a>

<details>
<summary>Файловые архивы сделок и минутных свечей</summary>

| Поле | Содержание |
|---|---|
| Источник | [Файловые исторические архивы](https://developer.tbank.ru/invest/services/history-md/head-history-md) |
| Данные | Дневные архивы обезличенных сделок по всем либо отдельному инструменту и годовые архивы минутных свечей |
| Формат | CSV внутри архивов. У свечей и сделок разные схемы, у минутных свечей нет строки заголовков |
| Ограничения | Покрытие неполное и начинается в разные даты. Для скачивания указано не более 30 файлов в минуту с одного IP |
| Что проверить | Наличие нужных инструментов и дней, поля и единицы, пропуски, разрешённое использование. Архив сделок не является архивом стакана |

</details>

## Подключение, форматы и обновление данных

**API.** Доступны gRPC, gRPC-web, REST и WebSocket. gRPC использует protobuf-контракты, REST и WebSocket предоставляют JSON-представление. REST-прокси не подменяет потоковую подписку, для событий выбирается поддерживаемый потоковый транспорт. [Протоколы подключения](https://developer.tbank.ru/invest/intro/developer/protocols/), [WebSocket](https://developer.tbank.ru/invest/intro/developer/protocols/ws)

| Контур | gRPC | REST | MCP |
|---|---|---|---|
| Реальный | invest-public-api.tbank.ru:443 | https://invest-public-api.tbank.ru/rest/ | https://invest-public-api.tbank.ru/mcp |
| Песочница | sandbox-invest-public-api.tbank.ru:443 | https://sandbox-invest-public-api.tbank.ru/rest/ | https://sandbox-invest-public-api.tbank.ru/mcp |

Адреса подтверждены [Протоколы подключения](https://developer.tbank.ru/invest/intro/developer/protocols/), [Документация MCP](https://developer.tbank.ru/invest/mcp), [Пример разработчика MCP](https://habr.com/ru/companies/tbank/articles/1086714/). В этом исследовании к ним не подключались.

**Денежные значения.** [Денежные типы данных](https://developer.tbank.ru/invest/intro/intro/faq_custom_types) поясняет MoneyValue с валютой и Quotation без валюты, с частями units и nano. В JSON int64-поля могут передаваться строками. Даты запрашиваемых периодов задаются по UTC. Конвертацию типов и проверку единиц нужно делать в коде. [Контракт GetCandles](https://developer.tbank.ru/invest/api/market-data-service-get-candles), [История операций с пагинацией](https://developer.tbank.ru/invest/api/operations-service-get-operations-by-cursor), [Контракты инструментов](https://developer.tbank.ru/invest/services/instruments/methods)

**История свечей.** Периоды и количество свечей ниже относятся к одному запросу. Это не глубина истории каждого инструмента. Полная таблица интервалов дополнена по странице загрузки исторических котировок. [Контракт GetCandles](https://developer.tbank.ru/invest/api/market-data-service-get-candles), [Периоды запросов исторических свечей](https://developer.tbank.ru/invest/intro/intro/load_history)

| Интервал | Максимальный период запроса | Максимальное число свечей |
|---|---|---|
| 5 секунд | 200 минут | 2500 |
| 10 секунд | 200 минут | 1250 |
| 30 секунд | 20 часов | 2500 |
| 1 минута | 1 день | 2400 |
| 2 минуты | 1 день | 1200 |
| 3 минуты | 1 день | 750 |
| 5 минут | 1 неделя | 2400 |
| 10 минут | 1 неделя | 1200 |
| 15 минут | 3 недели | 2400 |
| 30 минут | 3 недели | 1200 |
| 1 час | 3 месяца | 2400 |
| 2 часа | 3 месяца | 2400 |
| 4 часа | 3 месяца | 700 |
| 1 день | 6 лет | 2400 |
| 1 неделя | 5 лет | 300 |
| 1 месяц | 10 лет | 120 |

Секундные свечи доступны только за последний месяц. Для больших выгрузок отдельно предусмотрены файловые архивы сделок и минутных свечей. [Файловые исторические архивы](https://developer.tbank.ru/invest/services/history-md/head-history-md), [Периоды запросов исторических свечей](https://developer.tbank.ru/invest/intro/intro/load_history)

Контракт также описывает другие интервалы. Даты начала минутной и дневной истории можно определить по first_1min_candle_date и first_1day_candle_date в справочнике. Длинный период может потребовать нескольких запросов и проверки пропусков. [Начало истории свечей](https://developer.tbank.ru/invest/services/quotes/faq_marketdata/), [Контракт GetCandles](https://developer.tbank.ru/invest/api/market-data-service-get-candles)

Для истории операций предпочтителен GetOperationsByCursor. Старый GetOperations возвращает только последнюю тысячу операций, поэтому его нельзя считать полной исторической выгрузкой. [FAQ по операциям](https://developer.tbank.ru/invest/services/operations/faq_operations)

**Обновление.** Новости читаются постранично внутри доступного окна. Портфель и заявки можно получать запросами или потоками. Для точного наблюдения исполнения предпочтителен OrderStateStream, история операций приходит позднее. Сервисы не следует считать единым атомарным снимком. [Особенности справочных данных](https://developer.tbank.ru/invest/services/instruments/head-instruments), [Операции и потоки](https://developer.tbank.ru/invest/services/operations/methods), [Поручения и предварительные расчёты](https://developer.tbank.ru/invest/services/orders/methods), [Порядок обновления данных](https://developer.tbank.ru/invest/intro/developer/speedup)

Полный архив новостей, исторических стаканов и всех старых прогнозов для point-in-time теста этим исследованием не подтвержден. Их доступность проверяется отдельно под кандидата в #19. Это неизвестность, а не утверждение об отсутствии таких данных у Банка.

<a name="limits"></a>

## Лимиты и частота

Лимиты динамические и действуют совместно для счетов пользователя. Ниже указаны номинальные значения групп, используемых в матрице, на дату проверки. Отдельные методы имеют исключения. [Лимиты](https://developer.tbank.ru/invest/intro/intro/limits), [Тариф и квоты](https://developer.tbank.ru/invest/api/users-service-get-user-tariff)

| Группа | Запросов в минуту |
|---|---|
| Котировки | 600 |
| Инструменты | 200 |
| Каталоги Bonds, Shares, Options, Futures, Etfs, GetAssets | 15 |
| Счета | 100 |
| Операции | 200 |
| Формирование отчётов через gRPC | 5 |
| Поручения | 100 |
| Стоп-заявки | 50 |
| Песочница | 200 |

Например, для GetOrders указано 200 запросов в минуту, PostOrder 15 в секунду, CancelOrder и ReplaceOrder по 300 в минуту. Общую строку сервиса нельзя автоматически применять к каждому методу. [Лимиты](https://developer.tbank.ru/invest/intro/intro/limits)

Для котировок указаны 32 соединения и 300 подписок на свечи, стаканы и сделки суммарно в одном соединении, для изменения подписок 100 запросов в минуту. Для поручений указаны 16 соединений на тип, для операций 11. Интервал отправки свечей и стакана 100 мс является ограничением доставки, а не измеренной задержкой системы. [Лимиты](https://developer.tbank.ru/invest/intro/intro/limits)

Есть также ограничения по IP. Страница рекомендует не превышать 50 запросов в секунду суммарно с адреса. Текущие квоты уточняются через GetUserTariff и заголовки ответа. Лимиты MCP и число серверных обращений на один вызов инструмента не установлены. [Лимиты](https://developer.tbank.ru/invest/intro/intro/limits), [Тариф и квоты](https://developer.tbank.ru/invest/api/users-service-get-user-tariff)

## Доступ и безопасность

- Нужны брокерский счет, идентификация и действующий токен. Данные API названы бесплатными в вводной документации, но это не отменяет расходов на торговые операции, облака, хранение и LLM. [Введение в API](https://developer.tbank.ru/invest/intro/intro)
- Read-only предназначен для получения информации и не разрешает выставление торговых поручений. Full-access дает торговые возможности. Transfer-access дополнительно относится к переводам. Можно ограничить доступ одним счетом, кроме оговоренных в документации типов счетов. Sandbox использует свой вид токена. [Токены и права](https://developer.tbank.ru/invest/intro/intro/token)
- Токен сохраняется при выпуске. В документации указан срок три месяца с последнего использования и необходимость первого использования в течение семи дней. Порядок отзыва и перевыпуска нужно учитывать при проверке доступа. [Токены и права](https://developer.tbank.ru/invest/intro/intro/token)
- Для MCP в примере используется Authorization: Bearer и Streamable HTTP. В документации подключения указаны сертификаты НУЦ Минцифры РФ. Доверие к ним проверяется в окружении клиента, обход проверки TLS не является решением ошибки подключения. [Сертификаты и подключение](https://developer.tbank.ru/invest/intro/developer/network), [Пример разработчика MCP](https://habr.com/ru/companies/tbank/articles/1086714/)
- Секреты хранятся вне репозитория и текста запросов к модели. Торговый токен способен разрешить действия без отдельного диалога с человеком. Подтверждение, лимиты и журнал действий реализуются в клиенте. В статье приведено хранение секретов в окружении или credentials и подтверждение через Telegram. [Пример разработчика MCP](https://habr.com/ru/companies/tbank/articles/1086714/)
- Документацию T-API для бизнеса нельзя использовать как доказательство правил T-Invest. В частности, схемы авторизации и тестового доступа разных продуктов не взаимозаменяемы. Используем источники в разделе /invest/. [Протоколы подключения](https://developer.tbank.ru/invest/intro/developer/protocols/), [Токены и права](https://developer.tbank.ru/invest/intro/intro/token), [Сертификаты и подключение](https://developer.tbank.ru/invest/intro/developer/network)

Рекомендации команды для следующей проверки: минимальные права, явный выбор sandbox, разрешенный перечень инструментов агента, маскирование данных в логах, таймауты и проверки денежных значений кодом. Веб-страницы и новости считать входными данными, не инструкциями для агента. Это предлагаемые меры продукта, а не проверенные здесь встроенные гарантии MCP. Спецификация MCP предусматривает проверку входов и контроля доступа, а для чувствительных действий рекомендует подтверждение пользователем. [Спецификация MCP](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)

<a name="sandbox-details"></a>

## Песочница: что именно можно и нельзя заключить

Документированы виртуальные счета, пополнение и операции с поручениями. Они отделены от реальных счетов. Для проверки интеграции доступны также sandbox-методы стоп-заявок. [Поведение песочницы](https://developer.tbank.ru/invest/intro/developer/sandbox), [Методы песочницы](https://developer.tbank.ru/invest/api/sandbox-service)

Общая страница указывает: [Поведение песочницы](https://developer.tbank.ru/invest/intro/developer/sandbox)

- дивиденды и купоны на счет не начисляются, налоги не рассчитываются
- комиссия упрощена до 0,05% от сделки
- рыночное исполнение привязано к последней цене, заявки не воздействуют на рынок
- часть показателей портфеля и рисков не рассчитывается или упрощена

Таблица различий контуров отдельно исключает содержательные GetBrokerReport и GetDividendsForeignIssuer. Следовательно, sandbox не заменяет источник для проверки реальных налоговых отчетов и учета выплат. [Различия контуров](https://developer.tbank.ru/invest/intro/developer/sandbox/url_difference)

**Расхождение документации.** Общая страница описывает упрощенное плечо и отдельные нулевые маржинальные показатели. При этом релиз 1.51 сообщает о расчете вариационной маржи, корректировке доступных лотов и запрете маржинальной торговли по некоторым инструментам. Реальную модель текущего sandbox по этим параметрам считать неизвестной до проверки конкретного инструмента. [Поведение песочницы](https://developer.tbank.ru/invest/intro/developer/sandbox), [Релиз 1.51 на дату проверки](https://developer.tbank.ru/invest/release/latest)

Для первого отбора это означает, что sandbox обосновывает возможность технического теста. Он не доказывает экономический результат стратегии, доступность инструмента на реальном счете и качество исполнения при ограниченной ликвидности.

## Собственные модели, облака и внешние API

Поле 8 первого отбора разрешает собственные модели, облака и API. В поле 7 описывается предполагаемая архитектура, дополнительный прототип не обязателен. Поэтому на SIGNAL IN достаточно обоснованного доступного контура и плана проверки, развертывание инфраструктуры для этой задачи не требуется. Источник требований - переданный текст формы, сохраненный в Wiki, а не самостоятельно выведенное условие. [Текст первого отбора](https://github.com/vafaevelshodbek-png/invest-premarket/wiki/Hackathon#требования-первого-отбора)

Python и другие языки с SDK перечислены в документации API. Наличие SDK не заменяет проверку совместимости актуального контракта и сетевого окружения. [Введение в API](https://developer.tbank.ru/invest/intro/intro), [Сертификаты и подключение](https://developer.tbank.ru/invest/intro/developer/network)

Для будущего MVP отдельно проверить: доступность выбранного LLM-провайдера для команды, стоимость и задержки, обработку передаваемых данных и права на используемые модели, датасеты и компоненты. Разрешение облаков не подтверждает право передавать или распространять любые данные и компоненты. FAQ T-Invest API указывает, что сервис предоставляется клиентам без права на ретрансляцию данных. Допустимость конкретного публичного продукта и внешней обработки остаётся отдельной проверкой. [Ограничения использования API](https://developer.tbank.ru/invest/intro/faq)

Ссылка на правила программы сохранена, но текущая редакция PDF при аудите не получена. Условия о правах и зависимостях нельзя считать повторно проверенными по одной этой ссылке. Для решения нужен применимый текст правил. [Правила программы](https://cdn.tbank.ru/static/documents/promo-invest-premarket.pdf)

<a name="handoff"></a>

## Непроверенные условия и передача в №19

Следующие пункты являются **планом**, их выполнение не заявляется:

| Проверка | Какое подтверждение требуется | Значение для выбора кандидата |
|---|---|---|
| Доступ команды | Права и область действия sandbox/read-only токена без публикации секрета | Отделить доступный источник от документированного |
| MCP manifest | tools/list со всеми страницами, именами и схемами, затем только безопасные read-only вызовы | Не выдумывать tool и его аргументы, проверить набор после подключения [Спецификация MCP](https://modelcontextprotocol.io/specification/2025-06-18/server/tools) |
| Данные выбранных бумаг | Небольшие обезличенные ответы, начало истории, пропуски, даты публикации и обновления | Определить полноту и пригодность данных |
| Соответствие sandbox задаче | Таблица нужных полей и отказов против реального требования | Исключить ложную проверку налогов, выплат и исполнимости |
| Нагрузка | Квоты, задержка, размер ответов, поведение при ошибках и переподключении | Проверить выполнимость частоты обновления |
| Условия использования | Разрешения на хранение, передачу облаку и распространение нужных данных и компонентов | Установить ограничения конкретного продукта |

Готово для [#19](https://github.com/vafaevelshodbek-png/invest-premarket/issues/19): для каждого кандидата выбрать нужные строки матрицы и присвоить доступность «доступно», «условно доступно» или «неизвестно». Новостной ретротест, учет реальных налогов/выплат в sandbox, восстановление исторического стакана и предположение о полном совпадении API с MCP требуют отдельного основания. Идея и архитектура этой работой не выбирались.

## Источники

Ссылки исходного решения сохранены полностью. Проверка опирается на доступный текст первоисточников и индексированные копии официального портала. Прямое получение части страниц ограничено проверкой сертификата. Полнота повторного чтения и недоступная редакция правил указаны в [аудите](maintenance/audit.md).

- [Введение в API](https://developer.tbank.ru/invest/intro/intro).
- [Протоколы подключения](https://developer.tbank.ru/invest/intro/developer/protocols/).
- [Токены и права](https://developer.tbank.ru/invest/intro/intro/token).
- [Сертификаты и подключение](https://developer.tbank.ru/invest/intro/developer/network).
- [Лимиты](https://developer.tbank.ru/invest/intro/intro/limits).
- [Тариф и квоты](https://developer.tbank.ru/invest/api/users-service-get-user-tariff).
- [Каталог инструментов](https://developer.tbank.ru/invest/api/instruments-service).
- [Особенности справочных данных](https://developer.tbank.ru/invest/services/instruments/head-instruments).
- [Начало истории свечей](https://developer.tbank.ru/invest/services/quotes/faq_marketdata/).
- [Контракт GetCandles](https://developer.tbank.ru/invest/api/market-data-service-get-candles).
- [Рыночные данные](https://developer.tbank.ru/invest/services/quotes/marketdata).
- [Операции и потоки](https://developer.tbank.ru/invest/services/operations/methods).
- [История операций с пагинацией](https://developer.tbank.ru/invest/api/operations-service-get-operations-by-cursor).
- [Особенности истории операций](https://developer.tbank.ru/invest/services/operations/operations_problems).
- [Поручения и предварительные расчёты](https://developer.tbank.ru/invest/services/orders/methods).
- [Стоп-заявки](https://developer.tbank.ru/invest/services/stop-orders/stoporders).
- [Поведение песочницы](https://developer.tbank.ru/invest/intro/developer/sandbox).
- [Различия контуров](https://developer.tbank.ru/invest/intro/developer/sandbox/url_difference).
- [Методы песочницы](https://developer.tbank.ru/invest/api/sandbox-service).
- [Релиз 1.51 на дату проверки](https://developer.tbank.ru/invest/release/latest).
- [Документация MCP](https://developer.tbank.ru/invest/mcp).
- [Пример разработчика MCP](https://habr.com/ru/companies/tbank/articles/1086714/).
- [Контракты инструментов](https://developer.tbank.ru/invest/services/instruments/methods).
- [Спецификация MCP](https://modelcontextprotocol.io/specification/2025-06-18/server/tools).
- [Текст первого отбора](https://github.com/vafaevelshodbek-png/invest-premarket/wiki/Hackathon#требования-первого-отбора).
- [Правила программы](https://cdn.tbank.ru/static/documents/promo-invest-premarket.pdf).
- [Порядок обновления данных](https://developer.tbank.ru/invest/intro/developer/speedup).
- [FAQ по операциям](https://developer.tbank.ru/invest/services/operations/faq_operations).
- [Контракт брокерского отчёта](https://developer.tbank.ru/invest/api/operations-service-get-broker-report).
- [Счета пользователя](https://developer.tbank.ru/invest/services/accounts/users).
- [Доступность инструментов](https://developer.tbank.ru/invest/services/instruments/faq_instruments).
- [WebSocket](https://developer.tbank.ru/invest/intro/developer/protocols/ws).
- [Файловые исторические архивы](https://developer.tbank.ru/invest/services/history-md/head-history-md).
- [Ограничения использования API](https://developer.tbank.ru/invest/intro/faq).
- [Периоды запросов исторических свечей](https://developer.tbank.ru/invest/intro/intro/load_history).
- [Денежные типы данных](https://developer.tbank.ru/invest/intro/intro/faq_custom_types).

[Исходный текст задачи и решения](maintenance/archive/issue-30-2026-11-09.md)
