 Лабораторна робота №2 — Шарова архітектура та доменна модель

## Опис
Проєкт є рефакторингом лабораторної роботи №1.

Основна мета — відокремлення бізнес-логіки від інфраструктури та реалізація шарової архітектури.

## Реалізовані шари
- Presentation
- Application
- Domain
- Infrastructure

## Технології
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pytest

## Запуск

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
Тестування
pytest
Swagger

http://127.0.0.1:8000/docs

Основні зміни порівняно з Lab1
бізнес-логіка винесена з router-ів;
доменні моделі відокремлені від ORM моделей;
додані domain factories;
реалізовано repository pattern;
додані domain errors;
реалізовано DIP (Dependency Inversion Principle).