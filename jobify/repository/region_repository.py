from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    datas = db.query(models.Region).all()
    if not datas:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="No regions found in the database."
        )
    return datas

def get(id: int, db: Session):
    data = db.query(models.Region).filter(models.Region.id == id).first()
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Region with ID {id} does not exist."
        )
    return data

def create(request: schemas.RegionIn, db: Session):
    new_data = models.Region(
        code=request.code.upper(),
        name=request.name.capitalize(),
        region_image_url=request.region_image_url
    )
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data

def delete(id: int, db: Session):
    data_delete = db.query(models.Region).filter(models.Region.id == id)
    if not data_delete.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Cannot delete. Region with ID {id} does not exist."
        )
    data_delete.delete(synchronize_session=False)
    db.commit()
    return {"message": f"Region with ID {id} has been successfully deleted."}

def update(id: int, request: schemas.RegionIn, db: Session):
    data_update = db.query(models.Region).filter(models.Region.id == id)
    if not data_update.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Cannot update. Region with ID {id} does not exist."
        )
    data_update.update({
        'code': request.code.upper(),
        'name': request.name.capitalize(),
        'region_image_url': request.region_image_url
    })
    db.commit()
    return {"message": f"Region with ID {id} has been successfully updated."}
