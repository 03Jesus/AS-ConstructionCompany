from sqlalchemy.orm import Session

from database.db_models import Schedule, Employee, Project
from ..models.schedule_model import ScheduleModel, ScheduleUpdateModel
from .projects_crud import verify_if_record_exists


def get_schedules(db: Session):
    return db.query(Schedule).all()


def get_schedule_by_id(db: Session, schedule_id: int):
    return db.query(Schedule).filter(Schedule.id == schedule_id).first()


def create_schedule(db: Session, schedule: ScheduleModel):
    if schedule.employee_id:
        verify_if_record_exists(db=db, model=Employee,
                                model_id=schedule.employee_id)
    db_schedule = Schedule(
        name=schedule.name,
        description=schedule.description,
        start_date=schedule.start_date,
        finish_date=schedule.finish_date,
        priority=schedule.priority,
        state=schedule.state,
        project_id=schedule.project_id,
        employee_id=schedule.employee_id,
    )
    db.add(db_schedule)
    db.commit()
    db.flush(db_schedule)
    return db_schedule


def update_schedule(db: Session, schedule_id: int, schedule: ScheduleUpdateModel):
    db_schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    if schedule.name:
        db_schedule.name = schedule.name
    if schedule.description:
        db_schedule.description = schedule.description
    if schedule.start_date:
        db_schedule.start_date = schedule.start_date
    if schedule.finish_date:
        db_schedule.finish_date = schedule.finish_date
    if schedule.priority:
        db_schedule.priority = schedule.priority
    if schedule.state:
        db_schedule.state = schedule.state
    if schedule.project_id:
        verify_if_record_exists(db=db, model=Project,
                                model_id=schedule.project_id)
        db_schedule.project_id = schedule.project_id
    if schedule.employee_id:
        verify_if_record_exists(db=db, model=Employee,
                                model_id=schedule.employee_id)
        db_schedule.employee_id = schedule.employee_id
    db.commit()
    db.flush(db_schedule)
    return db_schedule


def delete_schedule(db: Session, schedule_id: int):
    db_schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    db.delete(db_schedule)
    db.commit()
    return {"message": f"Schedule {db_schedule.id} deleted"}
