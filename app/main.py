from fastapi import FastAPI
from app.config import settings
from app.routes import router

app = FastAPI(title=settings.APP_NAME)

app.include_router(router)


@app.get("/")
def root():
    return {"message": "DevSecOps application is running"}
