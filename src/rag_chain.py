from langchain.chains import ConversationalRetrievalChain
from src.llm_setup import llm
from src.memory import memory
from src.retriever import retriever
from src.prompt_templates import RAG_PROMPT

rag_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory,
    combine_docs_chain_kwargs={"prompt": RAG_PROMPT}
)