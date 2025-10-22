from langchain_ollama import ChatOllama
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from geopy.geocoders import Nominatim


app = FastAPI()

# CORS setting
origins = [
    "https://rag-demo-qqgzdmsr9-yeongu-choes-projects.vercel.app",
    "https://rag-demonstration.vercel.app",
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # React dev server
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# GPT model
llm = ChatOllama(model="qwen3:0.6b")


# Pydantic model
class LocationModel(BaseModel):
    # positive
    latitude: float
    # negative
    longitude: float


class RequestModel(BaseModel):
    query: str
    location: LocationModel


class ResponseModel(BaseModel):
    answer: str


def get_address(latitude, longitude):
    geolocator = Nominatim(user_agent="rag")
    location = geolocator.reverse((latitude, longitude), language="en")
    return location.raw["address"]["city"]


@app.post("/message")
async def root(request: RequestModel):
    address = get_address(request.location.latitude, request.location.longitude)
    messages = [
        (
            "system",
            f"""I am a helpful assistant.""",
        ),
        (
            "system",
            f"""I will answer any question.""",
        ),
        ("user", f"""user lives in {address}."""),
        ("user", request.query),
    ]
    output = llm.invoke(messages)
    return ResponseModel(answer=output.content)
