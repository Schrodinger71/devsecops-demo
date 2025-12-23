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
    return {"user": username}

# НЕБЕЗОПАСНЫЙ КОД ДЛЯ ДЕМОНСТРАЦИИ
@router.get("/vulnerable/users")
def get_user_unsafe(username: str):
    query = f"SELECT * FROM users WHERE name = '{username}'"
    return {"message": "This endpoint is vulnerable to SQL injection"}
