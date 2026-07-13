from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.health_check import HealthCheckResponse
from app.repositories.service_repository import ServiceRepository
from app.repositories.health_check_repository import HealthCheckRepository
from app.schemas.service_stats import ServiceStatsResponse
from app.schemas.dashboard import DashboardResponse

from app.db import get_db
from app.models.service import Service
from app.schemas.service import ServiceCreate, ServiceResponse

router = APIRouter(prefix="/services", tags=["services"])



@router.post("", response_model=ServiceResponse, status_code=status.HTTP_201_CREATED)
def register_service(
    service: ServiceCreate,
    db: Session = Depends(get_db),
):
    existing = db.query(Service).filter(Service.name == service.name).first()

    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Service already exists.",
        )

    new_service = Service(
        name=service.name,
        description=service.description,
        url=str(service.url),
    )

    db.add(new_service)
    db.commit()
    db.refresh(new_service)

    return new_service


@router.get("", response_model=list[ServiceResponse])
def list_services(
    db: Session = Depends(get_db),
):
    return db.query(Service).all()


@router.delete("/{name}", status_code=status.HTTP_204_NO_CONTENT)
def remove_service(
    name: str,
    db: Session = Depends(get_db),
):
    service = db.query(Service).filter(Service.name == name).first()

    if service is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Service not found.",
        )

    db.delete(service)
    db.commit()


@router.get(
    "/{name}/history",
    response_model=list[HealthCheckResponse],
)
def get_service_history(
    name: str,
    db: Session = Depends(get_db),
):
    service_repo = ServiceRepository(db)

    service = service_repo.get_by_name(name)

    if not service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Service not found.",
        )

    health_repo = HealthCheckRepository(db)

    history = health_repo.get_history(service.id)

    return history


@router.get(
    "/{name}/stats",
    response_model=ServiceStatsResponse,
)
def get_service_stats(
    name: str,
    db: Session = Depends(get_db),
):
    
    service_repo = ServiceRepository(db)
    service = service_repo.get_by_name(name)

    if not service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Service not found.",
        )

    health_repo = HealthCheckRepository(db)

    total_checks = health_repo.get_total_checks(service.id)

    successful_checks = health_repo.get_successful_checks(service.id)

    failed_checks = health_repo.get_failed_checks(service.id)

    average_response_time = health_repo.get_average_response_time(service.id)

    latest_check = health_repo.get_latest_check(service.id)

    uptime_percentage = (
        successful_checks / total_checks * 100
        if total_checks > 0
        else 0
    )

    return ServiceStatsResponse(
        service=service.name,
        total_checks=total_checks,
        successful_checks=successful_checks,
        failed_checks=failed_checks,
        uptime_percentage=uptime_percentage,
        average_response_time_ms=average_response_time,
        latest_status=latest_check.status if latest_check else None,
        latest_status_code=latest_check.status_code if latest_check else None,
        last_checked_at=latest_check.checked_at if latest_check else None,
    )


@router.get(
    "/dashboard",
    response_model=list[DashboardResponse],
)
def get_dashboard(
    db: Session = Depends(get_db),
):
    service_repo = ServiceRepository(db)
    health_repo = HealthCheckRepository(db)

    services = service_repo.get_all()

    dashboard = []

    for service in services:

        latest = health_repo.get_latest_check(service.id)

        total = health_repo.get_total_checks(service.id)

        successful = health_repo.get_successful_checks(service.id)

        uptime = (
            successful / total * 100
            if total > 0
            else 0
        )

        dashboard.append(
            DashboardResponse(
                name=service.name,
                status=latest.status if latest else None,
                status_code=latest.status_code if latest else None,
                response_time_ms=latest.response_time_ms if latest else None,
                uptime_percentage=uptime,
            )
        )

    return dashboard