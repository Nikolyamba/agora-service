from fastapi import Header, HTTPException
from starlette.requests import Request

async def get_current_user(request: Request, x_user_id: str = Header(..., alias="X-User-Id")) -> str:
    if not x_user_id:
        raise HTTPException(status_code=401, detail='Header не был передан!')

    request.state.user_id = x_user_id

    return x_user_id