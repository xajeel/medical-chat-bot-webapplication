from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_document(pages):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    # Using split_document()
    texts = text_splitter.split_documents(pages)
    return texts