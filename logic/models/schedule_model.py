from datetime import date
from typing import Optional, List

from pydantic import BaseModel

from logic.models.gadget_model import GadgetModelResponse


class ScheduleModel (BaseModel):
    name: str
    description: str
    start_date: date
    finish_date: date
    priority: int
    state: str
    project_id: int
    employee_id: Optional[int] = None

    class Config:
        from_attributes = True


class ScheduleModelResponse (BaseModel):
    id: int
    name: str
    description: str
    start_date: date
    finish_date: date
    priority: int
    state: str
    project_id: int
    employee_id: Optional[int] = None
    gadgets: Optional[List[GadgetModelResponse]] = None

    class Config:
        from_attributes = True


class ScheduleUpdateModel (BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[date] = None
    finish_date: Optional[date] = None
    priority: Optional[int] = None
    state: Optional[str] = None
    project_id: Optional[int] = None
    employee_id: Optional[int] = None

    class Config:
        from_attributes = True
