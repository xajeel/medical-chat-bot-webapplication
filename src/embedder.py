from langchain_huggingface import HuggingFaceEmbeddings
import sentence_transformers

def get_embedder(model="sentence-transformers/all-mpnet-base-v2"):
    hf = HuggingFaceEmbeddings(
        model_name=model,
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': False}
    )
    return hf