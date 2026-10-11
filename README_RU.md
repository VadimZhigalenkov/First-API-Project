# First API Automation Project --- Google Maps Training API

## О проекте

Учебный проект по автоматизации тестирования REST API на Python. Тест
проверяет жизненный цикл локации в учебном API: создание, получение,
изменение адреса и удаление.

> Это учебный сервис Rahul Shetty Academy, имитирующий API для работы с
> локациями, а не официальный публичный API Google Maps.

## Технологии

-   Python
-   Requests --- отправка HTTP-запросов
-   Pytest --- организация и запуск тестов
-   Allure Pytest --- шаги и сбор результатов для отчётов Allure
-   Logging --- запись запросов и ответов в файл

## Что проверяется

Тест `tests/test_google_maps_api.py` выполняет один сквозной сценарий:

1.  **POST** --- создаёт локацию и получает `place_id`.
2.  **GET** --- получает локацию по `place_id`, проверяет статус ответа,
    поля JSON и исходный адрес.
3.  **PUT** --- меняет адрес локации.
4.  **GET** --- проверяет, что новый адрес сохранён.
5.  **DELETE** --- удаляет локацию.
6.  **GET** --- проверяет, что удалённая локация больше не найдена
    (ожидается HTTP `404`).

## Структура проекта

``` text
First-API-Project/
├── tests/
│   └── test_google_maps_api.py
├── utils/
│   ├── api.py
│   ├── checking.py
│   ├── http_methods.py
│   └── logger.py
├── logs/                 # создаётся при записи логов
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

-   `tests/test_google_maps_api.py` --- сценарий тестирования и проверки
    ожидаемого поведения.
-   `utils/api.py` --- методы, соответствующие операциям API: создание,
    получение, изменение и удаление локации.
-   `utils/http_methods.py` --- отправка HTTP-запросов с помощью
    `requests`.
-   `utils/checking.py` --- повторно используемые проверки статус-кодов,
    JSON-полей и значений.
-   `utils/logger.py` --- запись информации о запросах и ответах.
-   `pytest.ini` --- конфигурация Pytest, в том числе добавление корня
    проекта в Python path.
-   `requirements.txt` --- Python-зависимости.

## Как работает тест

Тест вызывает метод из `Google_maps_api`. Тот формирует URL и данные
запроса и передаёт их в `HttpMethods`. HTTP-клиент отправляет запрос
через Requests и возвращает объект Response. Тест извлекает `place_id`
из JSON-ответа и использует его в следующих запросах. После каждой
операции вызываются проверки из `Cheking`.

Таким образом, обязанности разделены на сценарий, методы API,
HTTP-клиент, проверки и логирование.

## Установка и запуск

### 1. Клонировать репозиторий

``` bash
git clone https://github.com/VadimZhigalenkov/First-API-Project.git
cd First-API-Project
```

### 2. Создать виртуальное окружение

``` bash
python -m venv .venv
```

Активировать в Windows PowerShell:

``` powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Установить зависимости

``` bash
python -m pip install -r requirements.txt
```

### 4. Запустить тесты

``` bash
python -m pytest
```

### 5. Собрать результаты Allure

``` bash
python -m pytest --alluredir=allure-results
```

Для просмотра отчёта через `allure serve` дополнительно требуется
установленный Allure Commandline:

``` bash
allure serve allure-results
```

## Навыки, которые практиковались

-   REST API и HTTP-методы `GET`, `POST`, `PUT`, `DELETE`.
-   Отправка запросов и обработка ответов с Requests.
-   Проверка HTTP-статусов и JSON-ответов.
-   Организация теста с Pytest.
-   Разделение кода на логические модули.
-   Логирование и интеграция Allure.

## Автор

Вадим Жигаленков --- учебный проект для практики API test automation.
