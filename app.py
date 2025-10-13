from langchain_ollama import ChatOllama


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
print(ai_msg)
