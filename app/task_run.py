from celery_worker import task_get, task_set, task_delete


# sig = add.s(2, 8)
# res = sig.delay()
# print(type(res))
# print(res.get(timeout=1, propagate=False))
# print(res.state)

task = task_set.delay(key='key1', value='srvvsfgj123456789')
# print(task.id)
print(task.get())
task = task_delete.delay(key='key')
# task = task_get.delay(key='key1')
print(task.get())
# task.forget()
# word = 'fghfgh'
# task = send_task('task.test_celery', args=[word])
# print(task.get())
# print(add.tasks)
