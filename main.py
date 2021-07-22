import uvicorn

# http://127.0.0.1:8080/docs

if __name__ == '__main__':
    uvicorn.run(
        "app.app:app",
        host='localhost',
        port=8080,
        reload=True
    )
