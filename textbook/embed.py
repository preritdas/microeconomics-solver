"""Embed the textbook text and save in Pinecone."""
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import TokenTextSplitter
from langchain.vectorstores import Pinecone
from langchain.document_loaders import TextLoader
from langchain.schema import Document

import pinecone
from pathlib import Path

from keys import KEYS


embeddings = OpenAIEmbeddings(openai_api_key=KEYS.OpenAI.api_key)
splitter = TokenTextSplitter(encoding_name="cl100k_base", chunk_size=450, chunk_overlap=50)


def load_docs() -> list[Document]:
    """Load in the textbook as split documents."""
    textbook_path = Path(__file__).parent.absolute() / "textbook.txt"
    loader = TextLoader(textbook_path)
    docs = loader.load()
    return splitter.split_documents(docs)


def embed_to_pinecone(docs: list[Document]) -> bool:
    """Embed the docs and upload to Pinecone."""
    pinecone.init(
        api_key=KEYS.Pinecone.api_key,
        environment="gcp-starter",
    )

    index_name = "textbook"
    if index_name not in pinecone.list_indexes():
        pinecone.create_index(
        name=index_name,
        metric='cosine',
        dimension=1536  
    )

    docsearch = Pinecone(pinecone.Index(index_name))