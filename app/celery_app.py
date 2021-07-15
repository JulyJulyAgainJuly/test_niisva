from celery import Celery

celery_app = Celery(
        "worker",
        backend="redis://:wX4do7Xscne6KJFSD7Shu3xJx3Pn2MxC1JJaQVaVzpxePC@localhost:6379/1",
        broker="redis://:wX4do7Xscne6KJFSD7Shu3xJx3Pn2MxC1JJaQVaVzpxePC@localhost:6379/0"
    )
celery_app.conf.task_routes = {
    "app.celery_worker.test_celery": "test-queue"
}

celery_app.conf.update(task_track_started=True)
