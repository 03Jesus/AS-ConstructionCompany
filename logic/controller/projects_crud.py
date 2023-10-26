from sqlalchemy.orm import Session
from fastapi import HTTPException

from database.db_models import Project, Client
from ..models.project_model import ProjectModel, ProjectUpdateModel


def verify_if_record_exists(db: Session, model, model_id: int):
    db_model = db.query(model).filter(model.id == model_id).first()
    if not db_model:
        raise HTTPException(
            status_code=404, detail=f"{model.__name__} with id: {model_id} not found")
    return db_model


def get_projects(db: Session):
    return db.query(Project).all()


def get_project_by_id(db: Session, project_id: int):
    return db.query(Project).filter(Project.id == project_id).first()


def create_project(db: Session, project: ProjectModel):
    if project.client_id:
        verify_if_record_exists(db=db, model=Client,
                                model_id=project.client_id)
    db_project = Project(
        name=project.name,
        description=project.description,
        budget=project.budget,
        start_date=project.start_date,
        finish_date=project.finish_date,
        client_id=project.client_id,
    )
    db.add(db_project)
    db.commit()
    db.flush(db_project)
    return db_project


def update_project(db: Session, project_id: int, project: ProjectUpdateModel):
    db_project = db.query(Project).filter(Project.id == project_id).first()

    if project.name:
        db_project.name = project.name
    if project.description:
        db_project.description = project.description
    if project.budget:
        db_project.budget = project.budget
    if project.start_date:
        db_project.start_date = project.start_date
    if project.finish_date:
        db_project.finish_date = project.finish_date
    if project.client_id:
        verify_if_record_exists(db=db, model=Client,
                                model_id=project.client_id)
        db_project.client_id = project.client_id
    db.commit()
    db.flush(db_project)
    return db_project


def delete_project(db: Session, project_id: int):
    project = db.query(Project).filter(Project.id == project_id).first()
    if project:
        db.delete(project)
        db.commit()
        return {"message": f"Project with id: {project_id} deleted successfully"}
    raise HTTPException(
        status_code=404, detail=f"Project with id: {project_id} not found")
