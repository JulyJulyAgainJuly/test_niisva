from fastapi import FastAPI

from .celery_worker import log, task_get, task_set, task_delete


# теги
tags_metadata = [
    {
        'name': 'add',
        'description': 'Добавить запись в базу',
    },
    {
        'name': 'get',
        'description': 'Получить запись из базы',
    },
    {
        'name': 'update',
        'description': 'Изменить запись в базе',
    },
    {
        'name': 'get',
        'description': 'Получить запись из базы',
    }
]

# инициализация
app = FastAPI(
    title='API',
    description='API for Redis (+ Celery).\n1. Run redis-server.\n2. Run "celery_worker.py".\n3. Run "manage.py".',
    version='1.0.0',
    openapi_tags=tags_metadata
)


@app.get("/add")
async def add(key, value):
    """
    Get.
    :param key:
    :return:
    """
    log.warning('main.add RUN')
    task = task_set.delay(key=key, value=value)
    res = task.get()
    if res:
        # print(res)
        return res
    return {'msg': 'SOMETHING WRONG WITH task_set'}


@app.get("/get")
async def get(key):
    """
    Get.
    :param key:
    :return:
    """
    log.warning('main.get RUN')
    task = task_get.delay(key=key)
    res = task.get()
    if res:
        return res
    return {'msg': 'SOMETHING WRONG WITH task_get'}


@app.get("/update")
async def update(key, value):
    """
    Get.
    :param key:
    :return:
    """
    log.warning('main.update RUN')
    task = task_get.delay(key=key)
    res = task.get()
    if res:
        task = task_set.delay(key=key, value=value)
        res = task.get()
        if res:
            return res
        return {'msg': 'SOMETHING WRONG WITH task_set'}
    return {'msg': f'main.update THERE IS NO VALUE WITH KEY = {key}'}


@app.get("/delete")
async def delete(key):
    """
    Get.
    :param key:
    :return:
    """
    log.warning('main.delete RUN')
    task = task_delete.delay(key=key)
    res = task.get()
    if res:
        return res
    return {'msg': 'SOMETHING WRONG WITH task_delete'}
