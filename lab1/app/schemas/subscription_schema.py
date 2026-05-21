from pydantic import BaseModel

class SubscriptionCreate(BaseModel):
    plan: str

class SubscriptionResponse(BaseModel):
    id: int
    user_id: int
    plan: str
    status: str
    class Config:
        from_attributes = True
