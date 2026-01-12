from fastapi import Header, HTTPException
from app.config import settings

# Намеренно добавляем плохие практики
import os, sys  # множественные импорты в одной строке
some_var = 1
some_var = 2  # переопределение переменной

def verify_api_key(x_api_key: str = Header(...)):
    try:  # bare except
        pass
    except:
        pass
        
    if x_api_key != settings.API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
