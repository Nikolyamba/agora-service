Реализация тестового задания для компании aezakmi
Backend-сервис для генерации Agora RTC / RTM токенов и управления комнатами.

Основной стек технологий:
1) Python 3.11
2) PostgreSQL 17
3) SQLalchemy
4) Alembic для миграций
5) Logging для логов
6) Slowapi для рейт лимитера
7) Docker
8) Pytest для тестов
9) Backend-сервис для генерации Agora RTC / RTM токенов и управления комнатами.

Запуск проекта:
Требуется Docker Desktop с включённой WSL 2 интеграцией
!!! Также необходимо сделать .env файл. Данные можно взять из .env.example
docker compose up --build

Функциональность
Авторизация:
Простейшая header-based авторизация через X-User-Id

Генерация токенов
RTC токены (host / audience)
RTM токены

Управление комнатами:
Создание комнат
Генерация уникального Agora channel name
Привязка комнаты к пользователю

Дополнительно

Rate limiting (slowapi)
Health check эндпоинт (main.py)
Docker + docker-compose
Логирование ключевых событий
Юнит-тесты для сервиса генерации токенов
Миграции с помощью Alembic

Структура проекта: 

├── api/ # HTTP эндпоинты (controllers)
├── db/ # Подключение к БД и сессии
├── features/ # Папка для различных фич. Сюда можно было бы потом добавить генерацию паролей и прочего вспомогательного
├── models/ # SQLAlchemy модели
├── schemas/ # Pydantic схемы
├── services/ # Бизнес-логика (Agora, logging, rate limiting)
├── tests/ # Юнит-тесты
├── main.py # Точка входа
├── alembic.ini - файл-настройка для миграций. Подробно о миграциях в db -> migrations
├── Dockerfile
├── docker-compose.yml
└── .env

Эндпоинты:

POST /api/auth/simple
Headers: X-User-Id: user_123

response:
{
  "user_id": "user_123",
  "status_code": 200,
  "detail": "Вы успешно авторизовались"
}

POST /api/tokens/rtc
Headers: X-User-Id: user_123
Body: {
  "channel": "room_123",
  "uid": "user_456",
  "role": "host"
}
Response: {
  "token": "agora_rtc_token",
  "expires_in": 3600
}

POST /api/tokens/rtm
Headers: X-User-Id: user_123
Body: {
    "uid": "user_456"
}
Response: {
  "token": "agora_rtm_token",
  "expires_in": 3600
}

POST /api/rooms
Headers: X-User-Id: user_123
Body: {
  "name": "Вебинар по танцам",
  "is_private": true,
  "max_participants": 50
}
Response: {
  "room_id": "uuid",
  "channel_name": "agora_channel_xyzab12cd34"
}


