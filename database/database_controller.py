from decouple import config
import databases

import sqlalchemy
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


def database_connection():
    DATABASE_URL = config('DATABASE_URL')
    metadata = sqlalchemy.MetaData()

    # Employees table
    employees = sqlalchemy.Table(
        "employees",
        metadata,
        sqlalchemy.Column("id", sqlalchemy.Integer,
                          primary_key=True, index=True),
        sqlalchemy.Column("name", sqlalchemy.String),
        sqlalchemy.Column("last_name", sqlalchemy.String),
        sqlalchemy.Column("phone", sqlalchemy.String),
        sqlalchemy.Column("mail", sqlalchemy.String),
        sqlalchemy.Column("type", sqlalchemy.String),
    )

    # Payrolls table
    payrolls = sqlalchemy.Table(
        "payrolls",
        metadata,
        sqlalchemy.Column("id", sqlalchemy.Integer,
                          primary_key=True, index=True),
        sqlalchemy.Column("name", sqlalchemy.String),
    )

    # Payrolls-Employees table
    payrolls_employees = sqlalchemy.Table(
        "payrolls_employees",
        metadata,
        sqlalchemy.Column("id", sqlalchemy.Integer,
                          primary_key=True, index=True),
        sqlalchemy.Column("payroll_id", sqlalchemy.Integer,
                          ForeignKey("payrolls.id")),
        sqlalchemy.Column("employee_id", sqlalchemy.Integer,
                          ForeignKey("employees.id")),
    )

    # Gadgets table
    gadgets = sqlalchemy.Table(
        "gadgets",
        metadata,
        sqlalchemy.Column("id", sqlalchemy.Integer,
                          primary_key=True, index=True),
        sqlalchemy.Column("name", sqlalchemy.String),
        sqlalchemy.Column("type", sqlalchemy.String),
        sqlalchemy.Column("state", sqlalchemy.String),
    )

    # Equipments table
    equipments = sqlalchemy.Table(
        "equipments",
        metadata,
        sqlalchemy.Column("id", sqlalchemy.Integer,
                          primary_key=True, index=True),
        sqlalchemy.Column("name", sqlalchemy.String),
    )

    # Equipments-Gadgets table
    equipments_gadgets = sqlalchemy.Table(
        "equipments_gadgets",
        metadata,
        sqlalchemy.Column("id", sqlalchemy.Integer,
                          primary_key=True, index=True),
        sqlalchemy.Column("equipment_id", sqlalchemy.Integer,
                          ForeignKey("equipments.id")),
        sqlalchemy.Column("gadget_id", sqlalchemy.Integer,
                          ForeignKey("gadgets.id")),
    )

    # Clients table
    clients = sqlalchemy.Table(
        "clients",
        metadata,
        sqlalchemy.Column("id", sqlalchemy.Integer,
                          primary_key=True, index=True),
        sqlalchemy.Column("name", sqlalchemy.String),
        sqlalchemy.Column("last_name", sqlalchemy.String),
        sqlalchemy.Column("phone", sqlalchemy.String),
        sqlalchemy.Column("mail", sqlalchemy.String),
    )

    # Schedules table
    schedules = sqlalchemy.Table(
        "schedules",
        metadata,
        sqlalchemy.Column("id", sqlalchemy.Integer,
                          primary_key=True, index=True),
        sqlalchemy.Column("start_date", sqlalchemy.Date),
        sqlalchemy.Column("finish_date", sqlalchemy.Date),
        sqlalchemy.Column("state", sqlalchemy.String),
    )

    # Projects table
    projects = sqlalchemy.Table(
        "projects",
        metadata,
        sqlalchemy.Column("id", sqlalchemy.Integer,
                          primary_key=True, index=True),
        sqlalchemy.Column("name", sqlalchemy.String),
        sqlalchemy.Column("description", sqlalchemy.String),
        sqlalchemy.Column("budget", sqlalchemy.Float),
        sqlalchemy.Column("schedule_id", sqlalchemy.Integer,
                          ForeignKey("schedules.id")),
        sqlalchemy.Column("client_id", sqlalchemy.Integer,
                          ForeignKey("clients.id")),
        sqlalchemy.Column("equipment_id", sqlalchemy.Integer,
                          ForeignKey("equipments.id")),
        sqlalchemy.Column("payroll_id", sqlalchemy.Integer,
                          ForeignKey("payrolls.id")),
    )

    engine = sqlalchemy.create_engine(
        DATABASE_URL, pool_size=3, max_overflow=0
    )

    metadata.create_all(engine)

    database = databases.Database(DATABASE_URL)

    return database, employees, payrolls, payrolls_employees, gadgets, equipments, equipments_gadgets, clients, schedules, projects
