from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.get_db import get_db
from ..models.client_model import ClientModel, ClientModelResponse
import logic.controller.client_crud as client_crud

client_router = APIRouter(
    prefix="/clients",
    tags=["Clients"],
    dependencies=[Depends(get_db)]
)


@client_router.get("/",
                   response_model=List[ClientModelResponse],
                   summary="Get a list of all clients")
def get_clients(db: Session = Depends(get_db)):
    """
    Get a list of all clients

    - **id**: Client's id
    - **name**: Client's name
    - **last_name**: Client's last name
    - **mail**: Client's mail
    - **phone**: Client's phone
    """
    return client_crud.get_clients(db=db)


@client_router.get("/{client_id:int}",
                   response_model=ClientModelResponse,
                   summary="Get a client by id")
def get_client(client_id, db: Session = Depends(get_db)):
    """
    Get a client by id

    - **id**: Client's id
    """
    client_found = client_crud.get_client_by_id(
        db=db, client_id=client_id)
    if client_found:
        return client_found
    raise HTTPException(
        status_code=404, detail=f"Client with id: {client_id} not found")


@client_router.post("/",
                    response_model=ClientModelResponse,
                    summary="Create a new client")
def create_client(client: ClientModel, db: Session = Depends(get_db)):
    """
    Create a new client

    - **name**: Client's name
    - **last_name**: Client's last name
    - **mail**: Client's mail
    - **phone**: Client's phone
    """
    return client_crud.create_client(db=db, client=client)


@client_router.put("/{client_id:int}",
                   response_model=ClientModelResponse,
                   summary="Update a client by id")
def update_client(client_id, client: ClientModel, db: Session = Depends(get_db)):
    """
    Update a client by id

    - **id**: Client's id
    - **name**: Client's name
    - **last_name**: Client's last name
    - **mail**: Client's mail
    - **phone**: Client's phone
    """
    client_found = client_crud.get_client_by_id(
        db=db, client_id=client_id)
    if client_found:
        return client_crud.update_client(db=db, client_id=client_id, client=client)
    raise HTTPException(
        status_code=404, detail=f"Client with id: {client_id} not found")


@client_router.delete("/{client_id:int}",
                      summary="Delete a client by id")
def delete_client(client_id, db: Session = Depends(get_db)):
    """
    Delete a client by id

    - **id**: Client's id
    """
    client_found = client_crud.get_client_by_id(
        db=db, client_id=client_id)
    if client_found:
        return client_crud.delete_client(db=db, client_id=client_id)
    raise HTTPException(
        status_code=404, detail=f"Client with id: {client_id} not found")
