from fastapi import FastAPI\
    # , Form, Request
from fastapi.responses import JSONResponse\
    # , PlainTextResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import json

from app.celery_worker import log, get_all, get_data, set_data, update_data, delete_data


# класс модели данных Pydantic
class Task(BaseModel):
    key: str
    value: str = None


# теги
tags_metadata = [
    {
        'name': 'get',
        'description': 'Get data from Redis DB.',
    },
    {
        'name': 'post',
        'description': 'Put/Change/Delete data in Redis DB.',
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
# app.mount("/static", StaticFiles(directory="static"), name="static")

# экземпляр шаблона Jinja2 для возврата веб-страниц через шаблонизатор
# templates = Jinja2Templates(directory="templates")


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


@app.get('/get_data/{key}', response_class=JSONResponse, tags=["get"])
async def show_data_in_json(key=None):
    if key:
        task = get_data("app.celery_worker.get_data", args=[key])
        log.warning('Get for key')
    else:
        task = get_all("app.celery_worker.get_all")
        log.warning('Get all')
    print(task)
    return json.dumps({"status": "200", "message": "OK"})


@app.post('/post_data', response_class=JSONResponse, tags=["post"])
async def set_data_to_db(key=None, value=None):
    if key & value:
        task = update_data("app.celery_worker.update_data", args=[value])
        log.warning('Update existing data in DB')
    elif not key & value:
        task = set_data("app.celery_worker.set_data", args=[key, value])
        log.warning('Set new data to DB')
    elif not value & key:
        task = delete_data("app.celery_worker.delete_data", args=[key])
        log.warning('Deleting existing data from DB')
    else:
        log.error('WRONG PARAMETERS')
        return {"message": "ERROR. Wrong parameters"}
    print(task)
    return json.dumps({"status": "200", "message": "OK"})


# @app.get('/get_all_data', response_class=JSONResponse, tags=["get_all_data"])
# async def show_everything():
#     task = get_all("app.celery_worker.get_all")
#     log.warning('')
#     print(task)
#     return {"status": "200", "message": "OK"}
#
#
# @app.get('/get_data', response_class=JSONResponse, tags=["get_data"])
# async def show_data_for_key(key):
#     task = get_data("app.celery_worker.get_data")
#     log.warning('')
#     print(task)
#     return {"status": "200", "message": "OK"}
#
#
# @app.get('/set_data', response_class=JSONResponse, tags=["set_data"])
# async def input_new_data(key, value):
#     task = set_data("app.celery_worker.set_data", args=[key, value])
#     log.warning('UPDATE')
#     print(task)
#     return {"status": "200", "message": "OK"}
#
#
# @app.get('/update_data', response_class=JSONResponse, tags=["update_data"])
# async def update_data_for_key(key, value):
#     task = update_data("app.celery_worker.update_data", args=[key, value])
#     log.warning('')
#     print(task)
#     return {"status": "200", "message": "OK"}
#
#
# @app.get('/delete_data', response_class=JSONResponse, tags=["delete_data"])
# async def delete_data_for_key(key):
#     task = delete_data("app.celery_worker.delete_data", args=[key])
#     log.warning('')
#     print(task)
#     return {"status": "200", "message": "OK"}
