from typing import Union, List
import urllib
import os
from decouple import config
from enum import Enum

import databases
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
import sqlalchemy
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

from database.database_controller import database_connection
from logic.models.employee_model import EmployeeModel, EmployeeModelResponse, EmployeeUpdateModel
from logic.models.payroll_model import PayrollModel, PayrollModelRespone
from logic.models.gadget_model import GadgetModel, GadgetModelResponse, GadgetUpdateModel
from logic.models.equipment_model import EquipmentModel, EquipmentModelResponse
from logic.models.client_model import ClientModel, ClientModelRespone, ClientUpdateModel
from logic.models.schedule_model import ScheduleModel, ScheduleModelResponse
from logic.models.project_model import ProjectModel, ProjectModelResponse, ProjectUpdateModel

app = FastAPI(title="Construction Company API", version="0.1.7")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

database,\
    employees,\
    payrolls,\
    payrolls_employees,\
    gadgets,\
    equipments,\
    equipments_gadgets,\
    clients,\
    schedules,\
    projects = database_connection()


class Tags(Enum):
    employees = "Employees"
    payrolls = "Payrolls"
    gadgets = "Gadgets"
    equipments = "Equipments"
    clients = "Clients"
    schedules = "Schedules"
    projects = "Projects"


async def verify_record_exists(table_name, record_id):
    query = sqlalchemy.select([table_name]).where(table_name.c.id == record_id)
    result = await database.fetch_one(query)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"The record with id: {record_id} does not exist in the table {table_name}")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
def read_root():
    return {"Hello": "UTB"}


@app.post("/employees/",
          response_model=EmployeeModelResponse,
          status_code=status.HTTP_201_CREATED,
          tags=[Tags.employees],
          summary="Create a new employee"
          )
async def create_employee(employee: EmployeeModel):
    """
    Create a new employee with all the information

    - **name**: Employee's name
    - **last_name**: Employee's last name
    - **phone**: Employee's phone number
    - **mail**: Employee's email
    - **type**: Employee's type
    """
    query = employees.insert().values(
        name=employee.name,
        last_name=employee.last_name,
        phone=employee.phone,
        mail=employee.mail,
        type=employee.type
    )
    last_record_id = await database.execute(query)
    return {**employee.model_dump(), "id": last_record_id}


@app.get("/employees/",
         response_model=List[EmployeeModelResponse],
         status_code=status.HTTP_200_OK,
         tags=[Tags.employees],
         summary="Get all employees"
         )
async def read_employees():
    """
    Get a list of all employees

    - **id**: Employee's id
    - **name**: Employee's name
    - **last_name**: Employee's last name
    - **phone**: Employee's phone number
    - **mail**: Employee's email
    - **type**: Employee's type
    """
    query = employees.select()
    return await database.fetch_all(query)


@app.get("/employees/{employee_id}",
         response_model=EmployeeModelResponse,
         status_code=status.HTTP_200_OK,
         tags=[Tags.employees],
         summary="Get a single employee"
         )
async def read_employee(employee_id: int):
    """
    Get a single employee

    - **id**: Employee's id
    - **name**: Employee's name
    - **last_name**: Employee's last name
    - **phone**: Employee's phone number
    - **mail**: Employee's email
    - **type**: Employee's type
    """
    query = employees.select().where(employees.c.id == employee_id)
    return await database.fetch_one(query)


@app.put("/employees/{employee_id}",
         response_model=EmployeeModelResponse,
         status_code=status.HTTP_200_OK,
         tags=[Tags.employees],
         summary="Update a single employee"
         )
async def update_employee(employee_id: int, employee: EmployeeUpdateModel):
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
    query = employees.update().where(employees.c.id == employee_id)
    if employee.name:
        query = query.values(name=employee.name)
    if employee.last_name:
        query = query.values(last_name=employee.last_name)
    if employee.phone:
        query = query.values(phone=employee.phone)
    if employee.mail:
        query = query.values(mail=employee.mail)
    if employee.type:
        query = query.values(type=employee.type)
    await database.execute(query)
    return await read_employee(employee_id)


@app.delete("/employees/{employee_id}",
            status_code=status.HTTP_200_OK,
            tags=[Tags.employees],
            summary="Delete a single employee"
            )
