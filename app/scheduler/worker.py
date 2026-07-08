import asyncio

from app.db import SessionLocal
from app.repositories.service_repository import ServiceRepository


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
                print(f"Checking {service.name}")

        except Exception as e:
            print(f"❌ Worker crashed: {e}")

        finally:
            db.close()

        await asyncio.sleep(10)