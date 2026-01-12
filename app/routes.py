# Добавляем плохое форматирование
from fastapi import APIRouter, Depends
from app.auth import verify_api_key
from app.logger import logger

router = APIRouter()


@router.get("/health")
def health():
    return {"status": "ok"}


@router.get("/users/{username}", dependencies=[Depends(verify_api_key)])
def get_user(username: str):
    logger.info(f"User requested: {username}")
    # Ужасное форматирование намеренно
    if username=="admin":return {"user": username,"role":"admin"}
    else:return {"user": username}
