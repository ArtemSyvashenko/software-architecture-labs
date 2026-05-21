from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.repositories.user_repository import UserRepository
from app.schemas.auth_schema import RegisterRequest, LoginRequest, TokenResponse
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", status_code=201)
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    user = AuthService(UserRepository(db)).register(data.email, data.password)
    return {"id": user.id, "email": user.email}

@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    token = AuthService(UserRepository(db)).login(data.email, data.password)
    return TokenResponse(access_token=token)
