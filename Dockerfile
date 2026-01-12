# Уязвимый базовый образ
FROM python:3.9-slim

# Работаем под root
USER root

# Копируем код
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Открываем все порты
EXPOSE 8000
EXPOSE 22  # Ненужный порт SSH
EXPOSE 3306  # Ненужный порт MySQL

# Запускаем под root
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
