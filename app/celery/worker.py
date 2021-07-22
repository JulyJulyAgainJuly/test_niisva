from celery import Celery


celery_app = Celery(
        __name__,
        backend="redis://:wX4do7Xscne6KJFSD7Shu3xJx3Pn2MxC1JJaQVaVzpxePC@localhost:6379/1",
        broker="redis://:wX4do7Xscne6KJFSD7Shu3xJx3Pn2MxC1JJaQVaVzpxePC@localhost:6379/0"
    )