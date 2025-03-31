from fastapi import FastAPI, Depends, status, HTTPException
from .database import engine, get_db
from . import models, schemas
from sqlalchemy.orm import Session
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
	title='Jobify API',
	description='The dynamic platform to discover and apply for the best job opportunities in Cameroon. Find a job that fits your skills, preferences, and location. Simple, fast, and efficient.',
	version='0.1'
)

@app.get('/')
def home():
	return {'greeting': "Welcome to Jobify API! Let\'s find your dream job."}

@app.get('/difficulty', tags=["Difficulty"], status_code=status.HTTP_200_OK, response_model=List[schemas.DifficultyOut])
async def get(db: Session = Depends(get_db)):
	datas = db.query(models.Difficulty).all()
	if not datas:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No difficulties found in the database.")
	return datas

@app.get('/difficulty/{id}', tags=["Difficulty"], status_code=status.HTTP_200_OK, response_model=schemas.DifficultyOut)
async def show(id: int, db: Session = Depends(get_db)):
	data = db.query(models.Difficulty).filter(models.Difficulty.id == id).first()
	if not data:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Difficulty with ID {id} does not exist.")
	return data

@app.post('/difficulty', tags=["Difficulty"], status_code=status.HTTP_201_CREATED, response_model=schemas.DifficultyOut)
async def create(request: schemas.DifficultyIn, db: Session = Depends(get_db)):
	new_data = models.Difficulty(level=request.level.capitalize())
	db.add(new_data)
	db.commit()
	db.refresh(new_data)
	return new_data

@app.delete('/difficulty/{id}', tags=["Difficulty"], status_code=status.HTTP_204_NO_CONTENT)
async def destroy(id: int, db: Session = Depends(get_db)):
	data_delete = db.query(models.Difficulty).filter(models.Difficulty.id == id)
	if not data_delete.first():
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cannot delete. Difficulty with ID {id} does not exist.")
	data_delete.delete(synchronize_session=False)
	db.commit()
	return {"message": f"Difficulty with ID {id} has been successfully deleted."}

@app.put('/difficulty/{id}', tags=["Difficulty"], status_code=status.HTTP_202_ACCEPTED)
async def update(id: int, request: schemas.DifficultyIn, db: Session = Depends(get_db)):
	data_update = db.query(models.Difficulty).filter(models.Difficulty.id == id)
	if not data_update.first():
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cannot update. Difficulty with ID {id} does not exist.")
	data_update.update({'level': request.level.capitalize()})
	db.commit()
	return {"message": f"Difficulty with ID {id} has been successfully updated."}
