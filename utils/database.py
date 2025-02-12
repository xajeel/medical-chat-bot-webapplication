from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ("PINECONE_API_KEY")

def create_database(index_name):
    pc = Pinecone(api_key=api_key)

    # Creating an Index in the Pinecone with name of 'medical'

    index_name = index_name

    pc.create_index(
        name=index_name,
        dimension=768, # Replace with your model dimensions
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )