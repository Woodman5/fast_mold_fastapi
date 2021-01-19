from fastapi_users.authentication import CookieAuthentication, JWTAuthentication
from fastapi_users.db import TortoiseUserDatabase
from fastapi_users import FastAPIUsers

from models.db_users import UserModel
from schemas.sch_users import User, UserCreate, UserUpdate, UserDB


SECRET = "cg#p$g+j9tax!#a3cup@1$8obt2_+&k3q+pmu)5%asj6yjpkag"

user_db = TortoiseUserDatabase(UserDB, UserModel)


cookie_authentication = CookieAuthentication(secret=SECRET, lifetime_seconds=3600)
jwt_authentication = JWTAuthentication(secret=SECRET, lifetime_seconds=3600)

auth_backends = [
    cookie_authentication,
    jwt_authentication
]

fastapi_users = FastAPIUsers(
    user_db,
    auth_backends,
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)
