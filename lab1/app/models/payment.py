from sqlalchemy import Integer, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Payment(Base):
    __tablename__ = "payments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    amount: Mapped[float] = mapped_column(Float)
    status: Mapped[str] = mapped_column(String, default="paid")
