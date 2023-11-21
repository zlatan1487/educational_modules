FROM python:3

WORKDIR /app

# Копируем файл с зависимостями внутрь контейнера
COPY ./requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы внутрь контейнера
COPY . .

# Команда, которая будет выполняться при запуске контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
