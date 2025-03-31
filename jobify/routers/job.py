from fastapi import APIRouter, status, HTTPException, Depends
from .. import models, schemas
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
	prefix="/jobs",
	tags=["Jobs"]
)

@router.post('/', tags=["Jobs"], status_code=status.HTTP_201_CREATED, response_model=schemas.JobOut)
async def create_job(request: schemas.JobIn, db: Session = Depends(get_db)):
    new_job = models.Job(
        title=request.title,
        description=request.description,
        salary=request.salary,
        difficulty_id=request.difficulty_id,
        region_id=request.region_id
    )
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job  # Automatically includes nested relationships due to JobOut schema

@router.get('/{id}', tags=["Jobs"], status_code=status.HTTP_200_OK, response_model=schemas.JobOut)
async def get_job_by_id(id: int, db: Session = Depends(get_db)):
    job = db.query(models.Job).filter(models.Job.id == id).first()
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Job with ID {id} does not exist.")
    return job  # Automatically includes nested relationships due to JobOut schema

@router.get('/', tags=["Jobs"], status_code=status.HTTP_200_OK, response_model=List[schemas.JobOut])
async def get_all_jobs(db: Session = Depends(get_db)):
    jobs = db.query(models.Job).all()
    if not jobs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No jobs found in the database.")
    return jobs

@router.delete('/{id}', tags=["Jobs"], status_code=status.HTTP_204_NO_CONTENT)
async def delete_job(id: int, db: Session = Depends(get_db)):
    job_delete = db.query(models.Job).filter(models.Job.id == id)
    if not job_delete.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cannot delete. Job with ID {id} does not exist.")
    job_delete.delete(synchronize_session=False)
    db.commit()
    return {"message": f"Job with ID {id} has been successfully deleted."}

@router.put('/{id}', tags=["Jobs"], status_code=status.HTTP_202_ACCEPTED)
async def update_job(id: int, request: schemas.JobIn, db: Session = Depends(get_db)):
    job_update = db.query(models.Job).filter(models.Job.id == id)
    if not job_update.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cannot update. Job with ID {id} does not exist.")
    job_update.update({
        'title': request.title,
        'description': request.description,
        'salary': request.salary,
        'difficulty_id': request.difficulty_id,
        'region_id': request.region_id
    })
    db.commit()
    return {"message": f"Job with ID {id} has been successfully updated."}