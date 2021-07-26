from task import add, mul, xsum

# https://docs.celeryproject.org/en/stable/userguide/index.html#guide
res = add.delay('fdgdgdfgdf', '123')
print(res.state)
# print(result.traceback)
print(type(res))
# print(result.key())
# print(result.ready())
print(res.get(timeout=1, propagate=False))
print(res.state)
print(res.id)
res.update('123456789')
print(res.get(timeout=1, propagate=False))
# result.delete()
# print(result.get(timeout=1))

# result2 = dlt.delay(str(result))
# print(result2.ready())
# print(result2.get(timeout=1))
