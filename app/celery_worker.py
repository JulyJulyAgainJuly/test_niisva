from celery import Celery
import logging.config
import redis
import json

log = logging.getLogger(__name__)

_password = 'wX4do7Xscne6KJFSD7Shu3xJx3Pn2MxC1JJaQVaVzpxePC'
_host = 'localhost'
_port = '6379'

broker_url = f'redis://:{_password}@{_host}:{_port}/1'
result_backend = f'redis://:{_password}@{_host}:{_port}/0'
celery_app = Celery('app', broker=broker_url, backend=result_backend)
r = redis.Redis(db=0, host=_host, port=_port, password=_password)


@celery_app.task(name="task_get")
def task_get(key):
    assert type(key) == bytes or type(key) == str or type(key) == int or type(key) == float, 'WRONG KEY TYPE'
    log.warning('task.task_get RUN')
    val = json.loads(r.get(key))
    # print(val)
    return json.dumps({key: val})


@celery_app.task(name="task_set")
def task_set(key, value):
    assert type(key) == bytes or type(key) == str or type(key) == int or type(key) == float, 'WRONG KEY TYPE'
    log.warning('task.task_set RUN')
    r.set(key, json.dumps(value))
    return json.dumps({key: value})


@celery_app.task(name="task_delete")
def task_delete(key):
    assert type(key) == bytes or type(key) == str or type(key) == int or type(key) == float, 'WRONG KEY TYPE'
    log.warning('task.task_delete RUN')
    val = r.get(key)
    if val:
        r.delete(key)
        return True
    else:
        log.error(f'task.task_delete THERE IS NO VALUE WITH KEY = {key}')
        return False


if __name__ == '__main__':
    r.flushdb()
    celery_app.start(['worker'])
