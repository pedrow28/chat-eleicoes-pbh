from langchain_openai import OpenAIEmbeddings
from config import OPENAI_API_KEY, EMBEDDING_MODEL

embeddings = OpenAIEmbeddings(
    openai_api_key=OPENAI_API_KEY,
    model=EMBEDDING_MODEL
)