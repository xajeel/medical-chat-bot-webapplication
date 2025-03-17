from fastapi import FastAPI , Request#  class
from pydantic import BaseModel
import uvicorn
from main import main
import asyncio
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware



class Question(BaseModel):
    question: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development only; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")


# ====

chain = asyncio.run(main())

def question(question):
    ans = chain.invoke({"input": question})
    return ans['answer']

# ====

@app.get('/')
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post('/question/')
def ask(q: Question):
    answer = question(q.question)
    return answer


if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)