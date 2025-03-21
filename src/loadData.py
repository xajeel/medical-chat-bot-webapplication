from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv

load_dotenv()

def loading_data(index_name, embeddings):
    database = PineconeVectorStore.from_existing_index(index_name = index_name, embedding=embeddings)
    retriever = database.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 1}, )

    return retriever