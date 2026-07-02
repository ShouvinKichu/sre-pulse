from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from app.routers import services

app = FastAPI(
    title="SRE Pulse",
    description="A system metrics dashboard API — ingest, store, and alert on service health.",
    version="0.1.0",
)

app.include_router(services.router)


@app.get("/health")
def health_check():
    """
    Liveness check. Returns 200 if the API process itself is up.
    This is NOT the same as checking if dependencies (DB, Redis) are healthy —
    we'll separate that into /readyz once the DB layer exists (Step 3).
    """
    return {"status": "ok"}

@app.get("/scalar", include_in_schema=False)
def scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )