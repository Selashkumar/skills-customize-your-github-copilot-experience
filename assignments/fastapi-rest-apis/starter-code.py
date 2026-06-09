from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {
        "item_id": item_id,
        "q": q,
        "name": "Sample Item",
        "price": 9.99,
        "in_stock": True,
    }

@app.post("/items")
def create_item(item: Item):
    return {
        "message": "Item created successfully",
        "item": item,
    }
