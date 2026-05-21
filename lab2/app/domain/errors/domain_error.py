class DomainError(Exception):
    pass

class DomainValidationError(DomainError):
    pass

class DomainConflictError(DomainError):
    pass
