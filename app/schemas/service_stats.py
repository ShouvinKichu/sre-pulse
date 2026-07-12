from datetime import datetime

from pydantic import BaseModel


class ServiceStatsResponse(BaseModel):
    service: str
    total_checks: int
    successful_checks: int
    failed_checks: int
    uptime_percentage: float
    average_response_time_ms: float | None

    latest_status: bool | None
    latest_status_code: int | None
    last_checked_at: datetime | None