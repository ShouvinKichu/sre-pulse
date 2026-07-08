from sqlalchemy.orm import Session

from app.models.service import Service


class ServiceRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[Service]:
        return self.db.query(Service).all()

    def get_by_name(self, name: str) -> Service | None:
        return self.db.query(Service).filter(Service.name == name).first()

    def create(self, service: Service) -> Service:
        self.db.add(service)
        self.db.commit()
        self.db.refresh(service)
        return service

    def delete(self, service: Service) -> None:
        self.db.delete(service)
        self.db.commit()