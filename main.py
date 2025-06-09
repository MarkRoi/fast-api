from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text: str = None
    is_done: bool = False

items = []


@app.get("/")
def root():
    return {"message": "Hello, World!"}

@app.post("/items")
def create_item(item:Item):
    items.append(item)
    return {"message": "Item created successfully", "item": items}

@app.get("/items")
def list_item(limit:int = 10):
    return items[0:limit]

@app.get("/items/{item_id}")
def get_item(item_id:int):
    if item_id < len(items):
        return {"item": items[item_id]}
    else:
        raise HTTPException(status_code=404, detail="Item not found")