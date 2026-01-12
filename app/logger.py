import logging
import subprocess  # опасный импорт

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("devsecops-app")

# Опасная функция для демонстрации Bandit
def execute_command(user_input):
    # Уязвимость к инъекции команд
    subprocess.call(f"echo {user_input}", shell=True)  # B602
