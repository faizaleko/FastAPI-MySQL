import uuid
from sqlalchemy.orm import Session

from . import models, schemas


def get_user_by_username(db: Session, username: str):
    return db.query(models.Users).filter(models.Users.username == username).first()


def get_users(db: Session):
    return db.query(models.Users).all()


def create_user(db: Session, user: schemas.UsersCreate):
    db_user = models.Users(
        id=str(uuid.uuid4().hex[0:16]),
        username=user.username,
        password=user.password,
        fullname=user.fullname,
        email=user.email,
        telp=user.telp
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user: schemas.UsersBase, id: str):
    db_user = db.query(models.Users).filter(models.Users.id == id).first()
    db_user.username = user.username
    db_user.fullname = user.fullname
    db_user.email = user.email
    db_user.telp = user.telp
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, id: str):
    db_user = db.query(models.Users).filter(models.Users.id == id).first()
    db.delete(db_user)
    db.commit()
    return db_user