async def delete_employee(employee_id: int):
    """
    Delete a single employee

    - **id**: Employee's id to delete
    """
    query = employees.delete().where(employees.c.id == employee_id)
    await database.execute(query)
    return {"message": "Employee with id: {} deleted successfully".format(employee_id)}


@app.post("/payrolls/",
          response_model=PayrollModelRespone,
          status_code=status.HTTP_201_CREATED,
          tags=[Tags.payrolls],
          summary="Create a new payroll"
          )
async def create_payroll(payroll: PayrollModel):
    """
    Create a new payroll

    - **name**: Payroll's name
    """
    query = payrolls.insert().values(
        name=payroll.name
    )
    last_record_id = await database.execute(query)
    return {**payroll.model_dump(), "id": last_record_id}


@app.get("/payrolls/",
         response_model=List[PayrollModelRespone],
         status_code=status.HTTP_200_OK,
         tags=[Tags.payrolls],
         summary="Get all payrolls"
         )
async def read_payrolls():
    """
    Get a list of all payrolls

    - **id**: Payroll's id
    - **name**: Payroll's name
    """
    query = payrolls.select()
    return await database.fetch_all(query)


@app.post("/payrolls/{payroll_id}/assign_employee/{employee_id}",
          status_code=status.HTTP_200_OK,
          tags=[Tags.payrolls],
          summary="Assign an employee to a payroll"
          )
async def assign_employee_to_payroll(payroll_id: int, employee_id: int):
    """
    Assign an employee to a payroll

    - **payroll_id**: Payroll's id to assign the employee
    - **employee_id**: Employee's id to assign to the payroll
    """
    query = payrolls_employees.insert().values(
        payroll_id=payroll_id,
        employee_id=employee_id
    )
    await database.execute(query)
    return {"message": "Employee with id: {} assigned to payroll with id: {} successfully".format(employee_id, payroll_id)}


@app.get("/payrolls/{payroll_id}/employees/",
         response_model=List[EmployeeModelResponse],
         status_code=status.HTTP_200_OK,
         tags=[Tags.payrolls],
         summary="Get all employees assigned to a payroll"
         )
async def read_payroll_employees(payroll_id: int):
    """
    Get a list of all employees assigned to a payroll

    - **payroll_id**: Payroll's id to get the employees assigned to it
    """
    query = employees.select().join(payrolls_employees).where(
        payrolls_employees.c.payroll_id == payroll_id)
    return await database.fetch_all(query)


@app.post("/gadgets/",
          response_model=GadgetModelResponse,
          status_code=status.HTTP_201_CREATED,
          tags=[Tags.gadgets],
          summary="Create a new gadget"
          )
async def create_gadget(gadget: GadgetModel):
    """
    Create a new gadget

    - **name**: Gadget's name
    - **type**: Gadget's type
    - **state**: Gadget's state
    """
    query = gadgets.insert().values(
        name=gadget.name,
        type=gadget.type,
        state=gadget.state
    )
    last_record_id = await database.execute(query)
    return {**gadget.model_dump(), "id": last_record_id}


@app.get("/gadgets/",
         response_model=List[GadgetModelResponse],
         status_code=status.HTTP_200_OK,
         tags=[Tags.gadgets],
         summary="Get all gadgets"
         )
async def read_gadgets():
    """
    Get a list of all gadgets
    """
    query = gadgets.select()
    return await database.fetch_all(query)


@app.get("/gadgets/{gadget_id}",
         response_model=GadgetModelResponse,
         status_code=status.HTTP_200_OK,
         tags=[Tags.gadgets],
         summary="Get a single gadget"
         )
async def read_gadget(gadget_id: int):
    """
    Get a single gadget

    - **id**: Gadget's id
    - **name**: Gadget's name
    - **type**: Gadget's type
    - **state**: Gadget's state
    """
    query = gadgets.select().where(gadgets.c.id == gadget_id)
    return await database.fetch_one(query)


@app.put("/gadgets/{gadget_id}",
         response_model=GadgetModelResponse,
         status_code=status.HTTP_200_OK,
         tags=[Tags.gadgets],
         summary="Update a single gadget"
         )
