import asyncio
from src.loader import load_pdf
from src.splitter import split_document
from src.embedder import get_embedder
from src.loadData import loading_data
from src.model import qna_model


PATH = ""
INDEX = "medical"

async def main():
    # pages = await load_pdf(PATH)
    # texts = split_document(pages)
    print("*** Getting Embedding Model ***")
    embedder = get_embedder()
    print("*** Loading Data ***")
    retriever = loading_data(INDEX, embedder)
    print("*** Creating Chain ***")
    chain = qna_model(retriever)
    return chain
    