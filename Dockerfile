# Используем официальный образ Python 3.13
FROM python:3.13

# Устанавливаем curl и по-быстрому ставим Poetry, потом сразу чистим систему
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry && \
    apt-get purge -y curl && apt-get clean

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем только манифесты зависимостей
COPY pyproject.toml poetry.lock* ./

# Настраиваем Poetry: не создавать виртуалки (в контейнере они не нужны)
# И устанавливаем зависимости проекта без самого проекта (no-root)
RUN poetry config virtualenvs.create false && \
    poetry install --no-root

# Копируем всё остальное (код, .env, etc.)
COPY . .

# На всякий случай — создаём папку для вложений (если нужно для dev-сбора)
RUN mkdir -p /app/media/uploads

# Запускаем приложение (предполагаем, что main.py находится в src/)
CMD ["python", "src/main.py"]
