# RAG (Retrieval-Augmented Generation)

## Prerequisite
- Ollama
- qwen

## How to run
- Install requirements
```bash
python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
```
## Run FastAPI server
- Local
```bash
fastapi dev main.py
```

- Production
```bash
uvicorn main:app --host 127.0.0.1 --port 8000
```

- Run webserver in the background
```bash
source .venv/bin/activate && nohup uvicorn main:app --host 127.0.0.1 --port 8000 &
```

- Stop background process
```bash
kill -9 $(pgrep -f "uvicorn main:app")
```

## Server address with port
```
http://127.0.0.1:8000/message
```

## POST /message
- Client Request
```json
{
    "query": "What are the nearby coffee shops?",
    "location": {
        "latitude": 43.66911640522959,
        "longitude": -79.38359555225068
    }
}
```
- Server Response
```json
{
    "answer": "Time is 10:00pm"
}
```


### Reference
- [ChatOllama](https://docs.langchain.com/oss/python/integrations/chat/ollama)
- [ChatOllama API reference](https://python.langchain.com/api_reference/ollama/chat_models/langchain_ollama.chat_models.ChatOllama.html)
