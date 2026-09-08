# taski-docker

## Описание:
Taski — это минималистичный и быстрый менеджер задач, помогающий организовывать повседневные дела, структурировать рабочие процессы и контролировать выполнение целей. Приложение разработано для индивидуального использования, поддерживает аутентификацию пользователей и предоставляет гибкое REST API для управления статусами задач. Проект упакован в изолированные Docker-контейнеры с настроенным CI/CD на базе GitHub Actions.

## Установка:
1. Клонируйте репозиторий и перейдите в папку проекта:
```
git clone https://github.com/LittleVyach/taski-docker.git
cd taski
```
2. Создайте файл .env в корне проекта со следующими переменными окружения:
```
POSTGRES_DB=taski
POSTGRES_USER=taski_user
POSTGRES_PASSWORD=taski_password
DB_HOST=db
DB_PORT=5432
SECRET_KEY=ваш_секретный_ключ_django
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1
```
3. Запустите проект с помощью Docker Compose:
```
docker compose up --build
```
4. Для локального запуска тестов выполните:
```
python -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt
pytest
```
## Примеры:
Получить список задач текущего пользователя:
```
HTTP
GET /api/tasks/
Authorization: Bearer <ваш_токен>
```
Создать новую задачу:
```
HTTP
POST /api/tasks/
Authorization: Bearer <ваш_токен>
Content-Type: application/json

{
  "name": "Купить корм для кота",
  "description": "Взять премиум-класс с лососем",
  "is_completed": false
}
```
