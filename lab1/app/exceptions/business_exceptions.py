class BusinessError(Exception):
    pass

class ConflictError(BusinessError):
    pass

class NotFoundError(BusinessError):
    pass
