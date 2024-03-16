# Workflow-api

This project use Python and Framework FastAPI.

## Getting Started

### Run project with Docker

Follow the command in Makefile:

First, to build the project:

```bash
make build
```

Second, to run the development server:

```bash
make dev
```

Open [http://localhost:8000](http://localhost:8000) with your browser to see the result.

### Endpoints

Backend API at [http://localhost:8000](http://localhost:8000)

FastAPI - Swagger UI at [http://localhost:8000/docs](http://localhost:8000/docs)

FastAPI - ReDoc at [http://localhost:8000/redoc](http://localhost:8000/redoc)

API_PREFIX = `/api/v1`

### Test with pytest

Follow the command in Makefile:

```bash
make test
```

### Dependencies

Dependencies is managed py poetry.

To install dependencies just do `poetry install`.

To add dependencies just do `poetry add [dependency]`.

To remove dependencies just do `poetry remove [dependency]`.

FastAPI uses:

- Starlette for the web parts.
- Pydantic for the data parts.

ASGI (Asynchronous Server Gateway Interface) server for production, such as: Uvicorn or Hypercorn.

Document with OpenAPI (Swagger) and JSON Schema.

### Database

SqlAlchemy is used in project for testing purposes in the technical test.

### Todo

Alembic for migration.

Redis Cache.

Pagination.
