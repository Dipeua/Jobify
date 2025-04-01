from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status
from ..utility.Hashing import Hashing
from ..utility.JWToken import JWToken

def login(request: schemas.AuthIn, db: Session):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user or not Hashing.verify_password(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid credentials."
        )
    access_token = JWToken.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type":"bearer"}