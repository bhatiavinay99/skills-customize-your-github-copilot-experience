from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# In-memory store for items
items_db = []
next_id = 1


# Task 1 - Root and health-check endpoints
@app.get("/")
def read_root():
    # Return a welcome message
    pass


@app.get("/health")
def health_check():
    # Return a status ok response
    pass


# Task 2 - Path and query parameter endpoints
@app.get("/items/{item_id}")
def get_item_by_id(item_id: int):
    # Return the item_id in a JSON response
    pass


@app.get("/items")
def get_items(category: str = None):
    # Return all items, or filter by category if provided
    pass


# Task 3 - Pydantic model and POST endpoint
class Item(BaseModel):
    # Define the fields: name (str), price (float), category (str)
    pass


@app.post("/items")
def create_item(item: Item):
    # Add the item to items_db with a generated id and return it
    pass
