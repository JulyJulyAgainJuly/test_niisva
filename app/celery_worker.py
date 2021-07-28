from celery import Celery
import logging.config
import redis

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
_url = 'localhost:6379'

broker_url = f'redis://:{_password}@{_url}/1'
result_backend = f'redis://:{_password}@{_url}/0'
celery_app = Celery('app', broker=broker_url, backend=result_backend)
r = redis.Redis(db=0, password=_password)


@celery_app.task
def get_task(key):
    log.warning('Get data from DB for key')
    r.get(key)
    return True


@celery_app.task(name="add_task")
def add_task(key, value):
    log.warning('Set data to DB')
    return {key: value}


@celery_app.task
def update_task(key, value):
    log.warning('Updating data in DB for key')
    return {key: value}


@celery_app.task
def delete_task(self):
    log.warning('Deleting data from DB for key')
    # log.warning('Request: {0!r}'.format(self.request))
    return self.request


if __name__ == '__main__':
    celery_app.start(['worker'])
