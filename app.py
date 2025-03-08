from fastapi import FastAPI #  class
from pydantic import BaseModel
import uvicorn
from main import main
import asyncio

class Question(BaseModel):
    question: str

app = FastAPI()


# ====

chain = asyncio.run(main())

def question(question):
    ans = chain.invoke({"input": question})
    return ans['answer']

# ====


@app.get('/')
def home():
    return {"message": "Hello World"}

@app.post('/question/')
def ask(q: Question):
    answer = question(q.question)
    return answer


if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)