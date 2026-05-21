from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.repositories.subscription_repository import SubscriptionRepository
from app.schemas.subscription_schema import SubscriptionCreate, SubscriptionResponse
from app.security.dependencies import get_current_user
from app.services.subscription_service import SubscriptionService

router = APIRouter(prefix="/subscriptions", tags=["subscriptions"])

@router.post("/", response_model=SubscriptionResponse, status_code=201)
def create_subscription(data: SubscriptionCreate, user=Depends(get_current_user), db: Session = Depends(get_db)):
    return SubscriptionService(SubscriptionRepository(db)).create_subscription(user.id, data.plan)
