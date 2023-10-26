from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.get_db import get_db
from ..models.project_model import ProjectModel, ProjectModelResponse, ProjectUpdateModel
import logic.controller.projects_crud as projects_crud

project_router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
    dependencies=[Depends(get_db)]
)


@project_router.get("/",
                    response_model=List[ProjectModelResponse],
                    summary="Get a list of all projects")
def get_projects(db: Session = Depends(get_db)):
    """
    Get a list of all projects

    - **id**: Project's id
    - **name**: Project's name
    - **description**: Project's description
    - **budget**: Project's budget
    - **payroll_id**: Project's payroll id
    - **equipment_id**: Project's equipment id
    - **client_id**: Project's client id
    - **schedule_id**: Project's schedule id
    """
    return projects_crud.get_projects(db=db)


@project_router.get("/{project_id:int}",
                    response_model=ProjectModelResponse,
                    summary="Get a project by id")
def get_project(project_id, db: Session = Depends(get_db)):
    """
    Get a project by id

    - **id**: Project's id
    """
    project_found = projects_crud.get_project_by_id(
        db=db, project_id=project_id)
    if project_found:
        return project_found
    raise HTTPException(
        status_code=404, detail=f"Project with id: {project_id} not found")


@project_router.post("/",
                     response_model=ProjectModelResponse,
                     summary="Create a new project")
def create_project(project: ProjectModel, db: Session = Depends(get_db)):
    """
    Create a new project

    - **name**: Project's name
    - **description**: Project's description
    - **budget**: Project's budget
    - **payroll_id**: Project's payroll id
    - **equipment_id**: Project's equipment id
    - **client_id**: Project's client id
    - **schedule_id**: Project's schedule id
    """
    return projects_crud.create_project(db=db, project=project)


@project_router.put("/{project_id:int}",
                    response_model=ProjectModelResponse,
                    summary="Update a project")
def update_project(project_id, project: ProjectUpdateModel, db: Session = Depends(get_db)):
    """
    Update a project

    - **name**: Project's name
    - **description**: Project's description
    - **budget**: Project's budget
    - **payroll_id**: Project's payroll id
    - **equipment_id**: Project's equipment id
    - **client_id**: Project's client id
    - **schedule_id**: Project's schedule id
    """
    project_found = projects_crud.get_project_by_id(
        db=db, project_id=project_id)
    if project_found:
        return projects_crud.update_project(db=db, project_id=project_id, project=project)
    raise HTTPException(
        status_code=404, detail=f"Project with id: {project_id} not found")


@project_router.delete("/{project_id:int}",
                       summary="Delete a project by id")
def delete_project(project_id, db: Session = Depends(get_db)):
    """
    Delete a project by id

    - **id**: Project's id
    """
    project_found = projects_crud.get_project_by_id(
        db=db, project_id=project_id)
    if project_found:
        return projects_crud.delete_project(db=db, project_id=project_id)
    raise HTTPException(
        status_code=404, detail=f"Project with id: {project_id} not found")
