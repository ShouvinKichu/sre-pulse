from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

from app.db import engine
from app.models.service import Service
from app.routers import services

app = FastAPI(
    title="SRE Pulse",
    description="A system metrics dashboard API — ingest, store, and alert on service health.",
    version="0.1.0",
)

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