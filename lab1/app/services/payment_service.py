from app.models.payment import Payment
from app.repositories.payment_repository import PaymentRepository

class PaymentService:
    def __init__(self, payments: PaymentRepository):
        self.payments = payments

    def create_payment(self, user_id: int, amount: float):
        return self.payments.create(Payment(user_id=user_id, amount=amount))

    def list_payments(self, user_id: int):
        return self.payments.list_by_user(user_id)
