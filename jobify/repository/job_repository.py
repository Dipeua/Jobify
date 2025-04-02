from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session, skip: int = 0, limit: int = 10):
    datas = db.query(models.Job).offset(skip).limit(limit).all()
    if not datas:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="No jobs found in the database."
        )
    return datas

def get(id: int, db: Session):
    data = db.query(models.Job).filter(models.Job.id == id).first()
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Job with ID {id} does not exist."
        )
    return data  # Automatically includes nested relationships due to JobOut schema


def create(request: schemas.JobIn, db: Session):  # Fixed schema reference
    new_data = models.Job(
        title=request.title,
        description=request.description,
        salary=request.salary,
        difficulty_id=request.difficulty_id,
        region_id=request.region_id
    )
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data  # Automatically includes nested relationships due to JobOut schema


def delete(id: int, db: Session):
    data_delete = db.query(models.Job).filter(models.Job.id == id)
    if not data_delete.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Cannot delete. Job with ID {id} does not exist."
        )
    data_delete.delete(synchronize_session=False)
    db.commit()
    return {"message": f"Job with ID {id} has been successfully deleted."}

def update(id: int, request: schemas.JobIn, db: Session):  # Fixed schema reference
    data_update = db.query(models.Job).filter(models.Job.id == id)
    if not data_update.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Cannot update. Job with ID {id} does not exist."
        )
    data_update.update({
        'title': request.title,
        'description': request.description,
        'salary': request.salary,
        'difficulty_id': request.difficulty_id,
        'region_id': request.region_id
    })
    db.commit()
    return {"message": f"Job with ID {id} has been successfully updated."}