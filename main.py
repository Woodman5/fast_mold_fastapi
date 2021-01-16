import uvicorn

from fastapi import FastAPI, Request

from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise


DATABASE_URL = 'sqlite://db.sqlite3'

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse, tags=['Root'])
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "id": 42})


register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={"models": [
                        # "models.user",
                        "models.model",
                        "models.materials",
                        ]},
    generate_schemas=True,
)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=9000, reload=True)
