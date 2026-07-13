from pydantic import BaseModel


class DashboardResponse(BaseModel):
    name: str

    status: bool | None

    status_code: int | None

    response_time_ms: int | None

    uptime_percentage: float