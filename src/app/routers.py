from fastapi import APIRouter
from src.app.auth.api import auth_router
from src.app.user.endpoint import role  # , users, admin,
from src.app.user.endpoint import user_alchemy
# from src.app.handbook.endpoint.handbook import handbook_router
# from src.app.blog.routers import blog_router

api_router = APIRouter()

# api_router.include_router(auth_router, prefix='/auth', tags=["Login"])
api_router.include_router(user_alchemy.router, prefix='/user', tags=["User"])
# api_router.include_router(users.user_router, tags=["User"])
api_router.include_router(role.role_router, tags=["Person roles"])
# api_router.include_router(handbook_router, prefix="/handbook", tags=["Handbook"])
# # api_router.include_router(blog_router, prefix="/blog", tags=["blog"])
#
# api_router.include_router(admin.admin_router, prefix='/admin/user', tags=["Admin user"])
