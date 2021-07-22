from app.worker import celery_app
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
