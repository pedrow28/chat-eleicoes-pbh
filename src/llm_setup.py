import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from langchain_openai import ChatOpenAI
from langchain_community.cache import SQLiteCache
from langchain.globals import set_llm_cache
from config import OPENAI_API_KEY, MODEL_NAME

# Configurar cache
set_llm_cache(SQLiteCache(database_path=".langchain.db"))

# Inicializar o modelo LLM
llm = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY,
    model_name=MODEL_NAME,
    temperature=0.7
)