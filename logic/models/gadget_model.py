from typing import Optional

from pydantic import BaseModel


class GadgetModel (BaseModel):
    name: str
    type: str
    state: str
    schedule_id: Optional[int] = None

    class Config:
        from_attributes = True


class GadgetModelResponse (BaseModel):
    id: int
    name: str
    type: str
    state: str
    schedule_id: Optional[int] = None

    class Config:
        from_attributes = True


class GadgetUpdateModel (BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    state: Optional[str] = None
    schedule_id: Optional[int] = None

    class Config:
        from_attributes = True
