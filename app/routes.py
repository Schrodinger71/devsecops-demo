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

# ==================== УЯЗВИМОСТЬ 5: XXE ====================
@router.post("/vuln/xxe")
def xxe_vulnerability(xml_data: str):
    """
    XXE (XML External Entity) АТАКА
    Уязвимость: CWE-611
    Эксплуатация: Чтение локальных файлов
    """
    try:
        # УЯЗВИМЫЙ ПАРСЕР XML
        root = ET.fromstring(xml_data)
        return {
            "vulnerability": "XXE (CWE-611)",
            "root_tag": root.tag,
            "risk": "HIGH",
            "exploit": "Try including <!ENTITY xxe SYSTEM 'file:///etc/passwd'>"
        }
    except Exception as e:
        return {"error": str(e)}
