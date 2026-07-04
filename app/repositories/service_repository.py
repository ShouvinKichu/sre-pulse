from sqlalchemy.orm import Session

from app.models.service import Service


class ServiceRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Service).all()

    def get_by_name(self, name: str):
        return self.db.query(Service).filter(Service.name == name).first()

    def create(self, service: Service):
        self.db.add(service)
        self.db.commit()
        self.db.refresh(service)
        return service

    def delete(self, service: Service):
        self.db.delete(service)
        self.db.commit()