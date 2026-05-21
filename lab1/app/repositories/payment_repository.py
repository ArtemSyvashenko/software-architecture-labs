from sqlalchemy.orm import Session
from app.models.payment import Payment

class PaymentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, payment: Payment):
        self.db.add(payment)
        self.db.commit()
        self.db.refresh(payment)
        return payment

    def list_by_user(self, user_id: int):
        return self.db.query(Payment).filter(Payment.user_id == user_id).all()
