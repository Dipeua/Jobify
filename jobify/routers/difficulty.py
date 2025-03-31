from fastapi import APIRouter, status, HTTPException, Depends
from .. import models, schemas
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
	prefix="/difficulty",
	tags=["Difficulty"]
)

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.DifficultyOut])
async def get_difficulties(db: Session = Depends(get_db)):
	datas = db.query(models.Difficulty).all()
	if not datas:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No difficulties found in the database.")
	return datas

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.DifficultyOut)
async def show_difficulty(id: int, db: Session = Depends(get_db)):
	data = db.query(models.Difficulty).filter(models.Difficulty.id == id).first()
	if not data:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Difficulty with ID {id} does not exist.")
	return data

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.DifficultyOut)
async def create_difficulty(request: schemas.DifficultyIn, db: Session = Depends(get_db)):
	new_data = models.Difficulty(level=request.level.capitalize())
	db.add(new_data)
	db.commit()
	db.refresh(new_data)
	return new_data

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_difficulty(id: int, db: Session = Depends(get_db)):
	data_delete = db.query(models.Difficulty).filter(models.Difficulty.id == id)
	if not data_delete.first():
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cannot delete. Difficulty with ID {id} does not exist.")
	data_delete.delete(synchronize_session=False)
	db.commit()
	return {"message": f"Difficulty with ID {id} has been successfully deleted."}

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_difficulty(id: int, request: schemas.DifficultyIn, db: Session = Depends(get_db)):
	data_update = db.query(models.Difficulty).filter(models.Difficulty.id == id)
	if not data_update.first():
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cannot update. Difficulty with ID {id} does not exist.")
	data_update.update({'level': request.level.capitalize()})
	db.commit()
	return {"message": f"Difficulty with ID {id} has been successfully updated."}