import pickle
import sqlite3
import subprocess
import os
import yaml
import xml.etree.ElementTree as ET
from passlib.context import CryptContext
from fastapi import APIRouter, Depends, Query
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

# ==================== БЕЗОПАСНАЯ ВЕРСИЯ (для сравнения) ====================
@router.get("/safe/sql-parameterized")
def safe_sql(username: str = Query(...)):
    """Безопасная версия с параметризованными запросами"""
    conn = sqlite3.connect(':memory:')
    conn.execute('CREATE TABLE users (id INTEGER, name TEXT)')
    conn.execute("INSERT INTO users VALUES (1, 'admin')")
    
    # БЕЗОПАСНО: параметризованный запрос
    query = "SELECT * FROM users WHERE name = ?"
    result = conn.execute(query, (username,)).fetchall()
    
    return {
        "method": "Parameterized Query",
        "query": query,
        "result": result,
        "security": "SAFE"
    }
