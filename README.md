# API

A simple, scalable Python API built with FastAPI and SQLite.

## Project Structure

```
api_project/
├── app/
│   ├── api/                 # API routes
│   ├── models/              # SQLAlchemy models
│   ├── schemas/             # Pydantic schemas
│   ├── __init__.py
│   ├── config.py            # Configuration management
│   ├── database.py          # Database setup and session
│   └── main.py              # Application entry point
├── tests/                   # Test suite
├── requirements.txt         # Python dependencies
├── .env.example             # Environment variables template
├── .gitignore
└── README.md
```

## Setup

### Prerequisites
- Python 3.12+
- pip

### Installation

1. Clone the repository and navigate to the project directory:
```bash
cd api_project
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file from template:
```bash
cp .env.example .env
```

## Running the API

Start the development server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

Access API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Testing

Run tests:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=app
```

## Project Patterns

This project follows:
- **Dependency Injection**: Database sessions injected via FastAPI dependencies
- **Separation of Concerns**: Models, schemas, and routes in separate modules
- **Configuration Management**: Environment-based settings via Pydantic
- **Testing**: Pytest with test database isolation

## Adding New Endpoints

1. Create model in `app/models/` if needed
2. Create schema in `app/schemas/` if needed
3. Add route in `app/api/routes.py` or create new router file
4. Include router in `app/main.py`
5. Add tests in `tests/`
