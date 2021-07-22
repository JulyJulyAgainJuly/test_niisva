import uvicorn

# В одном терминале запускаем сервер Редис:
# redis-server PycharmProjects/test_niisva/redis.conf
# Во втором терминале (с виртуальной средой Python) запускаем celery:
#
# http://127.0.0.1:8080/docs

if __name__ == '__main__':
    uvicorn.run(
        "app.main:app",
        host='localhost',
        port=8080,
        reload=True
    )
