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

# from fastapi_utils.timing import add_timing_middleware, record_timing

# from tortoise.contrib.fastapi import register_tortoise

from src.config.log_config import InterceptHandler
from src.config.ormar_settings import database

from src.config.settings import settings
from src.app import routers

# logging.basicConfig(handlers=[InterceptHandler()], level=0)
# logger.debug('Hello!')
# logger.add("logs_1.log", rotation="5Mb")
# logger.add(sys.stdout, format="[{time:HH:mm:ss}] <lvl>{message}</lvl>", level="DEBUG")


openapi_url = settings.openapi_url
docs_url = settings.docs_url
redoc_url = settings.redoc_url


hide_docs = settings.hide_docs

if hide_docs == True:
    openapi_url = None
    docs_url = None
    redoc_url = None


app = FastAPI(
    title=settings.project_name,
    description=settings.description,
    version=settings.version,
    openapi_url=openapi_url,
    docs_url=docs_url,
    redoc_url=redoc_url
)

app.state.database = database

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.backend_cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# add_timing_middleware(app, record=logger.info, prefix="app")

app.mount("/static", StaticFiles(directory="src/static"), name="static")
templates = Jinja2Templates(directory="src/templates")

# app.include_router(auth_router)
app.include_router(routers.api_router, prefix=settings.api_v1_str)


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


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


# # todo In production, it's strongly recommended to setup a migration system to update your SQL schemas
# register_tortoise(
#     app,
#     db_url=settings.DATABASE_URI,
#     modules={"models": settings.APPS_MODELS},
#     generate_schemas=False,
#     add_exception_handlers=True,
# )

if __name__ == "__main__":
    print(settings.dict())
    uvicorn.run("main:app", host=settings.server_host, port=settings.server_port, reload=True)
