from sqlalchemy.orm import Session

from database.db_models import Client
from ..models.client_model import ClientModel


def get_clients(db: Session):
    return db.query(Client).all()


def get_client_by_id(db: Session, client_id: int):
    return db.query(Client).filter(Client.id == client_id).first()


def create_client(db: Session, client: ClientModel):
    db_client = Client(
        name=client.name,
        last_name=client.last_name,
        phone=client.phone,
        mail=client.mail,
    )
    db.add(db_client)
    db.commit()
    db.flush(db_client)
    return db_client


def update_client(db: Session, client_id: int, client: ClientModel):
    db_client = db.query(Client).filter(Client.id == client_id).first()
    if client.name:
        db_client.name = client.name
    if client.last_name:
        db_client.last_name = client.last_name
    if client.phone:
        db_client.phone = client.phone
    if client.mail:
        db_client.mail = client.mail
    db.commit()
    db.flush(db_client)
    return db_client


def delete_client(db: Session, client_id: int):
    db_client = db.query(Client).filter(Client.id == client_id).first()
    db.delete(db_client)
    db.commit()
    return {"message": f"Client {db_client.name} deleted"}
