# Доска объявлений

Backend-часть для сайта объявлений с авторизацией, CRUD операциями и отзывами.

## Возможности

-  Регистрация и авторизация пользователей
-  Ролевая система (пользователь, администратор)
-  Восстановление пароля через email
-  CRUD операции с объявлениями
-  Система отзывов к объявлениям
-  Поиск объявлений по названию
-  REST API документация (Swagger)

## Технологии

- **Backend**: Django 4.2+, Django REST Framework
- **База данных**: PostgreSQL / SQLite (для разработки)
- **Аутентификация**: JWT / Session Authentication
- **Документация**: drf-yasg (Swagger)
- **Тестирование**: pytest, Django Test Framework

##  Установка и запуск

### Предварительные требования

- Python 3.10+
- PostgreSQL (для production)
- Poetry (менеджер зависимостей)

### 1. Клонирование репозитория

```
https://github.com/eqxtapo/DW
```
### 2. Установка зависимостей
```
# Установка Poetry (если не установлен)
pip install poetry

# Установка зависимостей
poetry install

# Активация виртуального окружения
poetry shell
```
### 3. Настройка окружения
Создайте файл .env в корне проекта:
```
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
```

### 4. Настройка базы данных
```
# Применение миграций
python manage.py migrate

# Создание суперпользователя
python manage.py csu
```
### 5. Запуск сервера
```
# Development сервер
python manage.py runserver

# Или с конкретным портом
python manage.py runserver 0.0.0.0:8000
```

## API Документация
После запуска сервера откройте:

Swagger UI: http://localhost:8000/swagger/

ReDoc: http://localhost:8000/redoc/

## Тестирование
```
# Запуск всех тестов
pytest

# Запуск с покрытием
pytest --cov=.
```

## Разработка
Code Style
```
# Проверка стиля
flake8 .

# Форматирование кода
black .
```
## Миграции
```
# Создание миграций
python manage.py makemigrations

# Применение миграций
python manage.py migrate
```

