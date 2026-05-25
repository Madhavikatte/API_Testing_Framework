# 🔌 API Testing Framework

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Pytest](https://img.shields.io/badge/Tested%20with-Pytest-yellow?logo=pytest)
![Requests](https://img.shields.io/badge/Library-Requests-orange)
![API](https://img.shields.io/badge/API-REST-green)
![CI](https://github.com/Madhavikatte/API_Testing_Framework/actions/workflows/pytest.yml/badge.svg)
![Status](https://img.shields.io/badge/Tests-25%20Passing-brightgreen)

A REST API test automation framework built using **Python**, **Pytest**, and the **Requests** library — covering CRUD operations, authentication flows, and negative test scenarios against the [ReqRes REST API](https://reqres.in).

---

## 📋 Table of Contents

- [About the Project](#about-the-project)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Test Coverage](#test-coverage)
- [Setup & Installation](#setup--installation)
- [Configuration](#configuration)
- [How to Run Tests](#how-to-run-tests)
- [Test Reports](#test-reports)
- [CI/CD](#cicd)
- [Documentation](#documentation)
- [Author](#author)

---

## About the Project

This framework validates the business logic layer of a REST API directly — independent of any UI. It is designed following industry best practices:

- **Reusable API client** — single wrapper for all HTTP methods; base URL and headers managed in one place
- **Externalized test data** — all payloads stored in `test_data/payloads.py`, not hardcoded in tests
- **Secure credential handling** — API keys stored in `.env` locally and GitHub Secrets in CI; never committed to source control
- **Full traceability** — every test case maps to a documented requirement in the RTM

---

## Tech Stack

| Tool | Purpose |
|------|----------|
| Python 3.11 | Core language |
| Pytest | Test runner and assertions |
| Requests | HTTP library for API calls |
| pytest-html | HTML test report generation |
| python-dotenv | Secure environment variable management |
| GitHub Actions | CI/CD pipeline |

---

## Project Structure

```
API_Testing_Framework/
│
├── .github/
│   └── workflows/
│       └── pytest.yml          # GitHub Actions CI pipeline
│
├── docs/
│   └── API_Testing_RTM_Madhavi_Katte.xlsx   # Requirement Traceability Matrix
│
├── test_data/
│   ├── __init__.py
│   └── payloads.py             # All request payloads centralized here
│
├── tests/
│   ├── __init__.py
│   ├── test_users.py           # CRUD tests — GET, POST, PUT, DELETE
│   └── test_auth.py            # Auth tests — Register, Login
│
├── utils/
│   ├── __init__.py
│   └── api_client.py           # Reusable HTTP client wrapper
│
├── reports/                    # Auto-generated HTML reports (gitignored)
├── conftest.py                 # Pytest path configuration
├── pytest.ini                  # Pytest settings
├── requirements.txt            # Project dependencies
├── .env                        # Local secrets — never committed (gitignored)
└── .gitignore
```

---

## Test Coverage

### Users Module — `tests/test_users.py`

| Requirement | Test Scenario | Method | Type |
|-------------|--------------|--------|------|
| REQ-01 | Get all users returns 200 with data array | GET | Positive |
| REQ-01 | Get all users response time under 3 seconds | GET | Positive |
| REQ-02 | Get single user returns correct id and fields | GET | Positive |
| REQ-02 | Get single user email format is valid | GET | Positive |
| REQ-03 | Get non-existent user returns 404 | GET | Negative |
| REQ-03 | Get non-existent user returns empty body | GET | Negative |
| REQ-04 | Create user returns 201 with id and createdAt | POST | Positive |
| REQ-04 | Create user returns correct name and job | POST | Positive |
| REQ-05 | Update user returns 200 with updated fields | PUT | Positive |
| REQ-05 | Update user returns updatedAt timestamp | PUT | Positive |
| REQ-06 | Delete user returns 204 with empty body | DELETE | Positive |

### Auth Module — `tests/test_auth.py`

| Requirement | Test Scenario | Method | Type |
|-------------|--------------|--------|------|
| REQ-07 | Valid registration returns 200 with token | POST | Positive |
| REQ-08 | Registration without password returns 400 | POST | Negative |
| REQ-08 | Registration without password returns error message | POST | Negative |
| REQ-09 | Valid login returns 200 with token | POST | Positive |
| REQ-09 | Valid login token is non-empty string | POST | Positive |
| REQ-10 | Invalid login returns 400 with error | POST | Negative |

**Total: 25 test cases | 25 passing ✅**

---

## Setup & Installation

### Prerequisites
- Python 3.8 or higher
- A free ReqRes API key from [reqres.in](https://reqres.in)

### 1. Clone the repository

```bash
git clone https://github.com/Madhavikatte/API_Testing_Framework.git
cd API_Testing_Framework
```

### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

### Local Setup
Create a `.env` file in the project root:

```
REQRES_API_KEY=your_api_key_here
BASE_URL=https://reqres.in/api
```

> ⚠️ The `.env` file is gitignored and must never be committed. API keys should never appear in source code.

### CI Setup (GitHub Actions)
Add these repository secrets under `Settings → Secrets and variables → Actions`:

| Secret Name | Value |
|-------------|-------|
| `REQRES_API_KEY` | Your ReqRes API key |
| `BASE_URL` | `https://reqres.in/api` |

---

## How to Run Tests

### Run all tests

```bash
pytest
```

### Run a specific test file

```bash
pytest tests/test_users.py
pytest tests/test_auth.py
```

### Run a specific test class

```bash
pytest tests/test_users.py::TestGetUsers
pytest tests/test_auth.py::TestLogin
```

### Run by keyword

```bash
pytest -k "login"
pytest -k "delete"
```

All runs automatically generate an HTML report at `reports/report.html` via `pytest.ini` configuration.

---

## Test Reports

After each run, a self-contained HTML report is generated at `reports/report.html`. Open it in any browser — no internet connection required.

On CI, the report is uploaded as a downloadable artifact after every workflow run under **Actions → workflow run → Artifacts**.

> The `reports/` directory is gitignored — reports are generated fresh on every run.

---

## CI/CD

This project uses **GitHub Actions** for continuous integration. Tests run automatically on every push and pull request to `main`.

The pipeline:
1. Sets up Python 3.11
2. Installs dependencies from `requirements.txt`
3. Injects secrets securely as environment variables
4. Runs the full test suite via `pytest`
5. Uploads the HTML report as a downloadable artifact

No browser or driver setup needed — API tests run on pure Python.

---

## Documentation

A full **Requirement Traceability Matrix (RTM)** is maintained in:

```
docs/API_Testing_RTM_Madhavi_Katte.xlsx
```

The RTM contains:
- Requirement IDs mapped to test case IDs
- Endpoint, method, payload, and expected response for each test
- Actual results from manual Postman exploration
- Test execution summary with pass rate

---

## Author

**Madhavi Katte**
QA Automation Engineer | Python · Selenium · Pytest · API Testing · CI/CD

📧 madhavikatte99@gmail.com
🔗 [LinkedIn](https://linkedin.com/in/madhavikatte)
🐙 [GitHub](https://github.com/Madhavikatte)