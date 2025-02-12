from langchain_community.document_loaders import PyPDFLoader

async def load_pdf(path):
    loader = PyPDFLoader(path)
    pages = []
    async for page in loader.alazy_load():
        pages.append(page)
    return pages
