"""Embed the textbook text and save in local FAISS."""
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import TokenTextSplitter
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader
from langchain.schema import Document

from pathlib import Path

from keys import KEYS


textbook_path = Path(__file__).parent.absolute() / "textbook.pdf"
embeddings = OpenAIEmbeddings(openai_api_key=KEYS.OpenAI.api_key)


def load_docs() -> list[Document]:
    """Load in the textbook as split documents."""
    splitter = TokenTextSplitter(encoding_name="cl100k_base", chunk_size=450, chunk_overlap=50)
    loader = PyPDFLoader(str(textbook_path))
    docs = loader.load_and_split(splitter)

    # Append page number to each document content
    for doc in docs:
        doc.page_content += f" (Page {doc.metadata.get('page', 'n/a')})"

    return docs


def embed_to_file(docs: list[Document]) -> bool:
    """Embed the docs and upload to Pinecone."""
    vs = FAISS.from_documents(docs, embeddings)
    vs.save_local(str(textbook_path.parent / "vectorstore"))


def load_vectorstore() -> FAISS:
    """Load the vectorstore from file."""
    return FAISS.load_local(str(textbook_path.parent / "vectorstore"), embeddings)
