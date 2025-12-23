import uvicorn
from fastapi import FastAPI

from api.auth import a_router

app = FastAPI()

app.include_router(a_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level='info', reload=True)