from celery import Celery


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


@celery_app.task
def logging_task(self):
    return self.request


@celery_app.task
def logging_task(self):
    return self.request


@celery_app.task
def update(key, value):

    return 200


@celery_app.task
def logging_task(self):
    return self.request


@celery_app.task
def logging_task(self):
    # log.warning('Request: {0!r}'.format(self.request))
    return self.request
