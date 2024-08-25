#Configurações globais do projeto.

import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"] ## API
MODEL_NAME = "gpt-3.5-turbo" ##MODELO
EMBEDDING_MODEL = "text-embedding-ada-002" ##MODELO EMBEDDING

