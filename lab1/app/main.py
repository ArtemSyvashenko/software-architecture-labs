from fastapi import FastAPI
from app.database import Base, engine
from app.models.user import User
from app.models.movie import Movie
from app.models.subscription import Subscription
from app.models.payment import Payment
from app.routers.auth_router import router as auth_router
from app.routers.movie_router import router as movie_router
from app.routers.subscription_router import router as subscription_router
from app.routers.payment_router import router as payment_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Streaming Service Lab 1")

app.include_router(auth_router)
app.include_router(movie_router)
app.include_router(subscription_router)
app.include_router(payment_router)

@app.get("/health")
def health():
    return {"status": "ok"}
