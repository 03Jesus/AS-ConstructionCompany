from typing import List

from pydantic import BaseModel

from logic.models.employee_model import EmployeeModel


class PayrollModel (BaseModel):
    name: str

    class Config:
        from_attributes = True


class PayrollModelRespone (BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
