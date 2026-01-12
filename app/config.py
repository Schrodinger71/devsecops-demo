import os

class Settings:
    APP_NAME = os.getenv("APP_NAME", "DevSecOps Demo App")
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"
    # Хардкодированные секреты для демонстрации
    API_KEY = "super-secret-key-12345"
    DATABASE_PASSWORD = "admin123"  # B105
    AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
    AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    
    # JWT секрет
    JWT_SECRET = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"


settings = Settings()
