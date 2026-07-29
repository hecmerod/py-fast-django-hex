# A Python API

DDD, Hexagonal architecture Python API using **FastAPI** (HTTP layer) and **Django ORM** (persistence).

## Architecture

```
src/
  main.py              → FastAPI app entry point
  router.py            → Route registration
  concert/
    domain/            → Entities, repository ports, and domain errors
    application/       → Use cases
    infrastructure/    → Controllers, DTOs, and repository adapters
    concert_dependencies.py
  shared/
    django/            → Django settings, models, migrations, and setup
    healthcheck/       → Health check endpoint
```

## Setup

1. Start PostgreSQL:

```bash
docker compose up -d db
```

2. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Copy environment variables (optional — defaults match the Docker Compose database):

```bash
cp .env.example .env
```

4. Run migrations:

```bash
python manage.py migrate
```

5. Start the API:

```bash
python run_api.py
```

Open http://127.0.0.1:8000/docs for the interactive API docs.

### Run with Docker

To start both PostgreSQL and the API in containers:

```bash
docker compose up --build
```

## API endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Health check |
| GET | `/api/concerts` | List all concerts |
| GET | `/api/concerts/{id}` | Get a concert |
| POST | `/api/concerts` | Create a concert |
| PUT | `/api/concerts/{id}` | Update a concert |
| DELETE | `/api/concerts/{id}` | Delete a concert |

## Testing

Install dev dependencies and run the test suite:

```bash
pip install -r requirements-dev.txt
pytest
```
