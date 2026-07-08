import asyncio

from app.db import SessionLocal
from app.repositories.service_repository import ServiceRepository

from app.services.health_checker import check_service

async def monitor_services():
    print("🚀 Worker started")

    while True:
        try:
            print("🔍 Inside while loop")

            db = SessionLocal()

            repo = ServiceRepository(db)
            services = repo.get_all()

            print(f"Found {len(services)} services")

            for service in services:
                print(f"Checking {service.name}...")

                result = await check_service(service.url)

                print(
                    f"{service.name}: "
                    f"{result['status_code']} "
                    f"({result['response_time_ms']} ms)"
                )

        except Exception as e:
            print(f"❌ Worker crashed: {e}")

        finally:
            db.close()

        await asyncio.sleep(10)

        