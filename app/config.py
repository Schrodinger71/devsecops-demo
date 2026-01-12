import os


class Settings:
    APP_NAME = os.getenv("APP_NAME", "DevSecOps Demo App")
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"
    API_KEY = os.getenv("API_KEY", "dev-key")


settings = Settings()
