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
celery_app = Celery(__name__)
celery_app.config_from_object('celeryconfig')

# celery_app.conf.task_routes = {
#     "app.celery.tasks.logging_task": "test-queue"
# }
#
# celery_app.conf.update(task_track_started=True)


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


# @celery_app.task
# def logging_task():
#     return {"message": "OK"}


@celery_app.task
def get_all(self):
    log.warning('Get all data from DB')
    return self.request


@celery_app.task
def get_data(self):
    log.warning('Get data from DB for key')
    return self.request


@celery_app.task
def set_data(key, value):
    log.warning('Set data to DB')
    return {key: value}


@celery_app.task
def update_data(key, value):
    log.warning('Updating data in DB for key')
    return {key: value}


@celery_app.task
def delete_data(self):
    log.warning('Deleting data from DB for key')
    # log.warning('Request: {0!r}'.format(self.request))
    return self.request


if __name__ == '__main__':
    celery_app.start(['worker'])
