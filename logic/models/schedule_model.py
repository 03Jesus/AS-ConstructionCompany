from datetime import date

from pydantic import BaseModel


class ScheduleModel (BaseModel):
    start_date: date
    finish_date: date
    state: str

    class Config:
        from_attributes = True


class ScheduleModelResponse (BaseModel):
    id: int
    start_date: date
    finish_date: date
    state: str

    class Config:
        from_attributes = True


class ScheduleUpdateModel (BaseModel):
    start_date: date
    finish_date: date
    state: str

    class Config:
        from_attributes = True
