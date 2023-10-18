from pydantic import BaseModel


class EquipmentModel(BaseModel):
    name: str

    class Config:
        from_attributes = True


class EquipmentModelResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
