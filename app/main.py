from fastapi import FastAPI
from app.config import settings
from app.routes import router

app = FastAPI(title=settings.APP_NAME)

app.include_router(router)

# Намеренная типовая ошибка
@app.get("/")
def read_root() -> int:  # обещаем вернуть int, но возвращаем dict
    return {"message": "DevSecOps application is running"}
