# QA Automation API Template

A professional API test automation starter template for testers who want to build real-world skills and get hired faster.

---

## What is this project?

This repository provides a clean and simple automation framework designed to simulate a real QA Automation project environment.

It helps you practice:

* API testing
* Test design
* Automation architecture
* Debugging real API behavior
* Writing maintainable tests

The goal is learning **how automation is done in real jobs**, not just writing assertions.

---

## Technologies

* Python
* pytest
* requests

---

Project Structure
tests/
    jsonplaceholder/
        test_healthcheck.py
        test_example.py
    fakestore/
        test_products.py

utils/
    api_client.py  # reusable HTTP clien
    validators.py  # reusable response validators

config/
    settings.py

pytest.ini

requirements.txt

---

## What is covered

### Contract Testing

Validate API response structure and data types using reusable validators.

### Parametrized Testing

Run the same test across multiple product IDs without duplicating code.

### Negative Testing

Validate behavior for non-existing resources (empty response handling).

### Test Markers

Organize suites using:

* smoke
* api
* regression

### Multi-API Support

Switch between different services without modifying the framework.

---

## How to run

### 1 — Clone repository

```
git clone <your-repo-url>
cd qa-automation-api-template
```

### 2 — Create virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

### 3 — Install dependencies

```
pip install -r requirements.txt
```

### 4 — Run tests

```
pytest
```

---

## Why this project exists

Many beginners learn syntax but not structure.

This project focuses on:

* clean organization
* scalable tests
* real QA thinking

The intention is to help testers build a portfolio that looks like professional experience.

---

## Author

Almendra Polezzeli
almendra-testlab
