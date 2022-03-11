import schemas
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from repository import user


router = APIRouter(
    tags=['Users']
)

@router.post('/user', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)


@router.get('/user/{id}', response_model=schemas.ShowUser)
def get_user(id, db: Session = Depends(get_db)):
    return user.get_user(id, db)
