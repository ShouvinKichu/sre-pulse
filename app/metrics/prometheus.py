from prometheus_client import Gauge


SERVICE_UP = Gauge(
    "srepulse_service_up",
    "Current service health status",
    ["service"],
)


RESPONSE_TIME = Gauge(
    "srepulse_response_time_ms",
    "Current response time in milliseconds",
    ["service"],
)