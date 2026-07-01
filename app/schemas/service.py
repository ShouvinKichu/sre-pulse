from pydantic import BaseModel, Field
from datetime import datetime


class ServiceCreate(BaseModel):
    """What the client sends us to register a new service."""
    name: str = Field(..., min_length=1, max_length=100, examples=["payment-processor"])
    description: str | None = Field(default=None, max_length=500)


class ServiceResponse(BaseModel):
    """What we send back to the client. Note: this is DIFFERENT from ServiceCreate.
    We never just return the input back — we add server-generated fields like id
    and created_at. Separating request/response schemas is a deliberate FastAPI
    pattern, not duplication for its own sake."""
    id: int
    name: str
    description: str | None
    created_at: datetime

    class Config:
        from_attributes = True  # lets this be built from an ORM object later (Step 3)
