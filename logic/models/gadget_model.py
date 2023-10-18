from typing import Optional

from pydantic import BaseModel


class GadgetModel (BaseModel):
    name: str
    type: str
    state: str

    class Config:
        from_attributes = True


class GadgetModelResponse (BaseModel):
    id: int
    name: str
    type: str
    state: str

    class Config:
        from_attributes = True


class GadgetUpdateModel (BaseModel):
    name: Optional[str]
    type: Optional[str]
    state: Optional[str]

    class Config:
        from_attributes = True
