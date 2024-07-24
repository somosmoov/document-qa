nta  # import streamlit as st

# st.markdown("# Moov - Analisador de Editais 🎈")
# st.sidebar.markdown("# Início 🎈")
import streamlit as st
import anthropic

# with st.sidebar:
#    anthropic_api_key = st.text_input("Anthropic API Key", key="file_qa_api_key", type="password")
#    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/pages/1_File_Q%26A.py)"
#    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("📝 Análise do Edital")
uploaded_file = st.file_uploader("Carregue o arquivo com o edital", type=("pdf","docx","txt", "md"))
question = st.text_input(
    "Faça um questionamento",
    placeholder="Pode fornecer um sumário?",
    disabled=not uploaded_file,
)


    st.write("### Pergunta")
    #st.write(response.completion)
