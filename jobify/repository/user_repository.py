from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status
from ..utility.Hashing import Hashing

def create(request: schemas.UserIn, db: Session):
    if db.query(models.User).filter(models.User.email == request.email).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered."
        )
    new_data = models.User(
        username=request.username,
        email=request.email,
        password=Hashing.get_password_hash(request.password)
    )
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data

def get(id: int, db: Session):
    data = db.query(models.User).filter(models.User.id == id).first()
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {id} does not exist."
        )
    return data