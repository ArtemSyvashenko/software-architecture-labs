# Лабораторна робота №3 — Command Query Separation (CQS)

## Опис
Проєкт є продовженням лабораторної роботи №2.

Основна мета — розділення операцій запису (Commands) та читання (Queries) у Application Layer.

## Реалізовано
- Commands;
- Queries;
- Command Handlers;
- Query Handlers;
- Read Models;
- тонкі controller/router-и.

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

Основні зміни порівняно з Lab2
логіка читання та запису розділена;
додані command handlers;
додані query handlers;
queries повертають read models;
controllers містять лише маппінг HTTP → Command/Query.
Аналіз

docs/analysis/lab3.md