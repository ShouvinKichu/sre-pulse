from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

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