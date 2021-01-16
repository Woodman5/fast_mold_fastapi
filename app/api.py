from typing import List

from fastapi import FastAPI, Request
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from models import user, model
from fastapi_users.db import TortoiseBaseUserModel, TortoiseUserDatabase
from fastapi_users.authentication import CookieAuthentication
from fastapi_users import FastAPIUsers
from tortoise import fields
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator

from .database import engine

from starlette.middleware.sessions import SessionMiddleware

# old salt - PHNWzjeCTTft,   ajlgbfhkqlwhg98435y

DATABASE_URL = 'sqlite://db.sqlite3'
HASH_ROUNDS = 150000

SECRET = "SECRET"


auth_backends = []

cookie_authentication = CookieAuthentication(secret=SECRET, lifetime_seconds=3600)

auth_backends.append(cookie_authentication)


model.Base.metadata.create_all(bind=engine)


class UserModel(TortoiseBaseUserModel):
    id = fields.IntField(pk=True)
    user_uuid = fields.UUIDField(generated=False)
    username = fields.CharField(index=True, unique=True, null=False, max_length=255)
    email = fields.CharField(unique=True, null=False, max_length=255)
    password = fields.CharField(null=False, max_length=255)
    is_active = fields.BooleanField(default=True, null=False)
    is_superuser = fields.BooleanField(default=False, null=False)
    # is_verified = fields.BooleanField(default=False, null=False)

    class Meta:
        table = "UserAccounts_user"


User_Pydantic = pydantic_model_creator(UserModel, name="User")

user_db = TortoiseUserDatabase(user.UserDB, UserModel)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# app.add_middleware(PyInstrumentProfilerMiddleware)
app.add_middleware(SessionMiddleware, session_cookie='SSID-5', secret_key='eglhfvfyfyuf896r6f78ege')

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated='auto', pbkdf2_sha256__rounds=HASH_ROUNDS)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

templates = Jinja2Templates(directory="templates")


# Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)


# def get_password_hash(password):
#     return pwd_context.hash(password)


# def get_user(username: str, db):
#     db_user = crud.get_user_by_username(db, username=username)
#     if db_user:
#         # user_dict = db[username]
#         # return UserInDB(**user_dict)
#         # return schemas.UserInDB(db_user)
#         return db_user


# def authenticate_user(username: str, password: str, db):
#     user = get_user(username, db)
#     if not user:
#         return False
#     if not verify_password(password, user.password):
#         return False
#     return user


# def create_access_token():
#     return 'some_very_strong_token'
#
#
# async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#
#     username: str = 'Woodman5'
#     token_data = schemas.TokenData(username=username)
#     user = get_user(token_data.username, db)
#
#     if user is None:
#         raise credentials_exception
#     return user


# @app.post("/token", response_model=schemas.Token, tags=['Auth'])
# async def login_for_access_token(  # response: Response,
#         request: Request,
#         form_data: OAuth2PasswordRequestForm = Depends(),
#         db: Session = Depends(get_db),
# ):
#     user = authenticate_user(form_data.username, form_data.password, db)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token = create_access_token()
#     request.session["user_id"] = user.id
#     # response.set_cookie(key="SSID",
#     #                     value="fake-cookie-session-value",
#     #                     max_age=2592000,
#     #                     path='/users',
#     #                     httponly=True,
#     #                     samesite='strict')
#     return {"access_token": access_token, "token_type": "bearer"}


# @app.get("/users/", response_model=List[schemas.User], tags=['Users'])
# def read_users(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     print(request.cookies.get('SSID'))
#     print(request.session)
#     print(request.client.host)
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users


# @app.get("/users/{user_id}", response_model=schemas.User, tags=['Users'])
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_id(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @app.get("/users/me/", response_model=schemas.UserInDB, tags=['Users'])
# async def read_users_me(current_user: schemas.User = Depends(get_current_user)):
#     return current_user


@app.get("/", response_class=HTMLResponse, tags=['Root'])
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "id": 42})


@app.get("/users", response_model=List[User_Pydantic])
async def get_users():
    return await User_Pydantic.from_queryset(UserModel.all())


register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={"models": ['app.api']},
    generate_schemas=True,
)

fastapi_users = FastAPIUsers(
    user_db,
    auth_backends,
    user.User,
    user.UserCreate,
    user.UserUpdate,
    user.UserDB,
)


def on_after_register(user: user.UserDB, request: Request):
    print(f"User {user.id} has registered.")


def on_after_forgot_password(user: user.UserDB, token: str, request: Request):
    print(f"User {user.id} has forgot their password. Reset token: {token}")


def after_verification_request(user: user.UserDB, token: str, request: Request):
    print(f"Verification requested for user {user.id}. Verification token: {token}")


app.include_router(
    fastapi_users.get_auth_router(cookie_authentication), prefix="/auth/cook", tags=["auth"]
)

app.include_router(
    fastapi_users.get_register_router(on_after_register), prefix="/auth", tags=["auth"]
)

app.include_router(
    fastapi_users.get_reset_password_router(
        SECRET, after_forgot_password=on_after_forgot_password
    ),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_verify_router(
        SECRET, after_verification_request=after_verification_request
    ),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(fastapi_users.get_users_router(), prefix="/users", tags=["users"])