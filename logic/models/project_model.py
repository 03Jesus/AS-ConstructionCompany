from typing import Optional, List
from datetime import date

from pydantic import BaseModel

from logic.models.schedule_model import ScheduleModelResponse

# Model for post


class ProjectModel (BaseModel):
    name: str
    description: str
    budget: float
    start_date: Optional[date] = None
    finish_date: Optional[date] = None
    client_id: Optional[int] = None

    class Config:
        from_attributes = True

# Model for get


class ProjectModelResponse (BaseModel):
    id: int
    name: str
    description: str
    budget: float
    start_date: Optional[date] = None
    finish_date: Optional[date] = None
    schedule_id: Optional[List[ScheduleModelResponse]] = None
    client_id: Optional[int] = None

    class Config:
        from_attributes = True

# Model for put


class ProjectUpdateModel (BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    budget: Optional[float] = None
    start_date: Optional[date] = None
    finish_date: Optional[date] = None
    client_id: Optional[int] = None

    class Config:
        from_attributes = True
