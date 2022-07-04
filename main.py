from fastapi import FastAPI, APIRouter
from schemas import UserBaseModel
from database import User, Property, ShoppingCart, Brick, OrderDetail, PaymentMethods, Transaction

app = FastAPI()


# api_v1 = APIRouter(prefix='/api/v1')


@app.get("/")
async def root():
    return {"message": "API"}


@app.post("/users/")
async def create_user(user: UserBaseModel):
    user = User.create(
        email=user.email,
        password=user.password
    )
    return user.id


@app.get("/users/")
async def get_user():
    return User.select().first


@app.get("/findProperties")
async def get_properties():
    return Property.select().first
