from typing import List

from fastapi import APIRouter, Depends, Body, Form

from src.app.auth.permissions import get_user

from src.app.user.models import User
from src.app.user.schemas_alchemy import UserFull, UserInDB
from src.app.user.service import user_service
from src.app.base.router_base import get_customized_router


user_router = get_customized_router('/user',
                                    user_service,
                                    UserFull,
                                    create_schema=UserInDB,
                                    update_schema=UserFull,
                                    name='User'
                                    )


# @user_router.get('/me', response_model=User)
# def user_me(current_user: UserModel = Depends(get_user)):
#     """ Get current user by user"""
#     if current_user:
#         # current_user.fetch_related('role')
#         return current_user
