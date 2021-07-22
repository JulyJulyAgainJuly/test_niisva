from fastapi import FastAPI
from pydantic import BaseModel

# from .celery.worker import celery_app
from app.worker import logging_task

# http://127.0.0.1:8000/docs


class Task(BaseModel):
    key: str
    value: str = None


app = FastAPI()


@app.post('/get_task')
def send_task():
    logging_task.delay()
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


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
