from datetime import datetime

from pydantic import BaseModel, ConfigDict


class HealthCheckResponse(BaseModel):
    status: bool
    status_code: int | None
    response_time_ms: int | None
    error_message: str | None
    checked_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )