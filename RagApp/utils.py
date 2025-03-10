from haystack_integrations.document_stores.pinecone import PineconeDocumentStore
import os
from dotenv import load_dotenv



load_dotenv()
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
print("Import Succesfully")



def pinecon_config():
    document_store = PineconeDocumentStore(
        api_key= PINECONE_API_KEY,
        index='haystack-extractive-qa',
        similarity="cosine",
        embedding_dim=768
    )

    return document_store