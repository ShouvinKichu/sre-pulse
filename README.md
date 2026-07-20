# SRE Pulse

SRE Pulse continuously monitors registered services, stores historical health data, exposes Prometheus metrics, and visualizes operational insights through Grafana dashboards.

The project focuses on core SRE concepts including asynchronous health monitoring, observability, containerization, Infrastructure as Code (Terraform), and CI/CD automation.

---

## Why SRE Pulse?

Modern production systems require continuous visibility into service health and performance. SRE Pulse was built to explore how monitoring platforms are designed—from collecting health checks and metrics to visualizing operational data—using a clean, extensible architecture inspired by real-world SRE workflows.

---

## Screenshots

### Grafana Dashboard

![Grafana Dashboard](images/grafana-dashboard.png)

---

### API Documentation

![Scalar API](images/scalar-api.png)

---

### Prometheus Metrics

![Prometheus Metrics](images/prometheus-timeseries.png)

## Features

- 🔍 Continuous HTTP health monitoring
- ⚡ Asynchronous background worker
- 📊 Prometheus metrics endpoint
- 📈 Grafana dashboards
- 🗄 PostgreSQL persistent storage
- 🔄 Alembic database migrations
- 🐳 Dockerized application
- 📦 Docker Compose orchestration
- 🏗 Terraform fundamentals
- ⚙ GitHub Actions CI pipeline
- 🧹 Automated health check retention

---

## Architecture

```
                    +----------------+
                    |   Grafana      |
                    +-------+--------+
                            |
                            |
                    +-------v--------+
                    |  Prometheus    |
                    +-------+--------+
                            |
                            |
                    /metrics endpoint
                            |
                    +-------v--------+
                    |   FastAPI      |
                    |----------------|
                    | REST API       |
                    | Async Scheduler|
                    | Health Checker |
                    +-------+--------+
                            |
                    SQLAlchemy ORM
                            |
                    +-------v--------+
                    | PostgreSQL     |
                    +----------------+
```

---

## Tech Stack

| Category | Technology |
|----------|------------|
| Backend | FastAPI |
| Language | Python 3.12 |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Migrations | Alembic |
| Monitoring | Prometheus |
| Dashboard | Grafana |
| Containerization | Docker |
| Orchestration | Docker Compose |
| Infrastructure as Code | Terraform |
| CI/CD | GitHub Actions |
| Static Analysis | Ruff |

---

## Project Structure

```text
app/
├── config/
├── core/
├── models/
├── repositories/
├── routers/
├── scheduler/
├── services/
├── db.py
└── main.py

alembic/
prometheus/
terraform/
.github/workflows/

Dockerfile
docker-compose.yml
requirements.txt
```

---

## Quick Start

### Clone the repository

```bash
git clone https://github.com/ShouvinKichu/sre-pulse.git

cd sre-pulse
```

---

### Create virtual environment

```bash
python -m venv venv
```

Activate

macOS/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

### Configure environment

Create a `.env` file

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/srepulse
DEBUG=true
```

---

### Run with Docker Compose

```bash
docker compose up --build -d
```

---

## Services

| Service | URL |
|---------|-----|
| FastAPI | http://localhost:8000 |
| Scalar API Docs | http://localhost:8000/scalar |
| Prometheus | http://localhost:9090 |
| Grafana | http://localhost:3000 |

---

## Monitoring

SRE Pulse exports Prometheus metrics including:

- Service availability
- Response time
- Health status

Metrics endpoint

```
GET /metrics
```

Example

```
srepulse_service_up{service="Google"} 1

srepulse_response_time_ms{service="Google"} 184
```

---

## Grafana Dashboard

The dashboard includes:

- Service Health
- Response Time
- Average Response Time
- Maximum Response Time
- Minimum Response Time
- Services Up
- Services Down

---

## CI/CD

GitHub Actions automatically performs:

- Checkout Repository
- Install Dependencies
- Ruff Static Analysis
- Docker Image Build

The workflow runs on every push and pull request to `main`.

---

## Infrastructure

Terraform demonstrates Infrastructure as Code concepts and the standard workflow:

```text
terraform init

↓

terraform plan

↓

terraform apply

↓

terraform destroy
```

---

## Future Roadmap

### Monitoring & Alerting
- Email alerts
- Slack / Discord notifications
- Alert thresholds and escalation policies

### Cloud Native
- Kubernetes deployment
- Google Kubernetes Engine (GKE)
- Cloud deployment with Terraform

### Platform Features
- Authentication & RBAC
- Multi-region monitoring
- Automatic service discovery

### Reliability
- Retry policies with exponential backoff
- Configurable health check intervals
- Historical availability reports (SLA/Uptime)

---

## Author

**Shouvin A**

LinkedIn: [linkedin.com/in/shouvin](https://linkedin.com/in/shouvin)

---

## 📄 License

This project is licensed under the MIT License.