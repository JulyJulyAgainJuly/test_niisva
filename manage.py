import uvicorn

"""
Python 3.8.10

В одном терминале запускаем сервер Редис:
    redis-server PycharmProjects/test_niisva/redis.conf
Во втором терминале (с виртуальной средой Python) запускаем celery (из корня, где "manage.py"):
    celery -A worker worker --loglevel=INFO
В третьем терминале запускаем manage.py:
    python manage.py

Swagger UI    http://127.0.0.1:8080/docs
ReDoc         http://127.0.0.1:8080/redoc
"""

if __name__ == '__main__':
    uvicorn.run(
        "app.main:app",
        host='localhost',
        port=8080,
        reload=True
    )
