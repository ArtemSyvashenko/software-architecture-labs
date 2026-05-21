from fastapi import HTTPException
from app.models.subscription import Subscription
from app.repositories.subscription_repository import SubscriptionRepository

ALLOWED_PLANS = {"basic", "standard", "premium"}

class SubscriptionService:
    def __init__(self, subscriptions: SubscriptionRepository):
        self.subscriptions = subscriptions

    def create_subscription(self, user_id: int, plan: str):
        if plan not in ALLOWED_PLANS:
            raise HTTPException(status_code=400, detail="Invalid subscription plan")
        if self.subscriptions.get_active_by_user(user_id):
            raise HTTPException(status_code=409, detail="User already has active subscription")
        return self.subscriptions.create(Subscription(user_id=user_id, plan=plan))
