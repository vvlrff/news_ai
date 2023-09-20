# Используем образ Python
FROM python:3.9

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости для бэкенда
COPY server/requirements.txt ./app/

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем код бэкенда
COPY server/src ./app/src

# Указываем, что приложение должно быть запущено на порту 8000
EXPOSE 8000

# Запускаем uvicorn src.main:app —reload при запуске контейнера
CMD ["uvicorn", "src.main:app", "--reload"]