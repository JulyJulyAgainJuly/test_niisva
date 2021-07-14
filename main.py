from fastapi import FastAPI

app = FastAPI()


# uvicorn main:app --reload
# http://127.0.0.1:8000
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc
# http://127.0.0.1:8000/openapi.json


@app.get("/")
async def root():
    return {"message": "Hello World"}
