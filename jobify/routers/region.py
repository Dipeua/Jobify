from fastapi import APIRouter, status, HTTPException, Depends
from .. import models, schemas
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from ..repository import region_repository
from ..utility import Oauth2

router = APIRouter(
	prefix="/regions",
	tags=["Regions"]
)

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.RegionOut])
async def get_regions(db: Session = Depends(get_db), current_user: schemas.User = Depends(Oauth2.get_current_user)):
    return region_repository.get_all(db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.RegionOut)
async def show_region(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(Oauth2.get_current_user)):
    return region_repository.get(id, db)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.RegionOut)
async def create_region(request: schemas.RegionIn, db: Session = Depends(get_db), current_user: schemas.User = Depends(Oauth2.get_current_user)):
    return region_repository.create(request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_region(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(Oauth2.get_current_user)):
    return region_repository.delete(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_region(id: int, request: schemas.RegionIn, db: Session = Depends(get_db), current_user: schemas.User = Depends(Oauth2.get_current_user)):
    return region_repository.update(id, request, db)