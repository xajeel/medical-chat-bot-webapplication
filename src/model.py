from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain




load_dotenv()

def chain(retriever):

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.4,
        api_key = os.environ.get("GROQ_API_KEY")
        )

    # Creating prompt for the LLM

    template = ChatPromptTemplate.from_messages(
        [
        ("system", "You are a helpfull assistant for question answering task. use the following retrived context to generate answer.Keep it short and concise. If you do find anything from the context then just say I do not know "
        "\n\n {context}"),

        ("human", "{input}")
        ]
    )


    qna = create_stuff_documents_chain(llm, template)
    chain = create_retrieval_chain(retriever, qna)

    return chain

