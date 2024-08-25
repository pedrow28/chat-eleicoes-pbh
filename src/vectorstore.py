from langchain_chroma import Chroma
from langchain_community.document_loaders import CSVLoader
from src.embeddings import embeddings
from src.text_splitter import split_documents

class VectorStoreManager:
    def __init__(self, persist_directory="./data/vectorstore", file_path="./data/propostas.csv"):
        self.persist_directory = persist_directory
        self.file_path = file_path
        self.vectorstore = self._load_and_create_vectorstore()

    def _load_and_create_vectorstore(self):
        # Carrega o PDF
        loader = CSVLoader(self.file_path, encoding='utf-8')
        documents = loader.load()
        
        # Divide os documentos em chunks
        chunks = split_documents(documents)
        
        # Cria e retorna o Chroma vectorstore
        return Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory=self.persist_directory
        )

    def as_retriever(self, **kwargs):
        return self.vectorstore.as_retriever(**kwargs)