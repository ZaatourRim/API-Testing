# API Testing Framework with Pytest and Requests


A simple API testing framework built with *Python*, *Pytest* and *Requests*

This simulates how to automate and structure API test suites:
    Functional tests (GET, POST)
    Performance validation (response time threshold)
    Configurable base URLs and API keys (parametrized via CLI)
    HTTP request/response logging
    Easily Extendable for extra tests (headers and protocol tests)


## Project structure
```bash
API-Testing/
├── conftest.py              # Fixtures, CLI options, and logging setup
├── requirements.txt         # Dependencies
└── tests/
    ├── test_users.py        # GET /users
    ├── test_create_user.py  # POST /users
    └── test_performance.py  # Response time validation
````
## Setup Instructions
### Create and activate a virtual env
```bash
python3 -m venv .venv
source .venv/bin/actvate  # macOS/Linux
.venv\Scripts\activate  # Windows
```
### Install dependencies
```bash
pip install -r requirements.txt
```
### Run all tests
note: run comment in root folder
```bash
pytest -v
````
### CLI arguments
Pytest CLI options make this framework flexible
| Argument | Description | Default |
|-----------|-----------|-----------|
| --base-url | Target API base URL| https://reqres.in/api|
| --api-key  | API key for authentication (x-api-key header)| reqres-free-v1|
|--max-ms|Max response time allowed (ms)|1500|

Example:
```bash
pytest -v -s --max-ms=90
```

# Future enhancements
- Add protocol header validation
- Integrate with GitHub Actions CI
- Add JSON schema validation for responses
- Add PUT and DELETE endpoints





