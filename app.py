import streamlit as st
from src.rag_chain import rag_chain
from src.vector_store_instance import vector_store_manager
from langchain_core.runnables import RunnablePassthrough  # Para passar dados através da cadeia de processamento
import time

st.set_page_config(page_title="Eleições BH 2024 - Conheça as Propostas", page_icon="🗳️", layout="wide")

# Configuração das abas
tab1, tab2 = st.tabs(["Chatbot", "Sobre o Aplicativo"])

#st.image("Imagem1.jpg", width=1000)



with tab1:

    st.title("🗳️ Eleições BH 2024 - Conheça as Propostas")

    ## Introdução

    st.markdown("""
    **Bem-vindo ao Chatbot de Propostas Eleitorais de Belo Horizonte 2024**

    Esta ferramenta foi desenvolvida para ajudar você a conhecer melhor as propostas dos candidatos à prefeitura de Belo Horizonte nas eleições de 2024. Utilizando inteligência artificial avançada, nosso chatbot permite que você explore as ideias e planos dos candidatos de forma interativa e intuitiva.

    **Utilize a caixa de chat abaixo para digitar suas perguntas sobre as propostas dos candidatos.**

    Nosso objetivo é facilitar o acesso à informação e promover uma escolha consciente nas eleições. Aproveite a experiência e fique à vontade para explorar todas as funcionalidades da ferramenta!
    """)

    # Configura o retriever do rag_chain com o vectorstore pré-carregado
    rag_chain.retriever = vector_store_manager.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 3}
    )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    chat_container = st.container()

    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])



        if prompt := st.chat_input("O que você gostaria de saber sobre as propostas dos candidatos?"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                response_container = st.empty()
                full_response = ""

                # Processa a resposta do modelo
                response = rag_chain({"question": prompt})

                # Simula o streaming da resposta
                for char in response['answer']:
                    full_response += char
                    response_container.markdown(full_response + "▌")
                    time.sleep(0.01)  # Ajuste este valor para controlar a velocidade do "streaming"

                response_container.markdown(full_response)

            st.session_state.messages.append({"role": "assistant", "content": full_response})


with tab2:
    st.title("🗳️ Eleições BH 2024 - Conheça as Propostas")
    
    st.markdown("""
    ## Como este aplicativo foi feito

    Este chatbot foi desenvolvido utilizando tecnologias de ponta em Inteligência Artificial, incluindo:

    - **LangChain**: Um framework para desenvolvimento de aplicações usando modelos de linguagem.
    - **Retrieval Augmented Generation (RAG)**: Uma técnica que combina a recuperação de informações com a geração de texto.
    - **Streamlit**: Uma biblioteca Python para criar interfaces web interativas.

    O aplicativo usa um modelo de linguagem treinado para entender e responder perguntas sobre as propostas dos candidatos à prefeitura de Belo Horizonte em 2024.

    ## Limitações e Possíveis Erros

    Embora nosso chatbot seja uma ferramenta poderosa, é importante estar ciente de suas limitações:

    1. **Informações Limitadas**: O chatbot só pode fornecer informações baseadas nos dados que foram fornecidos durante seu treinamento.
    2. **Possíveis Imprecisões**: Como qualquer sistema de IA, pode haver erros ou imprecisões nas respostas.
    3. **Viés Algorítmico**: Embora tenhamos nos esforçado para minimizar, pode haver algum viés nas respostas.
    4. **Atualização de Dados**: As informações podem não refletir mudanças muito recentes nas propostas dos candidatos.

    ## Importância de Consultar Fontes Oficiais

    Este chatbot é uma ferramenta para auxiliar na compreensão das propostas dos candidatos, mas não deve ser a única fonte de informação para sua decisão de voto. Recomendamos fortemente que você:

    1. Consulte os sites oficiais das campanhas dos candidatos.
    2. Acompanhe debates e entrevistas com os candidatos.
    3. Verifique as informações em fontes jornalísticas confiáveis.
    4. Participe de discussões e eventos políticos em sua comunidade.
    5. Acesse os [Planos de Governo oficiais dos candidatos](https://divulgacandcontas.tse.jus.br/divulga/#/candidato/SUDESTE/MG/2045202024) no site do Tribunal Superior Eleitoral (TSE).

    Lembre-se: um voto consciente é fundamental para o fortalecimento da democracia!
    """)



st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: white;
        color: black;
        text-align: center;
        padding: 10px 0;
        z-index: 999;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Rodapé
footer = st.container()

with footer:
    st.markdown('<div class="footer">', unsafe_allow_html=True)
    st.markdown("---")
    col1, col2, col3 = st.columns([1,2,1])

    with col1:
        st.write("")

    with col2:
        st.markdown("<h6 style='text-align: center;'>Desenvolvido por Pedro William Ribeiro Diniz</h6>", unsafe_allow_html=True)

    with col3:
        st.write("")

    # Ícones com links
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.write("")

    with col2:
        st.write("")

    with col3:
        st.markdown(
            """
            <a href="https://github.com/pedrow28" target="_blank">
                <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="30">
            </a>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            """
            <a href="https://www.linkedin.com/in/pedrowilliamrd/" target="_blank">
                <img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width="30">
            </a>
            """,
            unsafe_allow_html=True
        )

    with col5:
        st.write("")
    st.markdown('</div>', unsafe_allow_html=True)