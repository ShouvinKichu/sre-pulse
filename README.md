# 🚀 SRE Pulse

A production-grade service monitoring platform built with FastAPI that continuously monitors website and API availability, stores historical health data, exports Prometheus metrics, and provides reliability insights for SRE and Platform Engineering workflows.

## Features

- ✅ Register and manage services to monitor
- ✅ Asynchronous background health checks
- ✅ Response time & HTTP status monitoring
- ✅ Historical health check storage
- ✅ Service statistics (uptime, failures, average latency)
- ✅ Dashboard API for monitoring multiple services
- ✅ Prometheus metrics exporter
- ✅ PostgreSQL persistence with SQLAlchemy & Alembic
- ✅ Dockerized development environment

## Tech Stack

- FastAPI
- Python
- PostgreSQL
- SQLAlchemy
- Alembic
- AsyncIO
- HTTPX
- Prometheus
- Docker

## Architecture

```
                Internet
                    │
                    ▼
          Async Monitoring Worker
                    │
          HTTP Health Checks
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
   PostgreSQL            Prometheus Metrics
        │                       │
        ▼                       ▼
 Historical Data         /metrics Endpoint
        │
        ▼
     FastAPI APIs
```

## APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/services` | Register a service |
| GET | `/services` | List monitored services |
| DELETE | `/services/{name}` | Remove a service |
| GET | `/services/{name}/history` | Health check history |
| GET | `/services/{name}/stats` | Service statistics |
| GET | `/dashboard` | Monitoring dashboard data |
| GET | `/metrics` | Prometheus metrics |

## Upcoming Features

- 📊 Grafana dashboards
- 📧 SMTP email alerts
- 🔁 Retry & consecutive failure detection
- 🐳 Docker Compose
- ☸️ Kubernetes deployment
- ☁️ Google Cloud (GKE)
- 🏗️ Terraform Infrastructure as Code
- ⚙️ GitHub Actions CI/CD

## Status

🚧 Actively under development.
