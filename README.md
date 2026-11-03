# SignAssist AI Core Service 🚀

A production-ready, scalable AI service core built with **FastAPI** and **Google Gemini API**, implementing **Clean Architecture** and strict software engineering design patterns.

---

## 🌟 Key Features

- **Modular Clean Architecture**: Separation of concerns between domain entities, abstract core models, and business logic services.
- **Abstract Base Engine (`AIModel`)**: Pluggable interface utilizing Python's `abc` module to enforce uniform model integration and easy provider swapping.
- **Live Google Gemini API Integration**: Direct interaction via the official `google-genai` SDK with built-in error handling and exponential backoff retry mechanisms.
- **Type Safety & Data Validation**: Request and response parsing powered by **Pydantic**.
- **Interactive Documentation**: Auto-generated OpenAPI/Swagger documentation for seamless API testing.
- **Secure Configuration**: Complete isolation of sensitive credentials via environment variables (`.env`).

---

## 🏗️ Project Architecture

```text
├── core/
│   ├── __init__.py
│   └── models.py          # Abstract Base Class (AIModel) & GeminiCloudModel implementation
├── services/
│   ├── __init__.py
│   └── ai_service.py       # AIService managing business logic, prompt handling & history
├── main.py                 # FastAPI application routes and dependency injection
├── .env.example            # Template for required environment variables
├── requirements.txt        # Project dependencies
└── README.md

```

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Framework:** FastAPI
* **AI SDK:** `google-genai`
* **Model Engine:** `models/gemini-flash-latest`
* **Validation:** Pydantic
* **Server:** Uvicorn

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name

```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
AI_MODEL_NAME=gemini-flash-latest
GEMINI_API_KEY=your_actual_gemini_api_key_here

```

### 5. Run the Application

```bash
uvicorn main:app --reload

```

Access the interactive API documentation at: `http://127.0.0.1:8000/docs`

---

## 📡 API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/` | Health check and current model status |
| `POST` | `/generate` | Accepts a JSON payload `{"prompt": "..."}` and returns the AI response |
| `GET` | `/history` | Retrieves session query and response history |

```

