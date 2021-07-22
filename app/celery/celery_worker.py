import logging.config

from app.worker import celery_app

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


@celery_app.task
def add(x, y):
    res = x + y
    log.warning("Adding %s + %s, res: %s" % (x, y, res))
    return res


# @celery_app.task(ask_test=True)
# def test_celery(word: str) -> str:
#     for i in range(1, 11):
#         sleep(1)
#         current_task.update_state(state='PROGRESS',
#                                   meta={'process_percent': i*10})
#     return f"test task return {word}"
