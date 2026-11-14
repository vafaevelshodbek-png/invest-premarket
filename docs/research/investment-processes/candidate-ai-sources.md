# №22. Основания

Проверено 14 ноября 2026 года. [Выводы](candidate-ai-summary.md) · [Сравнение](candidate-ai-check.md) · [Расходы](candidate-ai-costs.md).

## Материалы проекта

- [Условия №22](https://github.com/vafaevelshodbek-png/invest-premarket/issues/22): четыре класса альтернатив, вклад AI и проверяемое преимущество. Зависимости: №18 и №32.
- [Десять кандидатов №18](https://github.com/vafaevelshodbek-png/invest-premarket/blob/main/docs/research/investment-processes/candidates.md), PR №57.
- [Клиентские сценарии и текущие способы №32](https://github.com/vafaevelshodbek-png/invest-premarket/blob/main/docs/research/investment-processes/current-methods.md), PR №55.
- [Доступность данных №19](https://github.com/vafaevelshodbek-png/invest-premarket/blob/main/docs/research/investment-processes/candidate-data-summary.md), PR №58.

Предыдущая оценка A/B не использовалась. Применимость способов, диапазоны труда и нагрузки являются нашими оценками, источники не доказывают преимущество наших продуктов.

## Внешние основания

<a name="s01"></a>

**S01. [T-Invest MCP](https://developer.tbank.ru/invest/mcp).** Уже заявлены сценарные вопросы, работа со счётом и торговые действия. Это дополнительный соперник К3. Наличие таких функций не устанавливает качество конкретного подключения.

<a name="s02"></a>

**S02. [TradingView: историческая торговля](https://www.tradingview.com/support/solutions/43000691889-learn-to-trade-on-historical-data/).** Воспроизведение рынка и учебные сделки уже существуют. Для К7 отдельно проверяется польза персонального разбора.

<a name="s03"></a>

**S03. [ARQA: алгоритмическая торговля](https://arqatech.com/ru/products/quik/terminals/infrastructure-solutions/algorithmic-trading-module/).** Описаны TWAP, VWAP и различия модулей. Это основание обычных альтернатив К9, доступность нужного алгоритма клиенту проверяется отдельно.

<a name="s04"></a>

**S04. [Hypothesis: stateful testing](https://hypothesis.readthedocs.io/en/latest/stateful.html).** Генерация последовательностей и проверка свойств доступны без LLM. Применение к роботу требует событий, свойств и адаптера, а не только установки библиотеки.

<a name="s05"></a>

**S05. [OR-Tools: целочисленная оптимизация](https://developers.google.com/optimization/mip).** Позволяет моделировать количество единиц и ограничения. Предложенное применение к лотам К13 требует подготовки денежных потоков и постановки задачи.

<a name="s06"></a>

**S06. [TradingView: стратегии](https://www.tradingview.com/pine-script-docs/concepts/strategies/).** Описаны эмуляция исполнения, расходы и ошибки исторического теста. Основание учитывать эти условия у К8, К9 и К14.

<a name="s07"></a>

**S07. [Glasserman и Lin, 2023](https://arxiv.org/abs/2309.17322).** Исследуют смещения исторического анализа финансовых текстов языковой моделью. Для К7 и К8 отсюда выведен риск знания будущих событий, наша модель на нём не проверялась.

<a name="s08"></a>

**S08. [scikit-learn: утечка данных](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage).** Настройка модели и признаков не должна использовать итоговую тестовую выборку. Это относится к будущим проверкам К9 и К14.

<a name="s09"></a>

**S09. [Т-Банк: налоговый отчёт](https://www.tbank.ru/invest/help/educate/broker-report/about/tax-report/).** Описан Excel с листами и таблицами. Это готовая опора обычного импорта К11, полный сбор документов нескольких брокеров требует дополнительного процесса.

<a name="s10"></a>

**S10. [QuantConnect: парная торговля](https://www.quantconnect.com/docs/v2/research-environment/applying-research/pca-and-pairs-trading).** Уже описаны статистические способы оценки связи и построения стратегии. Их результат не переносится на наш рынок автоматически.

<a name="s11"></a>

**S11. [Anthropic: Building effective agents](https://www.anthropic.com/research/building-effective-agents), 19 декабря 2024 года.** Различает заданный процесс и динамический выбор шагов и инструментов моделью. Это основание рассматривать координацию действий как вклад агента. Применимость к нашим сценариям является предложением, выигрыш в сроках и качестве ещё не измерен.

<a name="s12"></a>

**S12. [Тарифы Yandex AI Studio](https://aistudio.yandex.ru/ru/docs/ai-studio/pricing).** Взяты синхронные рублёвые тарифы Alice AI LLM Flash и YandexGPT Pro 5.1 с НДС. Токены, инфраструктура, часы и ставка труда заданы в расчёте как допущения. Тарифы на встроенные инструменты и кеш не переносятся на наши функции.

Часть страниц Т-Банка проверена по официальному поисковому тексту. Источники подтверждают описанные возможности и цены, интеграции и испытания наших кандидатов не выполнялись.
