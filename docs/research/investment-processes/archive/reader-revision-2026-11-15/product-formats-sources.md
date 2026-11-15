# №33. Источники и границы выводов

[Обзор](product-formats-summary.md) · [Сравнение форматов](product-formats.md).

Дата подготовки: 14 ноября 2026 года. Источники показывают существующие интерфейсы и условия подключения. Предложенные форматы и удобство для наших пользователей пока являются гипотезами. Пользовательских испытаний не проводилось.

<a name="project-inputs"></a>

## Входные материалы

- [Условия №33](https://github.com/vafaevelshodbek-png/invest-premarket/issues/33): сравнить место работы, форму результата, инициатора, подтверждение, следующий шаг и ограничения перехода.
- [Ситуации №31](https://github.com/vafaevelshodbek-png/invest-premarket/blob/main/docs/research/investment-processes/participant-cases.md) и [разбор №32](https://github.com/vafaevelshodbek-png/invest-premarket/blob/main/docs/research/investment-processes/current-methods.md): 26 историй из согласованной пользователем редакции [PR №55](https://github.com/vafaevelshodbek-png/invest-premarket/pull/55). Материалы приняты в main.
- [Возможности и ограничения №30](https://github.com/vafaevelshodbek-png/invest-premarket/blob/main/docs/research/invest-api/reference.md): границы данных, MCP и учебного контура.
- [Рынки и инструменты №29](https://github.com/vafaevelshodbek-png/invest-premarket/blob/main/docs/research/investment-processes/markets.md): сохранены различия клиентского счёта, портфеля ДУ и операций фонда.

## Клиентские форматы

<a name="f04"></a>

**F04. T-Invest MCP:** [сценарии](https://developer.tbank.ru/invest/mcp), [подключение приложения агента](https://developer.tbank.ru/invest/mcp/agents-connect/coding-agents), [модель взаимодействия MCP](https://modelcontextprotocol.io/specification/2025-06-18/server/tools). Банк описывает подключение к совместимому приложению агента. В спецификации MCP нет обязательного единого интерфейса пользователя. Вывод для формата: подключение инструментов и создание экрана у брокера являются разными работами. Страницы банка повторно проверены по официальному поисковому представлению. Работа подключения командой не проверялась.

<a name="f11"></a>

**F11. [Аналитика портфеля Т-Банка](https://www.tbank.ru/invest/help/educate/yield-analysis/about/folio-lookup/).** Штатные экраны доходности, будущих выплат и структуры служат базой сравнения для №17, №19 и №21. Сложность их использования конкретным человеком неизвестна.

<a name="f12"></a>

**F12. Composer:** [Create with AI](https://help.composer.trade/article/108-create-with-ai), [платформа](https://www.composer.trade/). Диалог связан с визуальным редактором и тестом, отдельно заявлены автоматические сделки. Пример для №24–26. Доступность нужного брокерского подключения не установлена. Сведения о версии модели из статьи 2025 года не использованы.

<a name="f13"></a>

**F13. TradingView:** [Paper Trading](https://www.tradingview.com/support/solutions/43000516466-paper-trading-main-functionality/), [тестирование стратегий](https://www.tradingview.com/pine-script-docs/concepts/strategies/). Примеры учебного торгового экрана и среды проверки стратегии для №23–24. Предлагаемая обратная связь новичку не выдаётся за проверенную функцию этих продуктов.

<a name="f14"></a>

**F14. [Облигации и оферты в справке Т-Банка](https://www.tbank.ru/invest/help/educate/how-it-works/ways-to-invest/bonds-profit/).** Использован разбор из №32: карточка и справка уже дают часть условий выпуска. Сравнение и объяснение нужно проверять относительно этого пути.

<a name="f15"></a>

**F15. Т-Банк:** [покупка и продажа](https://www.tbank.ru/invest/help/brokerage/account/trade-on-bs/buy-n-sell/), [заявки](https://www.tbank.ru/invest/help/brokerage/account/trade-on-bs/bids/). Штатная форма является базой сравнения для №21–22. Собственный экран предварительного расчёта не гарантирует окончательную цену исполнения.

<a name="f16"></a>

**F16. [Вывод денег в Т-Банке](https://www.tbank.ru/invest/help/brokerage/account/trade-on-bs/withdraw-money/).** Для №19 важна доступность денег на конкретном счёте. Общий календарь не заменяет фактическую доступную сумму и условия вывода.

## Основания краткого раздела

Переиспользованы официальные материалы, рассмотренные в №32. Они подтверждают существующие рабочие места, но не возможность встроить туда продукт команды.

<a name="f01"></a>

**F01. [Bloomberg ASKB](https://professional.bloomberg.com/products/bloomberg-terminal/ai/askb/):** пример встроенного помощника для аналитика.

<a name="f02"></a>

**F02. [Aladdin Copilot](https://www.blackrock.com/aladdin/platforms/products/aladdin-copilot):** работа в контексте платформы и прав.

<a name="f05"></a>

**F05. [WEB-кабинет КД НРД](https://www.nsd.ru/workflow/system/programs/web-kabinet-kd/):** электронное взаимодействие по корпоративным действиям.

<a name="f06"></a>

**F06. [Платформа ПИФ НРД](https://www.nsd.ru/faq/156-fz/):** электронная передача заявок в контуре НРД. С 1 марта 2026 года бумажный путь прекращён, при отсутствии электронного взаимодействия НРД отказывает в передаче. Внутренние ручные этапы УК этим источником не подтверждены.

<a name="f07"></a>

**F07. [«1С-Рарус:ПИФ»](https://rarus.ru/1c-upravlenie-nfo-mfo/1c-rarus-pif-2/):** существующее место расчёта и работы с документами фонда.

<a name="f08"></a>

**F08. [SmartCollateral](https://smart.stream/solutions/smart-collateral/):** профессиональное управление обеспечением. Использовано описание продукта вместо прежнего акцента на анонсе MCP.

<a name="f09"></a>

**F09. [Prometheus: оповещения](https://prometheus.io/docs/practices/alerting/):** сигнал является началом реакции, а не полной приёмкой восстановления.

<a name="f10"></a>

**F10. [Электронный мэтчинг НРД](https://www.nsd.ru/services/depozitariy/operatsii-s-tsennymi-bumagami/vnebirzhevye-raschety/elektronnyy-metching/):** действующий канал сообщений об инструкциях.

<a name="f17"></a>

**F17. [QUIK OMS](https://arqatech.com/ru/products/quik/terminals/infrastructure-solutions/oms-manager/):** существующее место управления клиентскими заявками.

<a name="f18"></a>

**F18. [Сравнение по №32](https://github.com/vafaevelshodbek-png/invest-premarket/blob/main/docs/research/investment-processes/current-methods.md):** для кратких историй сохранены входы, разделение ролей и действующие альтернативы. Новый поиск внутренних рабочих мест не проводился.

<a name="f03"></a>

Прежняя ссылка F03 на Morgan Stanley Debrief исключена из обоснования клиентских форматов: итоги встречи советника относятся к другой задаче.
