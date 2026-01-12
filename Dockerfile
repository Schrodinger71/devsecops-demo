FROM python:3.11-slim

RUN useradd -m appuser
WORKDIR /app

# Меняем владельца рабочей директории
RUN chown -R appuser:appuser /app

# Копируем и устанавливаем зависимости от имени appuser
COPY --chown=appuser:appuser requirements.txt .
USER appuser
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код от имени appuser
COPY --chown=appuser:appuser app/ app/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]