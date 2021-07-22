from .worker import celery_app
import logging.config

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
def send_data(value):
    log.warning("Adding %s" % value)
    return value


@celery_app.task
def get_data(value):
    log.warning("Getting %s" % value)
    return value

# celery_app.conf.task_routes = {
#     "app.celery_worker.test_celery": "test-queue"
# }
#
# celery_app.conf.update(task_track_started=True)
