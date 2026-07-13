from app.metrics.prometheus import (
    RESPONSE_TIME,
    SERVICE_UP,
)


def update_metrics(
    service_name: str,
    result: dict,
):
    SERVICE_UP.labels(
        service=service_name
    ).set(
        1 if result["status"] else 0
    )

    if result["response_time_ms"] is not None:
        RESPONSE_TIME.labels(
            service=service_name
        ).set(
            result["response_time_ms"]
        )