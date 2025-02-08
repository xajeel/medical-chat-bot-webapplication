from langchain_community.document_loaders import PyPDFLoader

def load_pdf(path):
    loader = PyPDFLoader(path)
    pages = []
    for page in loader.alazy_load():
        pages.append(page)
    return pages

# print('Loaded')