# Продукт A: изменения раскрытия и модель аналитика

**Статус выбора: предложен, ждёт подтверждения команды в [№2](https://github.com/vafaevelshodbek-png/invest-premarket/issues/2).** Предложение внёс участник команды 10 ноября 2026 года. Материалы ниже подготовлены под этот выбор заранее, чтобы успеть к сроку подачи. Если команда выберет другой вариант, их нужно пересмотреть.

## Выбор

**Пользователь и задача.** Аналитик эмитента в управляющей компании после выхода нового отчёта эмитента находит изменения относительно прошлой версии, связывает их с предпосылками своей модели оценки и передаёт управляющему проверенную записку.

**Почему A, а не B.** Сравнение основано на [кандидатах №18](../research/investment-processes/candidates-summary.md), [проверке данных №19](../research/investment-processes/candidate-data-check.md) и [сравнении роли AI №22](../research/investment-processes/candidate-ai-check.md).

| Критерий | A. Раскрытие и модель аналитика | B. Расхождение учёта брокера |
|---|---|---|
| Данные для первой проверки | Публичные отчёты доступны, пример «Норникеля» за 2023 и 2024 годы прочитан | Внутренние выгрузки, первичные документы и закрытый случай недоступны |
| Задача для AI | Смысловая связь изменения с предпосылкой при разных формулировках остаётся гипотезой, которую можно проверить | После правил, соединения таблиц и действующего модуля задача для AI не установлена |
| Проверяемость на этапе заявки | Эксперимент можно спланировать на публичных парах отчётов | Возможна только синтетика, которая не проверяет причину расхождения |

**Причины отказа от B.** Нет доступа к данным и не показана работа, которую нельзя закрыть правилами и кодом. Вернуться к B можно, если появится партнёр-брокер с закрытым случаем.

**Что выбор не доказывает.** Спрос аналитиков, доступ к моделям УК и преимущество AI над обычным способом не подтверждены. Это вынесено в [риски](evaluation.md#risks) и [первый эксперимент](evaluation.md#experiment).

## Где что лежит

| Задача | Результат |
|---|---|
| [№4](https://github.com/vafaevelshodbek-png/invest-premarket/issues/4) Продукт и изменение | [Описание продукта](product.md#idea) |
| [№20](https://github.com/vafaevelshodbek-png/invest-premarket/issues/20) Обоснованность ценности | [Основания и допущения](product.md#grounds) |
| [№21](https://github.com/vafaevelshodbek-png/invest-premarket/issues/21) Вход, результат, границы | [Паспорт сценария](product.md#passport) |
| [№34](https://github.com/vafaevelshodbek-png/invest-premarket/issues/34) Шаги и отказы | [Шаги сценария](product.md#steps) |
| [№37](https://github.com/vafaevelshodbek-png/invest-premarket/issues/37) Востребованность и встраивание | [Бизнес-риски](product.md#business-risks) |
| [№3](https://github.com/vafaevelshodbek-png/invest-premarket/issues/3) Данные | [Спецификация данных](system.md#data) |
| [№23](https://github.com/vafaevelshodbek-png/invest-premarket/issues/23) AI-подходы и модели | [Подходы и модели](system.md#models) |
| [№24](https://github.com/vafaevelshodbek-png/invest-premarket/issues/24) Техническая схема | [Схема MVP](system.md#architecture) |
| [№35](https://github.com/vafaevelshodbek-png/invest-premarket/issues/35) Стоимость и осуществимость | [Оценка стоимости](system.md#cost) |
| [№36](https://github.com/vafaevelshodbek-png/invest-premarket/issues/36) Базовый способ и примеры | [Базовый способ и набор](evaluation.md#baseline) |
| [№25](https://github.com/vafaevelshodbek-png/invest-premarket/issues/25) Первый эксперимент | [Протокол](evaluation.md#experiment) |
| [№26](https://github.com/vafaevelshodbek-png/invest-premarket/issues/26) Стоп-факторы | [Риски](evaluation.md#risks) |
| [№38](https://github.com/vafaevelshodbek-png/invest-premarket/issues/38) Сборка ответов | [Черновик заявки](application.md) |

Перекрёстную проверку ([№28](https://github.com/vafaevelshodbek-png/invest-premarket/issues/28)) и отправку ([№5](https://github.com/vafaevelshodbek-png/invest-premarket/issues/5)) выполняют участники команды. Требования DoD о проверке финансовым или другим техническим профилем этими материалами не закрыты.

## Открытые вопросы

1. Подтверждает ли команда выбор A.
2. Кто из бизнес-профилей проверит смысл предпосылок и эталонных связей.
3. Удастся ли до подачи поговорить хотя бы с одним аналитиком УК. Если нет, это прямо указывается в поле 3.
