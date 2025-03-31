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

# Difficulty

@app.get('/difficulty', tags=["Difficulty"], status_code=status.HTTP_200_OK, response_model=List[schemas.DifficultyOut])
async def get_difficulties(db: Session = Depends(get_db)):
	datas = db.query(models.Difficulty).all()
	if not datas:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No difficulties found in the database.")
	return datas

@app.get('/difficulty/{id}', tags=["Difficulty"], status_code=status.HTTP_200_OK, response_model=schemas.DifficultyOut)
async def show_difficulty(id: int, db: Session = Depends(get_db)):
	data = db.query(models.Difficulty).filter(models.Difficulty.id == id).first()
	if not data:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Difficulty with ID {id} does not exist.")
	return data

@app.post('/difficulty', tags=["Difficulty"], status_code=status.HTTP_201_CREATED, response_model=schemas.DifficultyOut)
async def create_difficulty(request: schemas.DifficultyIn, db: Session = Depends(get_db)):
	new_data = models.Difficulty(level=request.level.capitalize())
	db.add(new_data)
	db.commit()
	db.refresh(new_data)
	return new_data

@app.delete('/difficulty/{id}', tags=["Difficulty"], status_code=status.HTTP_204_NO_CONTENT)
async def delete_difficulty(id: int, db: Session = Depends(get_db)):
	data_delete = db.query(models.Difficulty).filter(models.Difficulty.id == id)
	if not data_delete.first():
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cannot delete. Difficulty with ID {id} does not exist.")
	data_delete.delete(synchronize_session=False)
	db.commit()
	return {"message": f"Difficulty with ID {id} has been successfully deleted."}

@app.put('/difficulty/{id}', tags=["Difficulty"], status_code=status.HTTP_202_ACCEPTED)
async def update_difficulty(id: int, request: schemas.DifficultyIn, db: Session = Depends(get_db)):
	data_update = db.query(models.Difficulty).filter(models.Difficulty.id == id)
	if not data_update.first():
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cannot update. Difficulty with ID {id} does not exist.")
	data_update.update({'level': request.level.capitalize()})
	db.commit()
	return {"message": f"Difficulty with ID {id} has been successfully updated."}

# Regions

@app.get('/regions', tags=["Regions"], status_code=status.HTTP_200_OK, response_model=List[schemas.RegionOut])
async def get_regions(db: Session = Depends(get_db)):
    regions = db.query(models.Region).all()
    if not regions:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No regions found in the database.")
    return regions

@app.get('/regions/{id}', tags=["Regions"], status_code=status.HTTP_200_OK, response_model=schemas.RegionOut)
async def show_region(id: int, db: Session = Depends(get_db)):
    region = db.query(models.Region).filter(models.Region.id == id).first()
    if not region:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Region with ID {id} does not exist.")
    return region

@app.post('/regions', tags=["Regions"], status_code=status.HTTP_201_CREATED, response_model=schemas.RegionOut)
async def create_region(request: schemas.RegionIn, db: Session = Depends(get_db)):
    new_region = models.Region(
        code=request.code.upper(),
        name=request.name.capitalize(),
        region_image_url=request.region_image_url
    )
    db.add(new_region)
    db.commit()
    db.refresh(new_region)
    return new_region

@app.delete('/regions/{id}', tags=["Regions"], status_code=status.HTTP_204_NO_CONTENT)
async def delete_region(id: int, db: Session = Depends(get_db)):
    region_delete = db.query(models.Region).filter(models.Region.id == id)
    if not region_delete.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cannot delete. Region with ID {id} does not exist.")
    region_delete.delete(synchronize_session=False)
    db.commit()
    return {"message": f"Region with ID {id} has been successfully deleted."}

@app.put('/regions/{id}', tags=["Regions"], status_code=status.HTTP_202_ACCEPTED)
async def update_region(id: int, request: schemas.RegionIn, db: Session = Depends(get_db)):
    region_update = db.query(models.Region).filter(models.Region.id == id)
    if not region_update.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cannot update. Region with ID {id} does not exist.")
    region_update.update({
        'code': request.code.upper(),
        'name': request.name.capitalize(),
        'region_image_url': request.region_image_url
    })
    db.commit()
    return {"message": f"Region with ID {id} has been successfully updated."}

# Jobs

@app.post('/jobs', tags=["Jobs"], status_code=status.HTTP_201_CREATED, response_model=schemas.JobOut)
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

@app.get('/jobs/{id}', tags=["Jobs"], status_code=status.HTTP_200_OK, response_model=schemas.JobOut)
async def get_job_by_id(id: int, db: Session = Depends(get_db)):
    job = db.query(models.Job).filter(models.Job.id == id).first()
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Job with ID {id} does not exist.")
    return job  # Automatically includes nested relationships due to JobOut schema

@app.get('/jobs', tags=["Jobs"], status_code=status.HTTP_200_OK, response_model=List[schemas.JobOut])
async def get_all_jobs(db: Session = Depends(get_db)):
    jobs = db.query(models.Job).all()
    if not jobs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No jobs found in the database.")
    return jobs

@app.delete('/jobs/{id}', tags=["Jobs"], status_code=status.HTTP_204_NO_CONTENT)
async def delete_job(id: int, db: Session = Depends(get_db)):
    job_delete = db.query(models.Job).filter(models.Job.id == id)
    if not job_delete.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cannot delete. Job with ID {id} does not exist.")
    job_delete.delete(synchronize_session=False)
    db.commit()
    return {"message": f"Job with ID {id} has been successfully deleted."}

@app.put('/jobs/{id}', tags=["Jobs"], status_code=status.HTTP_202_ACCEPTED)
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