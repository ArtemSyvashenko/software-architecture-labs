from pydantic import BaseModel, Field

class PaymentCreate(BaseModel):
    amount: float = Field(gt=0)

class PaymentResponse(BaseModel):
    id: int
    user_id: int
    amount: float
    status: str
    class Config:
        from_attributes = True
