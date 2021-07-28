from celery.execute import send_task
# from task import test_celery
from task import get_, set_


# https://docs.celeryproject.org/en/stable/userguide/index.html#guide
# sig = add.s(2, 8)
# res = sig.delay()
# print(type(res))
# print(res.get(timeout=1, propagate=False))
# print(res.state)

task = set_.delay(somekey='key1', someword='srvvsfgj123456789')
print(task.id)
print(task.get())
task = get_.delay(somekey='key1')
print(task.get())
# print(task.get())
# task.forget()
# word = 'fghfgh'
# task = send_task('task.test_celery', args=[word])
# print(task.get())
# print(add.tasks)
