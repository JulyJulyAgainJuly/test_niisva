from fastapi import FastAPI, Form, Request
from fastapi.responses import PlainTextResponse, HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import logging.config
import random
import uvicorn

# from .celery.worker import celery_app
from app.worker import logging_task


# класс  модели данных Pydantic
class Task(BaseModel):
    key: str
    value: str = None


# теги
tags_metadata = [
    {
        'name': 'get_all_data',
        'description': 'Get all data from Redis DB.',
    },
    {
        'name': 'get_data',
        'description': 'Get data from Redis DB for key.',
    },
    {
        'name': 'set_data',
        'description': 'Set data to Redis DB for key.',
    },
    {
        'name': 'update_data',
        'description': 'Update data to Redis DB for key.',
    },
    {
        'name': 'delete_data',
        'description': 'Delete data to Redis DB for key.',
    }
]

# инициализация
app = FastAPI(
    title='API',
    description='API for Redis (+ Celery).\n1. Run redis-server.\n2. Run celery.\n3. Run "manage.py".',
    version='1.0.0',
    openapi_tags=tags_metadata
)

# монтирование статической папки для обслуживания статических файлов
app.mount("/static", StaticFiles(directory="static"), name="static")

# экземпляр шаблона Jinja2 для возврата веб-страниц через шаблонизатор
templates = Jinja2Templates(directory="templates")

# настройка логирования:
log_config = {
    'version': 1,
    'formatters': {
        'basic': {
            'format': '%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s',
            'datefmt': '%d-%b-%y %H:%M:%S'
        }
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'formatter': 'basic',
            'filename': 'app.log',
            'mode': 'w',
        },
    },
    'loggers': {
        '': {
            'level': 'NOTSET',
            'handlers': ['file_handler']
        }
    }
}

logging.config.dictConfig(log_config)
log = logging.getLogger(__name__)


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


@app.get('/get_all_data', response_class=JSONResponse, tags=["get_all_data"])
async def show_everything():
    task = logging_task("app.celery_worker.logging_task")
    print(task)
    return {"status": "200", "message": "OK"}


@app.get('/get_data', response_class=JSONResponse, tags=["get_data"])
async def show_data_for_key(key):
    task = logging_task("app.celery_worker.logging_task")
    print(task)
    return {"status": "200", "message": "OK"}


@app.get('/set_data', response_class=JSONResponse, tags=["set_data"])
async def input_new_data(value):
    task = logging_task("app.celery_worker.test_celery", args=[value])
    print(task)
    return {"status": "200", "message": "OK"}


@app.get('/update_data', response_class=JSONResponse, tags=["update_data"])
async def update_data_for_key(key, value):
    task = logging_task("app.celery_worker.test_celery", args=[key, value])
    print(task)
    return {"status": "200", "message": "OK"}


@app.get('/delete_data', response_class=JSONResponse, tags=["delete_data"])
async def delete_data_for_key(key):
    task = logging_task("app.celery_worker.test_celery", args=[key])
    print(task)
    return {"status": "200", "message": "OK"}
