from sqlalchemy.orm import Session
from app.models.subscription import Subscription

class SubscriptionRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_active_by_user(self, user_id: int):
        return self.db.query(Subscription).filter(
            Subscription.user_id == user_id,
            Subscription.status == "active"
        ).first()

    def create(self, subscription: Subscription):
        self.db.add(subscription)
        self.db.commit()
        self.db.refresh(subscription)
        return subscription
