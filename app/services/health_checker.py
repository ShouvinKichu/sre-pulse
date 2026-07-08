import time

import httpx


async def check_service(url: str):
    start = time.perf_counter()

    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(url)

        response_time = (time.perf_counter() - start) * 1000

        return {
            "status": response.status_code < 400,
            "status_code": response.status_code,
            "response_time_ms": round(response_time),
            "error_message": None,
        }

    except Exception as e:
        return {
            "status": False,
            "status_code": None,
            "response_time_ms": None,
            "error_message": str(e),
        }