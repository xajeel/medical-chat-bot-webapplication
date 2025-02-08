from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embedder():
    hf = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2",
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': False}
    )
    return hf