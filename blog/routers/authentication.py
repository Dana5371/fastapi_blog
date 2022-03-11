from email.policy import HTTP
from fastapi import APIRouter, Depends, HTTPException, status
import schemas
from sqlalchemy.orm import Session
from database import get_db
import models
from hashing import Hash

router = APIRouter(
    tags=['Authentication']
)



@router.post('/login', status_code=status.HTTP_200_OK)
def login(request: schemas.Login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"User with username {request.username} does not exist")
    if not Hash.verify(user.password, request.password):
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Password for user {request.username} not correct")
    #generate a jwt token and return it
    return user