from typing import Optional

from pydantic import BaseModel


class ProjectModel (BaseModel):
    name: str
    description: str
    budget: float
    payroll_id: Optional[int] = None
    equipment_id: Optional[int] = None
    client_id: Optional[int] = None
    schedule_id: Optional[int] = None

    class Config:
        from_attributes = True


class ProjectModelResponse (BaseModel):
    id: int
    name: str
    description: str
    budget: float
    payroll_id: Optional[int] = None
    equipment_id: Optional[int] = None
    client_id: Optional[int] = None
    schedule_id: Optional[int] = None

    class Config:
        from_attributes = True


class ProjectUpdateModel (BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    budget: Optional[float] = None
    payroll_id: Optional[int] = None
    equipment_id: Optional[int] = None
    client_id: Optional[int] = None
    schedule_id: Optional[int] = None

    class Config:
        from_attributes = True
