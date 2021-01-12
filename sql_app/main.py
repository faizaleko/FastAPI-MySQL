from typing import List

import uvicorn
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException

from sql_app import models, schemas, crud
from sql_app.database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency


def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Learn FastAPI"}


@app.get("/users", response_model=List[schemas.Users])
def read_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users


@app.post("/user")
def create_user(user: schemas.UsersCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(
            status_code=400, detail="Username Already Registered")
    else:
        crud.create_user(db=db, user=user)
        return {"message": "Successfully Create User"}


@app.put("/user/{user_id}")
def update_user(user_id: str, user: schemas.UsersBase, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(
            status_code=400, detail="Username Already Registered")
    else:
        crud.update_user(db=db, user=user, id=user_id)
        return {"message": "Successfully Update User"}


@app.delete("/user/{user_id}")
def delete_user(user_id: str, db: Session = Depends(get_db)):
    db_user = crud.delete_user(db=db, id=user_id)
    if db_user:
        return {"message": "Successfully Delete User"}
    else:
        raise HTTPException(status_code=400, detail="Failed Delete User")