async def update_gadget(gadget_id: int, gadget: GadgetUpdateModel):
    """
    Update a single gadget

    - **id**: Gadget's id to update
    - **name**: Gadget's name
    - **type**: Gadget's type
    - **state**: Gadget's state

    If the field is not going to be updated, just leave it empty (null)
    """
    query = gadgets.update().where(gadgets.c.id == gadget_id)
    if gadget.name:
        query = query.values(name=gadget.name)
    if gadget.type:
        query = query.values(type=gadget.type)
    if gadget.state:
        query = query.values(state=gadget.state)
    await database.execute(query)
    return await read_gadget(gadget_id)


@app.delete("/gadgets/{gadget_id}",
            status_code=status.HTTP_200_OK,
            tags=[Tags.gadgets],
            summary="Delete a single gadget"
            )
async def delete_gadget(gadget_id: int):
    """
    Delete a single gadget

    - **id**: Gadget's id to delete
    """
    query = gadgets.delete().where(gadgets.c.id == gadget_id)
    await database.execute(query)
    return {"message": "Gadget with id: {} deleted successfully".format(gadget_id)}


@app.post("/equipments/",
          response_model=EquipmentModelResponse,
          status_code=status.HTTP_201_CREATED,
          tags=[Tags.equipments],
          summary="Create a new equipment"
          )
async def create_equipment(equipment: EquipmentModel):
    """
    Create a new equipment

    - **name**: Equipment's name
    """
    query = equipments.insert().values(
        name=equipment.name
    )
    last_record_id = await database.execute(query)
    return {**equipment.model_dump(), "id": last_record_id}


@app.get("/equipments/",
         response_model=List[EquipmentModelResponse],
         status_code=status.HTTP_200_OK,
         tags=[Tags.equipments],
         summary="Get all equipments"
         )
async def read_equipments():
    """
    Get a list of all equipments
    """
    query = equipments.select()
    return await database.fetch_all(query)


@app.post("/equipments/{equipment_id}/assign_gadget/{gadget_id}",
          status_code=status.HTTP_200_OK,
          tags=[Tags.equipments],
          summary="Assign a gadget to a equipment"
          )
async def assign_gadget_to_equipment(equipment_id: int, gadget_id: int):
    """
    Assign a gadget to a equipment

    - **equipment_id**: Equipment's id to assign the gadget
    - **gadget_id**: Gadget's id to assign to the equipment
    """
    query = equipments_gadgets.select().where(
        equipments_gadgets.c.gadget_id == gadget_id)
    result = await database.fetch_one(query)
    if result:
        return {"message": "Gadget with id: {} is already assigned to a equipment".format(gadget_id)}
    query = equipments_gadgets.insert().values(
        equipment_id=equipment_id,
        gadget_id=gadget_id
    )
    await database.execute(query)
    return {"message": "Gadget with id: {} assigned to equipment with id: {} successfully".format(gadget_id, equipment_id)}


@app.get("/equipments/{equipment_id}/gadgets/",
         response_model=List[GadgetModelResponse],
         status_code=status.HTTP_200_OK,
         tags=[Tags.equipments],
         summary="Get all gadgets assigned to a equipment"
         )
async def read_equipment_gadgets(equipment_id: int):
    """
    Get a list of all gadgets assigned to a equipment
    """
    query = gadgets.select().join(equipments_gadgets).where(
        equipments_gadgets.c.equipment_id == equipment_id)
    return await database.fetch_all(query)


@app.post("/clients/",
          response_model=ClientModelRespone,
          status_code=status.HTTP_201_CREATED,
          tags=[Tags.clients],
          summary="Create a new client"
          )
async def create_client(client: ClientModel):
    """
    Create a new client

    - **name**: Client's name
    - **last_name**: Client's last name
    - **phone**: Client's phone number
    - **mail**: Client's email
    """
    query = clients.insert().values(
        name=client.name,
        last_name=client.last_name,
        phone=client.phone,
        mail=client.mail
    )
    last_record_id = await database.execute(query)
    return {**client.model_dump(), "id": last_record_id}


@app.get("/clients/",
         response_model=List[ClientModelRespone],
         status_code=status.HTTP_200_OK,
         tags=[Tags.clients],
         summary="Get all clients"
         )
async def read_clients():
    """
    Get a list of all clients
    """
    query = clients.select()
    return await database.fetch_all(query)


@app.get("/clients/{client_id}",
         response_model=ClientModelRespone,
         status_code=status.HTTP_200_OK,
         tags=[Tags.clients],
         summary="Get a single client"
         )
