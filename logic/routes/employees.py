from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.get_db import get_db
from ..models.employee_model import EmployeeModel, EmployeeModelResponse, EmployeeUpdateModel
import logic.controller.employees_crud as employees_crud

employee_router = APIRouter(
    prefix="/employees",
    tags=["Employees"],
    dependencies=[Depends(get_db)]
)


@employee_router.get("/",
                     response_model=List[EmployeeModelResponse],
                     summary="Get a list of all employees")
def get_employees(db: Session = Depends(get_db)):
    """
    Get a list of all employees

    - **id**: Employee's id
    - **name**: Employee's name
    - **last_name**: Employee's last name
    - **phone**: Employee's phone number
    - **mail**: Employee's email
    - **type**: Employee's type
    """
    return employees_crud.get_employees(db=db)


@employee_router.get("/{employee_id:int}",
                     response_model=EmployeeModelResponse,
                     summary="Get a single employee")
def get_employee(employee_id, db: Session = Depends(get_db)):
    """
    Get a single employee

    - **id**: Employee's id
    - **name**: Employee's name
    - **last_name**: Employee's last name
    - **phone**: Employee's phone number
    - **mail**: Employee's email
    - **type**: Employee's type
    """
    employee_found = employees_crud.get_employee_by_id(
        db=db, employee_id=employee_id)
    if employee_found:
        return employee_found
    raise HTTPException(
        status_code=404, detail=f"Employee with id: {employee_id} not found")


@employee_router.post("/",
                      response_model=EmployeeModelResponse,
                      summary="Create a new employee")
def create_employee(employee: EmployeeModel, db: Session = Depends(get_db)):
    """
    Create a new employee with all the information

    - **name**: Employee's name
    - **last_name**: Employee's last name
    - **phone**: Employee's phone number
    - **mail**: Employee's email
    - **type**: Employee's type
    """
    return employees_crud.create_employee(db=db, employee=employee)


@employee_router.put("/{employee_id:int}",
                     response_model=EmployeeModelResponse,
                     summary="Update a single employee")
def update_employee(employee_id, employee: EmployeeUpdateModel, db: Session = Depends(get_db)):
    """
    Update a single employee

    - **id**: Employee's id to update
    - **name**: Employee's name
    - **last_name**: Employee's last name
    - **phone**: Employee's phone number
    - **mail**: Employee's email
    - **type**: Employee's type

    If the field is not going to be updated, just leave it empty (null)
    """
    employee_found = employees_crud.get_employee_by_id(
        db=db, employee_id=employee_id)
    if employee_found:
        return employees_crud.update_employee(db=db, employee_id=employee_id, employee=employee)
    raise HTTPException(
        status_code=404, detail=f"Employee with id: {employee_id} not found")


@employee_router.delete("/{employee_id:int}", summary="Delete a single employee")
def delete_employee(employee_id, db: Session = Depends(get_db)):
    """
    Delete a single employee

    - **id**: Employee's id to delete
    """
    employee_found = employees_crud.get_employee_by_id(
        db=db, employee_id=employee_id)
    if employee_found:
        return employees_crud.delete_employee(db=db, employee_id=employee_id)
    raise HTTPException(
        status_code=404, detail=f"Employee with id: {employee_id} not found")
