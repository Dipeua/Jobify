from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status
from ..utility.Hashing import Hashing

def login(request: schemas.AuthIn, db: Session):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user or not Hashing.verify_password(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid credentials."
        )
    # Generate the token and return

    return user