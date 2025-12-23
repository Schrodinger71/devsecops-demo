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

# ==================== УЯЗВИМОСТЬ 2: Command Injection ====================
@router.get("/vuln/command-injection")
def command_injection(host: str = Query("127.0.0.1", description="Хост для ping")):
    """
    ИНЪЕКЦИЯ КОМАНД
    Уязвимость: B602 в Bandit
    Эксплуатация: host = 127.0.0.1; cat /etc/passwd
    """
    # УЯЗВИМЫЙ КОД - выполнение shell команд
    command = f"ping -c 1 {host}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    return {
        "vulnerability": "Command Injection (CWE-78)",
        "command": command,
        "output": result.stdout[:500],
        "risk": "CRITICAL",
        "exploit": "Try: google.com; ls -la"
    }
