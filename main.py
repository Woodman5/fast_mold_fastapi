import logging
from logging import handlers

import uvicorn

import sys
from loguru import logger
from log_config import InterceptHandler

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise

from auth.router import auth_router
from schemas.sch_users import User
from models.db_users import UserModel
from typing import List

DATABASE_URL = 'sqlite://db.sqlite3'

logging.basicConfig(handlers=[InterceptHandler()], level=0)
logger.debug('Hello!')
logger.add("logs_1.log", rotation="5Mb")
logger.add(sys.stdout, format="[{time:HH:mm:ss}] <lvl>{message}</lvl>", level="DEBUG")


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(auth_router)


@app.get("/", response_class=HTMLResponse, tags=['Root'])
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "id": 42})


@app.get("/users", response_model=List[User])
async def get_users():
    return await UserModel.all().prefetch_related('role')


@app.get("/me", response_model=User)
async def get_me():
    return await UserModel.get(id=8).prefetch_related('role')


# todo In production, it's strongly recommended to setup a migration system to update your SQL schemas
register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={"models": [
                        "models.db_users",
                        # "models.db_model",
                        # "models.db_materials",
                        ]},
    generate_schemas=False,
)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=9000, reload=True)