async def read_client(client_id: int):
    """
    Get a single client

    - **id**: Client's id
    - **name**: Client's name
    - **last_name**: Client's last name
    - **phone**: Client's phone number
    - **mail**: Client's email
    """
    query = clients.select().where(clients.c.id == client_id)
    return await database.fetch_one(query)


@app.put("/clients/{client_id}",
         response_model=ClientModelRespone,
         status_code=status.HTTP_200_OK,
         tags=[Tags.clients],
         summary="Update a single client"
         )
async def update_client(client_id: int, client: ClientUpdateModel):
    """
    Update a single client

    - **id**: Client's id to update
    - **name**: Client's name
    - **last_name**: Client's last name
    - **phone**: Client's phone number
    - **mail**: Client's email

    If the field is not going to be updated, just leave it empty (null)
    """
    query = clients.update().where(clients.c.id == client_id)
    if client.name:
        query = query.values(name=client.name)
    if client.last_name:
        query = query.values(last_name=client.last_name)
    if client.phone:
        query = query.values(phone=client.phone)
    if client.mail:
        query = query.values(mail=client.mail)
    await database.execute(query)
    return await read_client(client_id)


@app.delete("/clients/{client_id}",
            status_code=status.HTTP_200_OK,
            tags=[Tags.clients],
            summary="Delete a single client"
            )
async def delete_client(client_id: int):
    """
    Delete a single client

    - **id**: Client's id to delete
    """
    query = clients.delete().where(clients.c.id == client_id)
    await database.execute(query)
    return {"message": "Client with id: {} deleted successfully".format(client_id)}


@app.post("/schedules/",
          response_model=ScheduleModelResponse,
          status_code=status.HTTP_201_CREATED,
          tags=[Tags.schedules],
          summary="Create a new schedule"
          )
async def create_schedule(schedule: ScheduleModel):
    """
    Create a new schedule

    - **start_date**: Schedule's start date
    - **finish_date**: Schedule's finish date
    - **state**: Schedule's state
    """
    query = schedules.insert().values(
        start_date=schedule.start_date,
        finish_date=schedule.finish_date,
        state=schedule.state
    )
    last_record_id = await database.execute(query)
    return {**schedule.model_dump(), "id": last_record_id}


@app.get("/schedules/",
         response_model=List[ScheduleModelResponse],
         status_code=status.HTTP_200_OK,
         tags=[Tags.schedules],
         summary="Get all schedules"
         )
async def read_schedules():
    """
    Get a list of all schedules
    """
    query = schedules.select()
    return await database.fetch_all(query)


@app.get("/schedules/{schedule_id}",
         response_model=ScheduleModelResponse,
         status_code=status.HTTP_200_OK,
         tags=[Tags.schedules],
         summary="Get a single schedule"
         )
async def read_schedule(schedule_id: int):
    """
    Get a single schedule

    - **id**: Schedule's id
    - **start_date**: Schedule's start date
    - **finish_date**: Schedule's finish date
    - **state**: Schedule's state
    """
    query = schedules.select().where(schedules.c.id == schedule_id)
    return await database.fetch_one(query)


@app.put("/schedules/{schedule_id}",
         response_model=ScheduleModelResponse,
         status_code=status.HTTP_200_OK,
         tags=[Tags.schedules],
         summary="Update a single schedule"
         )
async def update_schedule(schedule_id: int, schedule: ScheduleModel):
    """
    Update a single schedule

    - **id**: Schedule's id to update
    - **start_date**: Schedule's start date
    - **finish_date**: Schedule's finish date
    - **state**: Schedule's state

    If the field is not going to be updated, just leave it empty (null)
    """
    query = schedules.update().where(schedules.c.id == schedule_id)
    if schedule.start_date:
        query = query.values(start_date=schedule.start_date)
    if schedule.finish_date:
        query = query.values(finish_date=schedule.finish_date)
    if schedule.state:
        query = query.values(state=schedule.state)
    await database.execute(query)
    return await read_schedule(schedule_id)


@app.delete("/schedules/{schedule_id}",
            status_code=status.HTTP_200_OK,
            tags=[Tags.schedules],
            summary="Delete a single schedule"
            )
