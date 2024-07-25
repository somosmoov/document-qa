import streamlit as st
st.title("📝 Carregue o Edital")
uploaded_file = st.file_uploader("Carregue o arquivo com o edital", type=("pdf","docx","txt", "md"))#,accept_multiple_files=True)
question = st.text_input(
        "Faça um questionamento",
        placeholder="Pode fornecer um sumário?",
        disabled=not uploaded_file,
    )
st.write(question)
    #return uploaded_file
