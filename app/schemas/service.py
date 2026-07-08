from pydantic import BaseModel, Field
from datetime import datetime
from pydantic import HttpUrl

class ServiceCreate(BaseModel):
    
    name: str = Field(..., min_length=1, max_length=100, examples=["payment-processor"])
    description: str | None = Field(default=None, max_length=500)
    url: HttpUrl

class ServiceResponse(BaseModel):
    
    id: int
    name: str
    description: str | None
    url: str
    created_at: datetime
    

    class Config:
        from_attributes = True  
