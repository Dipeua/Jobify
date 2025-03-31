from fastapi import APIRouter, status, HTTPException, Depends
from .. import models, schemas
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
	prefix="/regions",
	tags=["Regions"]
)

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.RegionOut])
async def get_regions(db: Session = Depends(get_db)):
    regions = db.query(models.Region).all()
    if not regions:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No regions found in the database.")
    return regions

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.RegionOut)
async def show_region(id: int, db: Session = Depends(get_db)):
    region = db.query(models.Region).filter(models.Region.id == id).first()
    if not region:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Region with ID {id} does not exist.")
    return region

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.RegionOut)
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

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_region(id: int, db: Session = Depends(get_db)):
    region_delete = db.query(models.Region).filter(models.Region.id == id)
    if not region_delete.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cannot delete. Region with ID {id} does not exist.")
    region_delete.delete(synchronize_session=False)
    db.commit()
    return {"message": f"Region with ID {id} has been successfully deleted."}

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
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