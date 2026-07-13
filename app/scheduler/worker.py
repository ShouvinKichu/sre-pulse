import asyncio

from app.db import SessionLocal
from app.repositories.service_repository import ServiceRepository

from app.services.health_checker import check_service

from app.core.constants import RETENTION_DAYS

from app.repositories.health_check_repository import HealthCheckRepository
from app.models.health_checks import HealthCheck

from app.services.metrics_service import update_metrics

async def monitor_services():
    print("🚀 Worker started")

    while True:
        try:
            print("🔍 Inside while loop")

            db = SessionLocal()

            service_repo = ServiceRepository(db)
            health_repo = HealthCheckRepository(db)
            services = service_repo.get_all()

            print(f"Found {len(services)} services")

            for service in services:
                print(f"Checking {service.name}...")

                result = await check_service(service.url)

                health_check = HealthCheck(
                    service_id=service.id,
                    status=result["status"],
                    status_code=result["status_code"],
                    response_time_ms=result["response_time_ms"],
                    error_message=result["error_message"],
                )

                health_repo.create(health_check)

                update_metrics(
                    service.name,
                    result,
                )

                print(
                    f"{service.name}: "
                    f"{result['status_code']} "
                    f"({result['response_time_ms']} ms)"
                )
            deleted = health_repo.delete_old_health_checks(RETENTION_DAYS)

            if deleted > 0:
                print(f"🧹 Deleted {deleted} old health checks")

        except Exception as e:
            print(f"❌ Worker crashed: {e}")
            

        finally:
            db.close()

        await asyncio.sleep(10)

        