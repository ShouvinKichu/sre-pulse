# SRE Pulse

A system metrics dashboard API — ingest, store, and alert on service health.
Built as a portfolio project demonstrating the full SRE/DevOps stack: FastAPI → Docker → Kubernetes (Helm) → CI/CD → Terraform → Prometheus/Grafana → ELK.

## Status: Week 2, Day 1 (in progress)

### Done
- Project structure (`app/main.py`, `routers/`, `schemas/`, `models/`, `core/`)
- `GET /health` — liveness check
- `POST /services` — register a service (201 / 409 on duplicate / 422 on bad input)
- `GET /services` — list all registered services
- `DELETE /services/{name}` — remove a service (204 / 404)

### Not yet done (in-memory storage only — replaced in Step 3)
- PostgreSQL persistence
- Redis caching
- `/metrics` ingest endpoint
- `/alerts` threshold logic
- API key auth

## Running locally

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Visit `http://localhost:8000/docs` for interactive Swagger UI.

## Why this structure?

Routes are grouped by resource (`routers/services.py`) rather than dumped into
`main.py`. Request and response schemas are kept separate (`ServiceCreate` vs
`ServiceResponse`) so we never accidentally leak server-generated fields back
into what the client is allowed to send.
