from fastapi import FastAPI
from enum import Enum

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "hello world"}


@app.post('/')
async def post():
    return {"message": "hello from the post route"}


@app.put('/')
async def put():
    return {"message": "hello from the put route"}


"""PATH PARAMETERS"""


@app.get('/users')
async def list_users():
    return {"message": "list users route"}


@app.get('/users/{user_id}')
async def get_item(user_id: int):
    return {"user_id": user_id}


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"


@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name, "message": "you are healthy"}

    if food_name == FoodEnum.fruits:
        return {"food_name": food_name,
                "message": "you are still healthy, but like sweet things"}

    return {"food_name": food_name, "message": "I like chocolate milk"}

"""QUERY PARAMETERS"""

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items")
async def get_items():

