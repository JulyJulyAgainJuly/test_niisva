import logging.config

from fastapi import FastAPI, BackgroundTasks

from app.celery.celery_app import celery_app

# http://127.0.0.1:8000/docs

# конфигурация логирования
CELERYD_HIJACK_ROOT_LOGGER = False

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

app = FastAPI()


def celery_on_message(body):
    log.warning(body)


def background_on_message(task):
    log.warning(task.get(on_message=celery_on_message, propagate=False))


@app.get("/get/{word}")
async def get(word: str, background_task: BackgroundTasks):
    """
    Get.
    :param word:
    :param background_task:
    :return:
    """
    task = celery_app.send_task("app.celery_worker.test_celery", args=[word])
    print(task)
    background_task.add_task(background_on_message, task)
    return {"message": "Word received"}


@app.post("/post")
async def post():
    pass
