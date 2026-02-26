from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


def load_logs(path: str):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    return [Document(page_content=text)]


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    return splitter.split_documents(documents)