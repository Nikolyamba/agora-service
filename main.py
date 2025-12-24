import uvicorn
from fastapi import FastAPI

from api.auth import a_router
from api.rooms import r_router
from api.tokens import t_router

app = FastAPI()

app.include_router(a_router, prefix='/api')
app.include_router(t_router, prefix='/api')
app.include_router(r_router, prefix='/api')

@app.get("/health")
async def healthcheck():
    return {"status": "ok", "service": "AgoraService"}

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level='info', reload=True)