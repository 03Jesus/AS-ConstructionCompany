from enum import Enum

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.db_session import engine, localSession
from database.db_models import Base
from logic.routes.employees import employee_router
from logic.routes.gadgets import gadget_router
from logic.routes.clients import client_router
from logic.routes.schedules import schedule_router
from logic.routes.projects import project_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Construction Company API", version="1.3.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(employee_router)
app.include_router(gadget_router)
app.include_router(client_router)
app.include_router(schedule_router)
app.include_router(project_router)


def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()


class Tags(Enum):
    employees = "Employees"
    payrolls = "Payrolls"
    gadgets = "Gadgets"
    equipments = "Equipments"
    clients = "Clients"
    schedules = "Schedules"
    projects = "Projects"


@app.get("/")
def read_root():
    return {"Hello": "UTB"}
