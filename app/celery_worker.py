from celery import Celery
import logging.config


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
celery_app = Celery('app')
celery_app.config_from_object('celeryconfig')

# celery_app.conf.task_routes = {
#     "app.celery.tasks.logging_task": "test-queue"
# }
#
# celery_app.conf.update(task_track_started=True)


@celery_app.task
def get_task(self):
    log.warning('Get data from DB for key')
    return self.request


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
