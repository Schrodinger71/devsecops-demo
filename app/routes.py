"""
Демонстрационные уязвимые endpoints для курсовой по DevSecOps
ВНИМАНИЕ: Этот код содержит преднамеренные уязвимости для обучения!
"""

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

# ==================== УЯЗВИМОСТЬ 1: SQL-инъекция ====================
@router.get("/vuln/sql-injection")
def sql_injection(username: str = Query(..., description="Имя пользователя для поиска")):
    """
    КЛАССИЧЕСКАЯ SQL-ИНЪЕКЦИЯ
    Уязвимость: B608 в Bandit
    Эксплуатация: username = ' OR '1'='1
    """
    conn = sqlite3.connect(':memory:')
    conn.execute('CREATE TABLE users (id INTEGER, name TEXT)')
    conn.execute("INSERT INTO users VALUES (1, 'admin')")
    
    # УЯЗВИМЫЙ КОД - прямая конкатенация
    query = f"SELECT * FROM users WHERE name = '{username}'"
    
    try:
        result = conn.execute(query).fetchall()
        return {
            "vulnerability": "SQL Injection (CWE-89)",
            "query": query,
            "result": result,
            "risk": "CRITICAL",
            "exploit": "Try: ' OR '1'='1 --"
        }
    except Exception as e:
        return {"error": str(e)}
