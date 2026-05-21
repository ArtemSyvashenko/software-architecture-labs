# Lab 3 Analysis

This lab continues the previous structure and introduces additional architectural separation.

Commands represent write operations and are handled by command handlers.
Queries represent read operations and return read models instead of domain objects.

Controllers remain thin: they only map HTTP input to command/query objects.
