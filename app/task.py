from celery import Celery

_password = 'wX4do7Xscne6KJFSD7Shu3xJx3Pn2MxC1JJaQVaVzpxePC'
_url = 'localhost:6379'

broker_url = f'redis://:{_password}@{_url}/0'
result_backend = f'redis://:{_password}@{_url}/1'
app = Celery('tasks', broker=broker_url, backend=result_backend)


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)