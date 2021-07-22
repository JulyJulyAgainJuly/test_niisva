from fastapi import FastAPI, Form, Request
from fastapi.responses import PlainTextResponse, HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import random
import uvicorn

# from .celery.worker import celery_app
# from worker import logging_task


# http://127.0.0.1:8000/docs


# класс  модели данных Pydantic
class Task(BaseModel):
    key: str
    value: str = None


tags_metadata = [
    {
        'name': 'items',
        'description': 'items',
    }
]

# инициализация
app = FastAPI(
    title='Mini api',
    description='This is my mini api (description)',
    version='1.0.0',
    openapi_tags=tags_metadata
)

# монтирование статической папки для обслуживания статических файлов
app.mount("/static", StaticFiles(directory="static"), name="static")

# экземпляр шаблона Jinja2 для возврата веб-страниц через шаблонизатор
templates = Jinja2Templates(directory="templates")


# @app.post('/get_task')
# def send_task():
#     logging_task.delay()
# req = request.json()
# try:
#     int(req["n1"])
# except TypeError:
#     return {"status": 1, "message": Wrong type}
# # We use celery delay method in order to enqueue the task with the given parameters
# add.delay(n1, n2)

# def celery_on_message(body):
#     log.warning(body)
#
#
# def background_on_message(task):
#     log.warning(task.get(on_message=celery_on_message, propagate=False))
#
#
# @app.get("/get/{word}")
# async def get(word: str, background_task: BackgroundTasks):
#     """
#     Get.
#     :param word:
#     :param background_task:
#     :return:
#     """
#     task = celery_app.send_task("app.celery_worker.test_celery", args=[word])
#     print(task)
#     background_task.add_task(background_on_message, task)
#     return {"message": "Word received"}
#
#
# @app.post("/post")
# async def post():
#     pass


# @app.get("/", response_class=PlainTextResponse)
# async def hello():
#     return "Hello World!"


# @app.get("/", response_class=HTMLResponse)
# async def hello(request: Request):
#     return templates.TemplateResponse("index.html",
#                                       {"request": request, "message": "Hello, world"})


@app.get('/get_data', response_class=JSONResponse)
async def get_webpage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Contact Us"})


@app.get("/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
