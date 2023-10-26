from sqlalchemy.orm import Session

from database.db_models import Gadget, Schedule
from ..models.gadget_model import GadgetModel, GadgetUpdateModel
from .projects_crud import verify_if_record_exists


def get_gadgets(db: Session):
    return db.query(Gadget).all()


def get_gadget_by_id(db: Session, gadget_id: int):
    return db.query(Gadget).filter(Gadget.id == gadget_id).first()


def create_gadget(db: Session, gadget: GadgetModel):
    if gadget.schedule_id:
        verify_if_record_exists(db=db, model=Schedule,
                                model_id=gadget.schedule_id)
    db_gadget = Gadget(
        name=gadget.name,
        type=gadget.type,
        state=gadget.state,
        schedule_id=gadget.schedule_id,
    )
    db.add(db_gadget)
    db.commit()
    db.flush(db_gadget)
    return db_gadget


def update_gadget(db: Session, gadget_id: int, gadget: GadgetUpdateModel):
    db_gadget = db.query(Gadget).filter(Gadget.id == gadget_id).first()
    if gadget.name:
        db_gadget.name = gadget.name
    if gadget.type:
        db_gadget.type = gadget.type
    if gadget.state:
        db_gadget.state = gadget.state
    if gadget.schedule_id:
        db_gadget.schedule_id = gadget.schedule_id
    db.commit()
    db.flush(db_gadget)
    return db_gadget


def delete_gadget(db: Session, gadget_id: int):
    db_gadget = db.query(Gadget).filter(Gadget.id == gadget_id).first()
    db.delete(db_gadget)
    db.commit()
    return {"message": f"Gadget {db_gadget.name} deleted"}
