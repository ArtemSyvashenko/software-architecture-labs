# Лабораторна робота №4 — Синхронна та асинхронна комунікація

## Опис
Проєкт є продовженням лабораторної роботи №3.

Основна мета — реалізація синхронної та асинхронної взаємодії між компонентами системи.

## Реалізовано
- synchronous communication;
- asynchronous communication;
- event bus;
- integration events;
- side components;
- subscribers/event handlers.

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

Основні зміни порівняно з Lab3
додано Event Bus;
реалізовано integration events;
реалізовано async communication;
додані subscribers;
побічна логіка винесена в окремі компоненти.
Аналіз

docs/analysis/lab4.md