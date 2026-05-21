from fastapi import HTTPException
from app.repositories.user_repository import UserRepository
from app.security.password import hash_password, verify_password
from app.security.jwt_handler import create_access_token

class AuthService:
    def __init__(self, users: UserRepository):
        self.users = users

    def register(self, email: str, password: str):
        if self.users.get_by_email(email):
            raise HTTPException(status_code=409, detail="Email already exists")
        return self.users.create(email, hash_password(password))

    def login(self, email: str, password: str):
        user = self.users.get_by_email(email)
        if not user or not verify_password(password, user.password_hash):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return create_access_token(user.email)
