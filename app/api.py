from typing import List

from fastapi import Depends, FastAPI, HTTPException, status, Response, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from . import models, schemas, crud
from .database import SessionLocal, engine

from starlette.middleware.sessions import SessionMiddleware

from fastapi_profiler.profiler_middleware import PyInstrumentProfilerMiddleware

# old salt - PHNWzjeCTTft,   ajlgbfhkqlwhg98435y


HASH_ROUNDS = 150000

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# app.add_middleware(PyInstrumentProfilerMiddleware)
app.add_middleware(SessionMiddleware, session_cookie='SSID-5', secret_key='eglhfvfyfyuf896r6f78ege')

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated='auto', pbkdf2_sha256__rounds=HASH_ROUNDS)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

templates = Jinja2Templates(directory="templates")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(username: str, db):
    db_user = crud.get_user_by_username(db, username=username)
    if db_user:
        # user_dict = db[username]
        # return UserInDB(**user_dict)
        # return schemas.UserInDB(db_user)
        return db_user


def authenticate_user(username: str, password: str, db):
    user = get_user(username, db)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token():
    return 'some_very_strong_token'


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    username: str = 'Woodman5'
    token_data = schemas.TokenData(username=username)
    user = get_user(token_data.username, db)

    if user is None:
        raise credentials_exception
    return user


@app.post("/token", response_model=schemas.Token, tags=['Auth'])
async def login_for_access_token(  # response: Response,
        request: Request,
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db),
):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token()
    request.session["user_id"] = user.id
    # response.set_cookie(key="SSID",
    #                     value="fake-cookie-session-value",
    #                     max_age=2592000,
    #                     path='/users',
    #                     httponly=True,
    #                     samesite='strict')
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/", response_model=List[schemas.User], tags=['Users'])
def read_users(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    print(request.cookies.get('SSID'))
    print(request.session)
    print(request.client.host)
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User, tags=['Users'])
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.get("/users/me/", response_model=schemas.UserInDB, tags=['Users'])
async def read_users_me(current_user: schemas.User = Depends(get_current_user)):
    return current_user


@app.get("/", response_class=HTMLResponse, tags=['Root'])
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "id": 42})
