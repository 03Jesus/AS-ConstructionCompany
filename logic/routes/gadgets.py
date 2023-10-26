from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.get_db import get_db
from ..models.gadget_model import GadgetModel, GadgetModelResponse, GadgetUpdateModel
import logic.controller.gadgets_crud as gadgets_crud

gadget_router = APIRouter(
    prefix="/gadgets",
    tags=["Gadgets"],
    dependencies=[Depends(get_db)]
)


@gadget_router.get("/",
                   response_model=List[GadgetModelResponse],
                   summary="Get a list of all gadgets")
def get_gadgets(db: Session = Depends(get_db)):
    """
    Get a list of all gadgets

    - **id**: Gadget's id
    - **name**: Gadget's name
    - **type**: Gadget's type
    - **state**: Gadget's state
    """
    return gadgets_crud.get_gadgets(db=db)


@gadget_router.get("/{gadget_id:int}",
                   response_model=GadgetModelResponse,
                   summary="Get a gadget by id")
def get_gadget(gadget_id, db: Session = Depends(get_db)):
    """
    Get a gadget by id

    - **id**: Gadget's id
    - **name**: Gadget's name
    - **type**: Gadget's type
    - **state**: Gadget's state
    """
    gadget_found = gadgets_crud.get_gadget_by_id(
        db=db, gadget_id=gadget_id)
    if gadget_found:
        return gadget_found
    raise HTTPException(
        status_code=404, detail=f"Gadget with id: {gadget_id} not found")


@gadget_router.post("/",
                    response_model=GadgetModelResponse,
                    summary="Create a new gadget")
def create_gadget(gadget: GadgetModel, db: Session = Depends(get_db)):
    """
    Create a new gadget

    - **name**: Gadget's name
    - **type**: Gadget's type
    - **state**: Gadget's state
    """
    return gadgets_crud.create_gadget(db=db, gadget=gadget)


@gadget_router.put("/{gadget_id:int}",
                   response_model=GadgetModelResponse,
                   summary="Update a gadget")
def update_gadget(gadget_id, gadget: GadgetUpdateModel, db: Session = Depends(get_db)):
    """
    Update a gadget

    - **name**: Gadget's name
    - **type**: Gadget's type
    - **state**: Gadget's state
    """
    gadget_found = gadgets_crud.get_gadget_by_id(
        db=db, gadget_id=gadget_id)
    if gadget_found:
        return gadgets_crud.update_gadget(db=db, gadget_id=gadget_id, gadget=gadget)
    raise HTTPException(
        status_code=404, detail=f"Gadget with id: {gadget_id} not found")


@gadget_router.delete("/{gadget_id:int}", summary="Delete a gadget by id")
def delete_gadget(gadget_id, db: Session = Depends(get_db)):
    """
    Delete a gadget by id

    - **id**: Gadget's id
    """
    gadget_found = gadgets_crud.get_gadget_by_id(
        db=db, gadget_id=gadget_id)
    if gadget_found:
        return gadgets_crud.delete_gadget(db=db, gadget_id=gadget_id)
    raise HTTPException(
        status_code=404, detail=f"Gadget with id: {gadget_id} not found")
