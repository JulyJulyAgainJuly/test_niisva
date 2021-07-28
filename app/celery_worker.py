from celery import Celery
import logging.config
import redis
import json

CELERYD_HIJACK_ROOT_LOGGER = False

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

# настройка Celery:
# celery_app = Celery('app')
# celery_app.config_from_object('celeryconfig')

_password = 'wX4do7Xscne6KJFSD7Shu3xJx3Pn2MxC1JJaQVaVzpxePC'
_host = 'localhost'
_port = '6379'

broker_url = f'redis://:{_password}@{_host}:{_port}/1'
result_backend = f'redis://:{_password}@{_host}:{_port}/0'
celery_app = Celery('app', broker=broker_url, backend=result_backend)
r = redis.Redis(db=0, host=_host, port=_port, password=_password)


@celery_app.task
def task_get(key):
    assert type(key) == bytes or type(key) == str or type(key) == int or type(key) == float, 'WRONG KEY TYPE'
    log.warning('task.task_get')
    val = json.loads(r.get(key))
    return {key: val}


@celery_app.task(name="add_task")
def task_set(key, value):
    assert type(key) == bytes or type(key) == str or type(key) == int or type(key) == float, 'WRONG KEY TYPE'
    log.warning('task.task_set')
    r.set(key, json.dumps(value))
    return {key: value}


@celery_app.task
def task_delete(key):
    assert type(key) == bytes or type(key) == str or type(key) == int or type(key) == float, 'WRONG KEY TYPE'
    log.warning('task.task_delete')
    r.delete(key)
    return True


if __name__ == '__main__':
    r.flushdb()
    celery_app.start(['worker'])
