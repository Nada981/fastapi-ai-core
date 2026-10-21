# FastAPI Modular AI Core Service

A production-grade, modular microservice architecture built with **FastAPI** and **Pydantic**, designed to serve and orchestrate AI model inferences with structured validation, clean OOP abstractions, and session history management.

## 🚀 Key Architectural Features

- **Modular Design:** Strict separation of concerns across `core` (domain models and abstractions) and `services` (business logic and history logging).
- **OOP & Dependency Injection:** Utilizes Abstract Base Classes (`ABC`) for flexible model swapping and loose coupling.
- **Data Validation:** Powered by **Pydantic** to enforce strict input schemas and automated HTTP `422` error handling.
- **Robust Error Handling:** Custom domain exceptions mapped cleanly to standard HTTP status codes (`400 Bad Request` vs `500 Server Error`).
- **Interactive Documentation:** Out-of-the-box OpenAPI specification and Swagger UI testing suite.

## 📁 Project Structure

```text
fastapi-ai-core/
├── core/
│   └── models.py        # Abstract AI interfaces & concrete implementations
├── services/
│   └── ai_service.py    # Business logic, query orchestration & history state
├── main.py              # FastAPI endpoints, dependency setup & routing
├── .gitignore           # Ignored caches and local environment artifacts
└── README.md            # Technical project documentation

```

## 🛠️ Getting Started

### 1. Prerequisites

* Python 3.10+

### 2. Installation

Clone the repository and install dependencies:

```bash
git clone [https://github.com/Nada981/fastapi-ai-core.git](https://github.com/Nada981/fastapi-ai-core.git)
cd fastapi-ai-core
pip install fastapi uvicorn pydantic

```

### 3. Run the Server

Launch the development server with live reload:

```bash
uvicorn main:app --reload

```

### 4. Interactive API Docs

Visit the interactive Swagger UI at:
👉 `http://127.0.0.1:8000/docs`

