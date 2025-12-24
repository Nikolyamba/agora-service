from fastapi import APIRouter, Header, HTTPException
from starlette.requests import Request

a_router = APIRouter(prefix='/auth') #a as auth

@a_router.post('/simple')
async def auth(request: Request, x_user_id: str = Header(..., alias="X-User-Id")) -> dict:
    if not x_user_id:
        raise HTTPException(status_code=401, detail='Header не был передан!')

    request.state.user_id = x_user_id

    return {'user_id': x_user_id, 'status_code': 200, 'detail': 'Вы успешно авторизовались'}
