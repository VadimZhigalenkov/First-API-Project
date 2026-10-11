# First API Automation Project --- Google Maps Training API

## About

An educational Python project focused on REST API test automation. The
test covers the lifecycle of a location in a training API: creating it,
retrieving it, updating its address, and deleting it.

> This is the Rahul Shetty Academy training service that simulates a
> location API, not Google's official public Google Maps API.

## Tech Stack

-   Python
-   Requests --- HTTP request handling
-   Pytest --- test organization and execution
-   Allure Pytest --- test steps and Allure result collection
-   Logging --- recording request and response details

## What Is Tested

The test in `tests/test_google_maps_api.py` runs one end-to-end
scenario:

1.  **POST** --- creates a location and retrieves its `place_id`.
2.  **GET** --- retrieves the location by `place_id` and checks the
    response status, JSON fields, and original address.
3.  **PUT** --- updates the location's address.
4.  **GET** --- verifies that the new address has been saved.
5.  **DELETE** --- deletes the location.
6.  **GET** --- verifies that the deleted location can no longer be
    found (HTTP `404` is expected).

## Project Structure

``` text
First-API-Project/
├── tests/
│   └── test_google_maps_api.py
├── utils/
│   ├── api.py
│   ├── checking.py
│   ├── http_methods.py
│   └── logger.py
├── logs/                 # created when logs are written
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

-   `tests/test_google_maps_api.py` --- the test scenario and
    expected-behavior checks.
-   `utils/api.py` --- API methods for creating, retrieving, updating,
    and deleting locations.
-   `utils/http_methods.py` --- sends HTTP requests using `requests`.
-   `utils/checking.py` --- reusable assertions for status codes, JSON
    fields, and values.
-   `utils/logger.py` --- records request and response information.
-   `pytest.ini` --- Pytest configuration, including adding the project
    root to Python's import path.
-   `requirements.txt` --- Python dependencies.

## How the Test Works

The test calls a method from `Google_maps_api`. That method builds the
URL and request data, then passes the request to `HttpMethods`. The HTTP
client sends it through Requests and returns a Response object. The test
extracts `place_id` from the JSON response and uses it in subsequent
requests. After each operation, assertions from `Cheking` validate the
result.

The responsibilities are separated into the test scenario, API methods,
HTTP client, assertions, and logging.

## Installation and Usage

### 1. Clone the repository

``` bash
git clone https://github.com/VadimZhigalenkov/First-API-Project.git
cd First-API-Project
```

### 2. Create a virtual environment

``` bash
python -m venv .venv
```

Activate it in Windows PowerShell:

``` powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

``` bash
python -m pip install -r requirements.txt
```

### 4. Run the tests

``` bash
python -m pytest
```

### 5. Collect Allure results

``` bash
python -m pytest --alluredir=allure-results
```

To view the report using `allure serve`, Allure Commandline must also be
installed:

``` bash
allure serve allure-results
```

## Skills Practiced

-   REST APIs and `GET`, `POST`, `PUT`, and `DELETE` methods.
-   Sending requests and handling responses with Requests.
-   Validating HTTP status codes and JSON responses.
-   Organizing tests with Pytest.
-   Separating code into logical modules.
-   Logging and Allure integration.

## Author

Vadim Zhigalenkov --- educational project for practicing API test
automation.
