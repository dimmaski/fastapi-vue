from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List


class Item(BaseModel):
    id: int
    example: str

app = FastAPI()

@app.get("/things")
async def things() -> List[Item]:
    return [
        Item(id=1, example="example1"), 
        Item(id=2, example="example2")]

app.mount('/', StaticFiles(directory='../ui/dist', html=True))
