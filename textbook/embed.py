"""Embed the textbook text and save in Pinecone."""
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import TokenTextSplitter
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
from langchain.schema import Document

from pathlib import Path

from keys import KEYS


textbook_path = Path(__file__).parent.absolute() / "textbook.txt"
embeddings = OpenAIEmbeddings(openai_api_key=KEYS.OpenAI.api_key)


def load_docs() -> list[Document]:
    """Load in the textbook as split documents."""
    splitter = TokenTextSplitter(encoding_name="cl100k_base", chunk_size=450, chunk_overlap=50)
    loader = TextLoader(str(textbook_path))
    docs = loader.load()
    return splitter.split_documents(docs)


def embed_to_file(docs: list[Document]) -> bool:
    """Embed the docs and upload to Pinecone."""
    vs = FAISS.from_documents(docs, embeddings)
    vs.save_local(str(textbook_path.parent / "vectorstore"))


def load_vectorstore() -> FAISS:
    """Load the vectorstore from file."""
    return FAISS.load_local(str(textbook_path.parent / "vectorstore"), embeddings)
