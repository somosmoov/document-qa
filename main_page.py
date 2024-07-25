import streamlit as st

st.markdown("# Moov - Analisador de Editais 🎈")
#st.sidebar.markdown("# Início 🎈")
pg = st.navigation([st.Page("page_1.py"), st.Page("page_2.py")])
pg.run()
st.title("📝 Análise do Edital")
uploaded_file = st.file_uploader("Carregue o arquivo com o edital", type=("pdf","docx","txt", "md"))
question = st.text_input(
    "Faça um questionamento",
    placeholder="Pode fornecer um sumário?",
    disabled=not uploaded_file,
)
st.write("### Pergunta")
#st.write(response.completion)
