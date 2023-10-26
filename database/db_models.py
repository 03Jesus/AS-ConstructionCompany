from typing import Optional, List

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship, Mapped, mapped_column


from database.db_session import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), index=True)
    last_name = Column(String(30), index=True)
    phone = Column(String(15), index=True)
    mail = Column(String(40), index=True)
    type = Column(String(15), index=True)
    schedules: Mapped[List["Schedule"]] = relationship()


class Gadget(Base):
    __tablename__ = "gadgets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), index=True)
    type = Column(String(30), index=True)
    state = Column(String(30), index=True)
    schedule_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("schedules.id"))


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), index=True)
    last_name = Column(String(30), index=True)
    phone = Column(String(15), index=True)
    mail = Column(String(40), index=True)


class Schedule(Base):
    __tablename__ = "schedules"

    id: Mapped[int] = mapped_column(primary_key=True)
    name = Column(String(30), index=True)
    description = Column(String(100), index=True)
    start_date = Column(DateTime, index=True)
    finish_date = Column(DateTime, index=True)
    priority = Column(Integer, index=True)
    state = Column(String(30), index=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"))
    employee_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("employees.id"))
    gadgets: Mapped[List["Gadget"]] = relationship()
    project = relationship("Project", back_populates="schedule_id")


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True)
    name = Column(String(30), index=True)
    description = Column(String(100), index=True)
    budget = Column(Float, index=True)
    start_date = Column(DateTime, index=True)
    finish_date = Column(DateTime, index=True)
    schedule_id = relationship(
        "Schedule", back_populates="project", cascade="all, delete-orphan")
    client_id = Column(Integer, ForeignKey("clients.id"))
