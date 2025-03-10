from haystack import Pipeline
from haystack.components.writers import DocumentWriter
from haystack.components.preprocessors import DocumentSplitter
from haystack.components.embedders import SentenceTransformersDocumentEmbedder
from haystack.components.converters import PyPDFToDocument
from haystack_integrations.document_stores.pinecone import PineconeDocumentStore
from pathlib import Path
import os
from dotenv import load_dotenv


def get_result(query):
        pass


if __name__ == '__main__':
        get_result()