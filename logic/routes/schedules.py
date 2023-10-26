from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.get_db import get_db
from ..models.schedule_model import ScheduleModel, ScheduleModelResponse, ScheduleUpdateModel
import logic.controller.schedule_crud as schedule_crud

schedule_router = APIRouter(
    prefix="/schedules",
    tags=["Schedules"],
    dependencies=[Depends(get_db)]
)


@schedule_router.get("/",
                     response_model=List[ScheduleModelResponse],
                     summary="Get a list of all schedules")
def get_schedules(db: Session = Depends(get_db)):
    """
    Get a list of all schedules

    - **id**: Schedule's id
    - **start_date**: Schedule's start date
    - **finish_date**: Schedule's finish date
    - **state**: Schedule's state
    """
    return schedule_crud.get_schedules(db=db)


@schedule_router.get("/{schedule_id:int}",
                     response_model=ScheduleModelResponse,
                     summary="Get a schedule by id")
def get_schedule(schedule_id, db: Session = Depends(get_db)):
    """
    Get a schedule by id

    - **id**: Schedule's id
    """
    schedule_found = schedule_crud.get_schedule_by_id(
        db=db, schedule_id=schedule_id)
    if schedule_found:
        return schedule_found
    raise HTTPException(
        status_code=404, detail=f"Schedule with id: {schedule_id} not found")


@schedule_router.post("/",
                      response_model=ScheduleModelResponse,
                      summary="Create a new schedule")
def create_schedule(schedule: ScheduleModel, db: Session = Depends(get_db)):
    """
    Create a new schedule

    - **start_date**: Schedule's start date
    - **finish_date**: Schedule's finish date
    - **state**: Schedule's state
    """
    return schedule_crud.create_schedule(db=db, schedule=schedule)


@schedule_router.put("/{schedule_id:int}",
                     response_model=ScheduleModelResponse,
                     summary="Update a schedule by id")
def update_schedule(schedule_id, schedule: ScheduleUpdateModel, db: Session = Depends(get_db)):
    """
    Update a schedule by id

    - **id**: Schedule's id
    """
    schedule_found = schedule_crud.get_schedule_by_id(
        db=db, schedule_id=schedule_id)
    if schedule_found:
        return schedule_crud.update_schedule(db=db, schedule_id=schedule_id, schedule=schedule)
    raise HTTPException(
        status_code=404, detail=f"Schedule with id: {schedule_id} not found")


@schedule_router.delete("/{schedule_id:int}", summary="Delete a schedule by id")
def delete_schedule(schedule_id, db: Session = Depends(get_db)):
    """
    Delete a schedule by id

    - **id**: Schedule's id
    """
    schedule_found = schedule_crud.get_schedule_by_id(
        db=db, schedule_id=schedule_id)
    if schedule_found:
        return schedule_crud.delete_schedule(db=db, schedule_id=schedule_id)
    raise HTTPException(
        status_code=404, detail=f"Schedule with id: {schedule_id} not found")
