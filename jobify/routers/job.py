from fastapi import APIRouter, status, HTTPException, Depends
from .. import models, schemas
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from ..repository import job_repository
from ..utility import Oauth2

router = APIRouter(
	prefix="/jobs",
	tags=["Jobs"]
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.JobOut)
async def create_job(request: schemas.JobIn, db: Session = Depends(get_db), current_user: schemas.User = Depends(Oauth2.get_current_user)):
    return job_repository.create(request, db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.JobOut)
async def get_job(id: int, db: Session = Depends(get_db)):
    return job_repository.get(id, db)

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.JobOut])
async def get_jobs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return job_repository.get_all(db, skip=skip, limit=limit)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_job(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(Oauth2.get_current_user)):
    return job_repository.delete(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_job(id: int, request: schemas.JobIn, db: Session = Depends(get_db), current_user: schemas.User = Depends(Oauth2.get_current_user)):
    return job_repository.update(id, request, db)