from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.repositories.payment_repository import PaymentRepository
from app.schemas.payment_schema import PaymentCreate, PaymentResponse
from app.security.dependencies import get_current_user
from app.services.payment_service import PaymentService

router = APIRouter(prefix="/payments", tags=["payments"])

@router.post("/", response_model=PaymentResponse, status_code=201)
def create_payment(data: PaymentCreate, user=Depends(get_current_user), db: Session = Depends(get_db)):
    return PaymentService(PaymentRepository(db)).create_payment(user.id, data.amount)

@router.get("/", response_model=list[PaymentResponse])
def list_payments(user=Depends(get_current_user), db: Session = Depends(get_db)):
    return PaymentService(PaymentRepository(db)).list_payments(user.id)
