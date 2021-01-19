from sqlalchemy.orm import Session
from datetime import datetime

from app import schemas
import schemas


def get_user_by_id(db: Session, user_id: int):
    return db.query(schemas.User).filter(schemas.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(schemas.User).filter(schemas.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(schemas.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserInDB):
    fake_hashed_password = user.password + "_notreallyhashed"
    db_user = schemas.User(
        email=user.email,
        username=user.username,
        hashed_password=fake_hashed_password,
        phone=user.phone,
        date_joined=datetime.now(),
        role_id=4
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()
#
#
# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item