from fastapi import APIRouter, status, Depends
from .. import schemas
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import user_repository

router = APIRouter(
	prefix="/user",
	tags=["User"]
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
async def create_user(request: schemas.UserIn, db: Session = Depends(get_db)):
	return user_repository.create(request, db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.UserOut)
async def show_user(id: int, db: Session = Depends(get_db)):
	return user_repository.get(id, db)