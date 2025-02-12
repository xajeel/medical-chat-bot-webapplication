from langchain_pinecone import PineconeVectorStore

def loading_data(index_name, embeddings):
    database = PineconeVectorStore.from_existing_index(index_name = index_name, embedding=embeddings)
    return database