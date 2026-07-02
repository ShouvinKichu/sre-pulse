from fastapi import APIRouter, HTTPException, status
from datetime import datetime, timezone
from app.schemas.service import ServiceCreate, ServiceResponse

router = APIRouter(prefix="/services", tags=["services"])

# TEMPORARY in-memory store. This goes away in Step 3 when PostgreSQL comes in.
# Using a dict keyed by name so we can check for duplicates cheaply.
_services_db: dict[str, dict] = {}
_next_id = 1

@router.post("", response_model=ServiceResponse, status_code=status.HTTP_201_CREATED)
def register_service(service: ServiceCreate):
    """
    Register a new service to be monitored.
    Returns 201 Created on success, 409 Conflict if the service name already exists.
    """
    global _next_id

    if service.name in _services_db:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Service '{service.name}' is already registered.",
        )

    record = {
        "id": _next_id,
        "name": service.name,
        "description": service.description,
        "created_at": datetime.now(timezone.utc),
    }
    _services_db[service.name] = record
    _next_id += 1
    return record


@router.get("", response_model=list[ServiceResponse])
def list_services():
    """Return all registered services."""
    return list(_services_db.values())


@router.delete("/{name}", status_code=status.HTTP_204_NO_CONTENT)
def remove_service(name: str):
    """Remove a service by name. Returns 404 if it doesn't exist."""
    if name not in _services_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Service not found.")
    del _services_db[name]
    return None
