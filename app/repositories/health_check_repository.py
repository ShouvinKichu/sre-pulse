from datetime import datetime, timedelta, UTC

from sqlalchemy.orm import Session
from sqlalchemy import func, delete

from app.models.health_checks import HealthCheck


class HealthCheckRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, health_check: HealthCheck):
        self.db.add(health_check)
        self.db.commit()
        self.db.refresh(health_check)
        return health_check
    
    def get_history(self, service_id: int):
        return (
            self.db.query(HealthCheck)
            .filter(HealthCheck.service_id == service_id)
            .order_by(HealthCheck.checked_at.desc())
            .all()
        )   
    
    def get_total_checks(self, service_id: int):
        return (
            self.db.query(func.count(HealthCheck.id))
            .filter(HealthCheck.service_id == service_id)
            .scalar()
        )
    
    def get_successful_checks(self, service_id: int):
        return (
            self.db.query(func.count(HealthCheck.id))
            .filter(
                HealthCheck.service_id == service_id,
                HealthCheck.status.is_(True),
            )
            .scalar()
        )
    
    def get_failed_checks(self, service_id: int):
        return (
            self.db.query(func.count(HealthCheck.id))
            .filter(
                HealthCheck.service_id == service_id,
                HealthCheck.status.is_(False),
            )
            .scalar()
        )
    
    def get_average_response_time(self, service_id: int):
        return (
            self.db.query(func.avg(HealthCheck.response_time_ms))
            .filter(
                HealthCheck.service_id == service_id,
                HealthCheck.status.is_(True),
            )
            .scalar()
        )
    
    def get_latest_check(self, service_id: int):
        return (
            self.db.query(HealthCheck)
            .filter(HealthCheck.service_id == service_id)
            .order_by(HealthCheck.checked_at.desc())
            .first()
        )
    
    def delete_old_health_checks(self, retention_days: int) -> None:
        cutoff = datetime.now(UTC) - timedelta(days=retention_days)

        stmt = delete(HealthCheck).where(
            HealthCheck.checked_at < cutoff
        )

        result = self.db.execute(stmt)
        self.db.commit()

        return result.rowcount