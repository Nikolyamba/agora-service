import uvicorn
from fastapi import FastAPI
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from starlette.requests import Request

from api.auth import a_router
from api.rooms import r_router
from api.tokens import t_router
from services.limiter import limiter
from services.log import setup_logger

app = FastAPI()

app.include_router(a_router, prefix='/api')
app.include_router(t_router, prefix='/api')
app.include_router(r_router, prefix='/api')

app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

logger = setup_logger()

logger.info("Запуск приложения")

@app.get("/health")
@limiter.limit("5/minute")
async def healthcheck(request: Request):
    return {"status": "ok", "service": "AgoraService"}

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level='info', reload=True)