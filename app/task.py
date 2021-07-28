import logging.config
import redis
from celery import Celery
from uuid import uuid4


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
            'filename': f'{__name__}.log',
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

_password = 'wX4do7Xscne6KJFSD7Shu3xJx3Pn2MxC1JJaQVaVzpxePC'
_host = 'localhost'
_port = '6379'

broker_url = f'redis://:{_password}@{_host}:{_port}/1'
result_backend = f'redis://:{_password}@{_host}:{_port}/0'
app = Celery('task', broker=broker_url, backend=result_backend)
r = redis.Redis(db=0, host=_host, port=_port, password=_password)


@app.task()
def get_(somekey):
    log.warning(f'Getting {somekey}')
    val = r.get(somekey)
    print(val)
    return str(val)


@app.task()
def set_(someword: str, somekey=uuid4()):
    log.warning(f'Adding {somekey}: {someword}')
    r.mset({somekey: someword})
    return True


# @app.task(acks_late=True)
# def test_celery(word: str) -> str:
#     for i in range(1, 11):
#         sleep(1)
#         current_task.update_state(state='PROGRESS',
#                                   meta={'process_percent': i*10})
#     return f"test task return {word}"


if __name__ == '__main__':
    app.start()
