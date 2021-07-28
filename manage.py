import uvicorn

"""
Задание: реализовать API-сервер для работы с хранилищем Redis (и брокер, и бэк), используя Celery.

Python 3.8.10

В одном терминале запускаем сервер Редис:
    redis-server PycharmProjects/test_niisva/redis.conf
    
Во втором терминале запускаем celery:
    python app/celery_worker.py
    
!!! После запуска воркер первым делом чистит базу-бэкенд !!!
    
В третьем терминале запускаем manage.py:
    python manage.py
    
Пример использования:
    http://127.0.0.1:8080/add?key=KEY1&value=SOME_VALUE - добавление записи
    http://127.0.0.1:8080/get?key=KEY1 - вывод записи
    http://127.0.0.1:8080/update?key=KEY1&value=SOME_NEW_VALUE - изменение записи
    http://127.0.0.1:8080/delete?key=KEY1 - удаление записи

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
