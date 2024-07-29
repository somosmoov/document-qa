import streamlit as st
from docx import Document
import fitz  # PyMuPDF
from pptx import Presentation
import mammoth

# Função para ler arquivos PDF
def read_pdf(file):
    document = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in document:
        text += page.get_text()
    return text

# Função para ler arquivos DOCX
def read_docx(file):
    document = Document(file)
    text = ""
    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"
    return text

# Função para ler arquivos DOC usando mammoth
def read_doc(file):
    result = mammoth.extract_raw_text(file)
    return result.value

# Função para ler arquivos PPT e PPTX
def read_ppt_pptx(file):
    presentation = Presentation(file)
    text = ""
    for slide in presentation.slides:
        for shape in slide.shapes:
            if hasattr(shape, "text"):
                text += shape.text + "\n"
    return text

# Função para ler arquivos TXT e MD
def read_txt_md(file):
    return file.read().decode()

# Streamlit UI
st.title("📝 Carregue o Edital")

uploaded_file = st.file_uploader("Carregue o arquivo com o edital", type=("pdf", "docx", "doc", "ppt", "pptx", "txt", "md"))

question = st.text_input(
    "Faça um questionamento",
    placeholder="Pode fornecer um sumário?",
    disabled=not uploaded_file,
)

if uploaded_file and question:
    # Process the uploaded file based on its type
    if uploaded_file.type == "application/pdf":
        document_text = read_pdf(uploaded_file)
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        document_text = read_docx(uploaded_file)
    elif uploaded_file.type == "application/msword":
        document_text = read_doc(uploaded_file)
    elif uploaded_file.type in ["application/vnd.ms-powerpoint", "application/vnd.openxmlformats-officedocument.presentationml.presentation"]:
        document_text = read_ppt_pptx(uploaded_file)
    else:
        document_text = read_txt_md(uploaded_file)

    messages = [
        {
            "role": "user",
            "content": f"Here's a document: {document_text} \n\n---\n\n {question}",
        }
    ]
    
    st.write(messages)  # Para fins de depuração, você pode exibir as mensagens no Streamlit

# Certifique-se de instalar as dependências necessárias
# pip install pymupdf python-docx python-pptx mammoth
