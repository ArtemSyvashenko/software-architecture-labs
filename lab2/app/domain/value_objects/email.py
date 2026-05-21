import re
from app.domain.errors.domain_error import DomainValidationError

class Email:
    def __init__(self, value: str):
        if not re.match(r"^[^@]+@[^@]+\.[^@]+$", value):
            raise DomainValidationError("Invalid email")
        self.value = value
