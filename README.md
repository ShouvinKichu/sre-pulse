# 🚀 SRE Pulse

**SRE Pulse** is a production-inspired service monitoring platform built with FastAPI. It continuously monitors the health of configured services, stores historical health data, exposes Prometheus metrics, and visualizes them through Grafana dashboards.

The project was built to demonstrate practical Site Reliability Engineering (SRE) and DevOps concepts including asynchronous monitoring, observability, containerization, Infrastructure as Code, and CI/CD.

---

## ✨ Features

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

## 🏗 Architecture

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
                    | Background Job |
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

## 🛠 Tech Stack

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

## 📁 Project Structure

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

## 🚀 Getting Started

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

## 🌐 Services

| Service | URL |
|---------|-----|
| FastAPI | http://localhost:8000 |
| Scalar API Docs | http://localhost:8000/scalar |
| Prometheus | http://localhost:9090 |
| Grafana | http://localhost:3000 |

---

## 📊 Monitoring

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

## 📈 Grafana Dashboard

The dashboard includes:

- Service Health
- Response Time
- Average Response Time
- Maximum Response Time
- Minimum Response Time
- Services Up
- Services Down

---

## 🔄 CI/CD

GitHub Actions automatically performs:

- Checkout Repository
- Install Dependencies
- Ruff Static Analysis
- Docker Image Build

The workflow runs on every push and pull request to `main`.

---

## 🏗 Infrastructure

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

## 📌 Future Enhancements

- Email alerts
- Slack / Discord notifications
- Kubernetes deployment
- Google Kubernetes Engine (GKE)
- Terraform cloud infrastructure
- Authentication & RBAC
- Multi-region monitoring
- Service discovery

---

## 👨‍💻 Author

**Shouvin A**

LinkedIn: https://linkedin.com/in/shouvin

---

## 📄 License

This project is licensed under the MIT License.