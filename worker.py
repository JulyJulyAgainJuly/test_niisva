from celery import Celery
import logging.config


celery_app = Celery(
        __name__,
        backend="redis://:wX4do7Xscne6KJFSD7Shu3xJx3Pn2MxC1JJaQVaVzpxePC@localhost:6379/1",
        broker="redis://:wX4do7Xscne6KJFSD7Shu3xJx3Pn2MxC1JJaQVaVzpxePC@localhost:6379/0"
    )

celery_app.conf.task_routes = {
    "app.celery.tasks.logging_task": "test-queue"
}

celery_app.conf.update(task_track_started=True)

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


# @celery_app.task
# def send_data(value):
#     log.warning("Adding %s" % value)
#     return value
#
#
# @celery_app.task
# def get_data(value):
#     log.warning("Getting %s" % value)
#     return value


@celery_app.task
def logging_task(self):
    log.warning('Request: {0!r}'.format(self.request))
