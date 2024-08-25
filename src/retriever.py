from src.vector_store_instance import vector_store_manager

retriever = vector_store_manager.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 6}
)