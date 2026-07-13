from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

from contextlib import asynccontextmanager
import asyncio

from prometheus_client import make_asgi_app

metrics_app = make_asgi_app()

from app.db import engine
from app.models import Service, HealthCheck
from app.routers import services

from app.scheduler.worker import monitor_services


@asynccontextmanager
async def lifespan(app: FastAPI):
    task = asyncio.create_task(monitor_services())

    yield

    task.cancel()


app = FastAPI(
    title="SRE Pulse",
    description="A system metrics dashboard API — ingest, store, and alert on service health.",
    version="0.1.0",
    lifespan=lifespan,
)
app.mount("/metrics", metrics_app)

app.include_router(services.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/scalar", include_in_schema=False)
def scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )

