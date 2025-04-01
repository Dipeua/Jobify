from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    datas = db.query(models.Difficulty).all()
    if not datas:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No difficulties found in the database."
        )
    return datas

def get(id: int, db: Session):
    data = db.query(models.Difficulty).filter(models.Difficulty.id == id).first()
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Difficulty with ID {id} does not exist."
        )
    return data

def create(request: schemas.DifficultyIn, db: Session):
    new_data = models.Difficulty(level=request.level.capitalize())
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data

def delete(id: int, db: Session):
    data_delete = db.query(models.Difficulty).filter(models.Difficulty.id == id)
    if not data_delete.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Difficulty with ID {id} does not exist."
        )
    data_delete.delete(synchronize_session=False)
    db.commit()
    return {"detail": f"Difficulty with ID {id} successfully deleted."}

def update(id: int, request: schemas.DifficultyIn, db: Session):
    data_update = db.query(models.Difficulty).filter(models.Difficulty.id == id)
    if not data_update.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Difficulty with ID {id} does not exist."
        )
    data_update.update({'level': request.level.capitalize()})
    db.commit()
    return {"detail": f"Difficulty with ID {id} successfully updated."}