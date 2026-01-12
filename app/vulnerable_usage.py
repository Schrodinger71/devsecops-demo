"""
Демонстрация использования уязвимых библиотек
для проверки безопасности зависимостей
"""

import requests
import urllib3
import django
from django.conf import settings
import json
import os


class VulnerableComponents:
    """Класс, демонстрирующий использование уязвимых библиотек"""
    
    def __init__(self):
        # Используем старую версию requests с уязвимостью CVE-2021-33503
        self.session = requests.Session()
        
        # Отключаем проверки для демонстрации
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
        # Инициализируем Django с устаревшей версией
        if not settings.configured:
            settings.configure(
                DEBUG=True,
                SECRET_KEY='insecure-secret-key-for-demo',
                ALLOWED_HOSTS=['*'],
                INSTALLED_APPS=[
                    'django.contrib.auth',
                    'django.contrib.contenttypes',
                ]
            )
            django.setup()
    
    def make_insecure_request(self, url):
        """Создание небезопасного HTTP запроса"""
        # Уязвимость: отключена проверка SSL
        response = self.session.get(url, verify=False, timeout=5)
        return response.text
    
    def download_file(self, url, destination):
        """Загрузка файла с уязвимыми настройками"""
        # Потенциальная уязвимость: скачивание без проверок
        response = self.session.get(url, stream=True, verify=False)
        
        with open(destination, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        return destination
    
    def parse_user_input(self, user_input):
        """Опасный парсинг пользовательского ввода"""
        # Уязвимость: использование eval с пользовательским вводом
        try:
            result = eval(user_input)  # НИКОГДА ТАК НЕ ДЕЛАЙТЕ!
            return result
        except Exception as e:
            return f"Error: {str(e)}"
    
    def get_django_info(self):
        """Информация о Django с уязвимой версией"""
        return {
            "version": django.get_version(),
            "vulnerabilities": [
                "CVE-2021-33203",
                "CVE-2021-33571",
                "CVE-2021-45452"
            ]
        }


# Демонстрационные функции для использования в API
def check_external_service(url: str):
    """Проверка внешнего сервиса с уязвимыми настройками"""
    vulnerable = VulnerableComponents()
    
    try:
        result = vulnerable.make_insecure_request(url)
        return {"status": "success", "result": result[:100] + "..." if len(result) > 100 else result}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def evaluate_expression(expression: str):
    """ОПАСНО: выполнение произвольного кода"""
    vulnerable = VulnerableComponents()
    
    # СИЛЬНО НЕБЕЗОПАСНО - только для демонстрации
    result = vulnerable.parse_user_input(expression)
    return {"expression": expression, "result": result}


def show_django_vulnerabilities():
    """Показ информации об уязвимостях Django"""
    vulnerable = VulnerableComponents()
    return vulnerable.get_django_info()