async def delete_schedule(schedule_id: int):
    """
    Delete a single schedule

    - **id**: Schedule's id to delete
    """
    query = schedules.delete().where(schedules.c.id == schedule_id)
    await database.execute(query)
    return {"message": "Schedule with id: {} deleted successfully".format(schedule_id)}


@app.post("/projects/",
          response_model=ProjectModelResponse,
          status_code=status.HTTP_201_CREATED,
          tags=[Tags.projects],
          summary="Create a new project"
          )
async def create_project(project: ProjectModel):
    """
    Create a new project

    - **name**: Project's name
    - **description**: Project's description
    - **budget**: Project's budget
    - **payroll_id**: Project's payroll id
    - **equipment_id**: Project's equipment id
    - **client_id**: Project's client id
    - **schedule_id**: Project's schedule id

    If the foreign key does not exist, it will raise an status code 404
    """
    await verify_record_exists(clients, project.client_id)
    await verify_record_exists(equipments, project.equipment_id)
    await verify_record_exists(payrolls, project.payroll_id)
    await verify_record_exists(schedules, project.schedule_id)

    query = projects.insert().values(
        name=project.name,
        description=project.description,
        budget=project.budget,
        payroll_id=project.payroll_id,
        equipment_id=project.equipment_id,
        client_id=project.client_id,
        schedule_id=project.schedule_id
    )
    last_record_id = await database.execute(query)
    return {**project.model_dump(), "id": last_record_id}


@app.get("/projects/",
         response_model=List[ProjectModelResponse],
         status_code=status.HTTP_200_OK,
         tags=[Tags.projects],
         summary="Get all projects"
         )
async def read_projects():
    """
    Get a list of all projects
    """
    query = projects.select()
    return await database.fetch_all(query)


@app.get("/projects/{project_id}",
         response_model=ProjectModelResponse,
         status_code=status.HTTP_200_OK,
         tags=[Tags.projects],
         summary="Get a single project"
         )
async def read_project(project_id: int):
    """
    Get a single project

    - **id**: Project's id
    - **name**: Project's name
    - **description**: Project's description
    - **budget**: Project's budget
    - **payroll_id**: Project's payroll id
    - **equipment_id**: Project's equipment id
    - **client_id**: Project's client id
    - **schedule_id**: Project's schedule id
    """
    query = projects.select().where(projects.c.id == project_id)
    return await database.fetch_one(query)


@app.put("/projects/{project_id}",
         response_model=ProjectModelResponse,
         status_code=status.HTTP_200_OK,
         tags=[Tags.projects],
         summary="Update a single project"
         )
async def update_project(project_id: int, project: ProjectUpdateModel):
    """
    Update a single project

    - **id**: Project's id to update
    - **name**: Project's name
    - **description**: Project's description
    - **budget**: Project's budget
    - **payroll_id**: Project's payroll id
    - **equipment_id**: Project's equipment id
    - **client_id**: Project's client id
    - **schedule_id**: Project's schedule id

    If the field is not going to be updated, just leave it empty (null)
    If the foreign key does not exist, it will raise an status code 404
    """
    await verify_record_exists(clients, project.client_id)
    await verify_record_exists(equipments, project.equipment_id)
    await verify_record_exists(payrolls, project.payroll_id)
    await verify_record_exists(schedules, project.schedule_id)

    query = projects.update().where(projects.c.id == project_id)
    if project.name:
        query = query.values(name=project.name)
    if project.description:
        query = query.values(description=project.description)
    if project.budget:
        query = query.values(budget=project.budget)
    if project.payroll_id:
        query = query.values(payroll_id=project.payroll_id)
    if project.equipment_id:
        query = query.values(equipment_id=project.equipment_id)
    if project.client_id:
        query = query.values(client_id=project.client_id)
    if project.schedule_id:
        query = query.values(schedule_id=project.schedule_id)
    await database.execute(query)
    return await read_project(project_id)


@app.delete("/projects/{project_id}",
            status_code=status.HTTP_200_OK,
            tags=[Tags.projects],
            summary="Delete a single project"
            )
async def delete_project(project_id: int):
    """
    Delete a single project

    - **id**: Project's id to delete
    """
    query = projects.delete().where(projects.c.id == project_id)
    await database.execute(query)
    return {"message": "Project with id: {} deleted successfully".format(project_id)}
