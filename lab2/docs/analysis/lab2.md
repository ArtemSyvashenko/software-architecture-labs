# Lab 2 Analysis

Compared with lab 1, the project was refactored into four layers:
Presentation, Application, Domain and Infrastructure.

The main improvement is separation of business logic from framework and database code.
Domain models are independent from ORM models. Infrastructure contains SQLAlchemy models,
mappers and repository implementations. Application layer orchestrates use cases.

The disadvantage is additional code and more mapping between layers, but the database
or web framework can now be replaced with fewer changes.
