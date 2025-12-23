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

# ==================== УЯЗВИМОСТЬ 3: Небезопасная десериализация ====================
@router.post("/vuln/deserialization")
def insecure_deserialization(data: str):
    """
    НЕБЕЗОПАСНАЯ ДЕСЕРИАЛИЗАЦИЯ
    Уязвимость: B301 в Bandit
    Риск: RCE через pickle
    """
    try:
        # ОПАСНО: pickle может выполнять произвольный код
        decoded = bytes.fromhex(data)
        obj = pickle.loads(decoded)
        return {
            "vulnerability": "Insecure Deserialization (CWE-502)",
            "type": str(type(obj)),
            "risk": "CRITICAL",
            "warning": "NEVER deserialize untrusted data with pickle!"
        }
    except Exception as e:
        return {"error": str(e)}
