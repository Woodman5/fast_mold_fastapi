from typing import List, Union

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from src.config import settings
# from src.utils import send_new_account_email
from src.config.sqlalchemy_conf import get_db
from src.app.auth.permissions import get_superuser, get_user

from src.app.user.models import User, Role
from src.app.user.schemas_alchemy import UserFull, UserBase, UserInDB
from src.app.user.service import user_service


router = APIRouter()


@router.get("/", response_model=List[UserFull])
async def read_users(
    skip: int = 0,
    limit: int = 100,
    current_user=Depends(get_superuser),
):
    """
    Retrieve users.
    """
    users = await user_service.get_multi(skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=UserFull)
async def read_user_by_id(
    user_id: int,
    # current_user: DBUser = Depends(get_user),
):
    """
    Get a specific user by id.
    """
    user = await user_service.get(pk=user_id)
    # if user == current_user:
    #     return user
    # if not crud_user.user.is_superuser(current_user):
    #     raise HTTPException(
    #         status_code=400, detail="The user doesn't have enough privileges"
    #     )
    return user


@router.post("/")  # , response_model=UserFull)
async def create_user(
    user_in: UserInDB,
    # current_user: DBUser = Depends(get_current_active_superuser),
):
    """
    Create new user.
    """
    user = await user_service.get_by_email(email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username or email already exists.",
        )
    user = await user_service.create(obj_in=user_in)
    # if config.EMAILS_ENABLED and user_in.email:
    #     send_new_account_email(
    #         email_to=user_in.email, username=user_in.email, password=user_in.password
    #     )
    return user


# @router.put("/me", response_model=UserCreate)
# def update_user_me(
#     *,
#     db: Session = Depends(get_db),
#     password: str = Body(None),
#     full_name: str = Body(None),
#     email: EmailStr = Body(None),
#     current_user: DBUser = Depends(get_user),
# ):
#     """
#     Update own user.
#     """
#     current_user_data = jsonable_encoder(current_user)
#     user_in = UserCreate(**current_user_data)
#     if password is not None:
#         user_in.password = password
#     if full_name is not None:
#         user_in.full_name = full_name
#     if email is not None:
#         user_in.email = email
#     user = crud_user.user.update(db, db_obj=current_user, obj_in=user_in)
#     return user


# @router.get("/me", response_model=UserCreate)
# def read_user_me(
#     db: Session = Depends(get_db),
#     current_user: DBUser = Depends(get_user),
# ):
#     """
#     Get current user.
#     """
#     return current_user


# @router.post("/open", response_model=UserCreate)
# def create_user_open(
#     *,
#     db: Session = Depends(get_db),
#     password: str = Body(...),
#     email: EmailStr = Body(...),
#     full_name: str = Body(None),
# ):
#     """
#     Create new user without the need to be logged in.
#     """
#     if not settings.USERS_OPEN_REGISTRATION:
#         raise HTTPException(
#             status_code=403,
#             detail="Open user registration is forbidden on this server",
#         )
#     user = crud_user.user.get_by_email(db, email=email)
#     if user:
#         raise HTTPException(
#             status_code=400,
#             detail="The user with this username already exists in the system",
#         )
#     user_in = UserCreate(password=password, email=email, full_name=full_name)
#     user = crud_user.user.create(db, obj_in=user_in)
#     return user


# @router.put("/{user_id}", response_model=UserCreate)
# def update_user(
#     *,
#     db: Session = Depends(get_db),
#     user_id: int,
#     user_in: UserCreate,
#     current_user: DBUser = Depends(get_superuser),
# ):
#     """
#     Update a user.
#     """
#     user = crud_user.user.get(db, id=user_id)
#     if not user:
#         raise HTTPException(
#             status_code=404,
#             detail="The user with this username does not exist in the system",
#         )
#     user = crud_user.user.update(db, db_obj=user, obj_in=user_in)
#     return user
