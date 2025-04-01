from fastapi import APIRouter, status, Depends, HTTPException
from .. import models, schemas
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import auth_repository
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
	tags=["Authentication"]
)

@router.post('/login', status_code=status.HTTP_200_OK, response_model=schemas.Token)
async def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return auth_repository.login(request, db)