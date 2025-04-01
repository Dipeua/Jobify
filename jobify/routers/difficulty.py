from fastapi import APIRouter, status, HTTPException, Depends
from .. import models, schemas
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from ..repository import difficulty_repository

router = APIRouter(
	prefix="/difficulty",
	tags=["Difficulty"]
)

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.DifficultyOut])
async def get_difficulties(db: Session = Depends(get_db)):
	return difficulty_repository.get_all(db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.DifficultyOut)
async def show_difficulty(id: int, db: Session = Depends(get_db)):
	return difficulty_repository.get(id, db)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.DifficultyOut)
async def create_difficulty(request: schemas.DifficultyIn, db: Session = Depends(get_db)):
	return difficulty_repository.create(request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_difficulty(id: int, db: Session = Depends(get_db)):
	return difficulty_repository.delete(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_difficulty(id: int, request: schemas.DifficultyIn, db: Session = Depends(get_db)):
	return difficulty_repository.update(id, request, db)