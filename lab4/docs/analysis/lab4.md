# Lab 4 Analysis

Compared with lab 3, a side component for analytics was extracted.

Two communication approaches were implemented:
1. Synchronous call: command handler directly calls analytics through a dependency.
2. Asynchronous call: command handler publishes MovieCreatedEvent to an event bus.

Synchronous communication is easier to implement, but increases response time and couples
the main operation to side effects.

Asynchronous communication makes the main operation independent from subscribers.
The API can respond faster, but testing and event delivery become more complex.

For production, the asynchronous approach is preferable for analytics and notifications,
because these side effects should not block the main business operation.
Handlers should be idempotent because the same event can be delivered more than once.
