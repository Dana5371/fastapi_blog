from typing import List
from fastapi import Depends, FastAPI, status, Response, HTTPException
import models
import schemas
from database import engine, get_db
from sqlalchemy.orm import Session
from routers import blog, user
from hashing import *

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)















