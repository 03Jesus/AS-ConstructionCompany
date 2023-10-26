from typing import Optional, List

from logic.models.person_model import PersonModel
from logic.models.schedule_model import ScheduleModel


class EmployeeModel (PersonModel):
    type: str

    class Config:
        from_attributes = True


class EmployeeModelResponse (PersonModel):
    id: int
    type: str
    schedules: List[ScheduleModel]

    class Config:
        from_attributes = True


class EmployeeUpdateModel (PersonModel):
    type: Optional[str] = None

    class Config:
        from_attributes = True
