import logging
import sys
from typing import List

import uvicorn

from loguru import logger

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from starlette.middleware.sessions import SessionMiddleware

from tortoise.contrib.fastapi import register_tortoise

from src.config.log_config import InterceptHandler

from src.config import settings
from src.app import routers

from src.app.user.schemas import User_Pydantic


logging.basicConfig(handlers=[InterceptHandler()], level=0)
logger.debug('Hello!')
logger.add("logs_1.log", rotation="5Mb")
logger.add(sys.stdout, format="[{time:HH:mm:ss}] <lvl>{message}</lvl>", level="DEBUG")


app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)

app.mount("/static", StaticFiles(directory="src/static"), name="static")
templates = Jinja2Templates(directory="src/templates")

# app.include_router(auth_router)
app.include_router(routers.api_router, prefix=settings.API_V1_STR)


@app.get("/", response_class=HTMLResponse, tags=['Root'])
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "id": 42})


# @app.get("/users", response_model=List[User])
# async def get_users():
#     return await UserModel.all().prefetch_related('role')
#
#
# @app.get("/me", response_model=User)
# async def get_me():
#     return await UserModel.get(id=8).prefetch_related('role')


# todo In production, it's strongly recommended to setup a migration system to update your SQL schemas
register_tortoise(
    app,
    db_url=settings.DATABASE_URI,
    modules={"models": settings.APPS_MODELS},
    generate_schemas=False,
    add_exception_handlers=True,
)

print(User_Pydantic.schema_json(indent=4))

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=9000, reload=True)
