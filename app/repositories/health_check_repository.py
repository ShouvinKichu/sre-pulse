from sqlalchemy.orm import Session

from app.models.health_checks import HealthCheck


class HealthCheckRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, health_check: HealthCheck):
        self.db.add(health_check)
        self.db.commit()
        self.db.refresh(health_check)
        return health_check