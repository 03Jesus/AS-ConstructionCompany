from sqlalchemy.orm import Session

from database.db_models import Employee
from ..models.employee_model import EmployeeModel, EmployeeUpdateModel


def get_employees(db: Session):
    return db.query(Employee).all()


def get_employee_by_id(db: Session, employee_id: int):
    return db.query(Employee).filter(Employee.id == employee_id).first()


def create_employee(db: Session, employee: EmployeeModel):
    db_employee = Employee(
        name=employee.name,
        last_name=employee.last_name,
        phone=employee.phone,
        mail=employee.mail,
        type=employee.type,
    )
    db.add(db_employee)
    db.commit()
    db.flush(db_employee)
    return db_employee


def update_employee(db: Session, employee_id: int, employee: EmployeeUpdateModel):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if employee.name:
        db_employee.name = employee.name
    if employee.last_name:
        db_employee.last_name = employee.last_name
    if employee.phone:
        db_employee.phone = employee.phone
    if employee.mail:
        db_employee.mail = employee.mail
    if employee.type:
        db_employee.type = employee.type
    db.commit()
    db.flush(db_employee)
    return db_employee


def delete_employee(db: Session, employee_id: int):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    db.delete(db_employee)
    db.commit()
    return db_employee
