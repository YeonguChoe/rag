from langchain_ollama import ChatOllama
from fastapi import FastAPI
from pydantic import BaseModel
from geopy.geocoders import Nominatim


app = FastAPI()

llm = ChatOllama(model="qwen3:0.6b")

text = "Tell me about Canada"

messages = [
    (
        "system",
        "You are knowledgeable of geography. You should answer in 5 sentences",
    ),
    ("human", text),
]
ai_msg = llm.invoke(messages)
# print(ai_msg)


class UserRequest(BaseModel):
    question: str
    longitude: float
    latitude: float


def get_address(latitude, longitude):
    geolocator = Nominatim(user_agent="rag")
    location = geolocator.reverse((latitude, longitude))
    return location


@app.post("/message")
async def root(request: UserRequest):
    address = get_address(request.latitude, request.longitude)
    return {"message": f"Your location is {address}. and answer is {ai_msg}"}
