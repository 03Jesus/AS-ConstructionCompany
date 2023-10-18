from typing import Optional

from logic.models.person_model import PersonModel


class EmployeeModel (PersonModel):
    type: str

    class Config:
        from_attributes = True


class EmployeeModelResponse (PersonModel):
    id: int
    type: str

    class Config:
        from_attributes = True


class EmployeeUpdateModel (PersonModel):
    type: Optional[str]

    class Config:
        from_attributes = True
