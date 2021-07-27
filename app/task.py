from celery import Celery
from time import sleep

from celery import current_task



_password = 'wX4do7Xscne6KJFSD7Shu3xJx3Pn2MxC1JJaQVaVzpxePC'
_url = 'localhost:6379'

broker_url = f'redis://:{_password}@{_url}/1'
result_backend = f'redis://:{_password}@{_url}/0'
app = Celery('task', broker=broker_url, backend=result_backend)


@app.task(bind=True)
def add(self, x, y):
    # print(f'Adding {x} + {y}')
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)


@app.task(acks_late=True)
def test_celery(word: str) -> str:
    for i in range(1, 11):
        sleep(1)
        current_task.update_state(state='PROGRESS',
                                  meta={'process_percent': i*10})
    return f"test task return {word}"


if __name__ == '__main__':
    app.start()
