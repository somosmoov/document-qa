import streamlit as st
import PyPDF2 as pd
from os import listdir
from os.path import isfile, join,isdir
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_qdrant import Qdrant
import sys
from langchain_text_splitters import TokenTextSplitter
from pptx import Presentation
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
import docx

def getTextFromWord(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

def getTextFromPPTX(filename):
    prs = Presentation(filename)
    fullText = []
    for slide in prs.slides:
        for shape in slide.shapes:
            fullText.append(shape.text)
    return '\n'.join(fullText)

st.title("📝 Carregue o Edital")
uploaded_file = st.file_uploader("Carregue o arquivo com o edital", type=("pdf","docx","txt", "md"))#,accept_multiple_files=True)
question = st.text_input(
        "Faça um questionamento",
        placeholder="Pode fornecer um sumário?",
        disabled=not uploaded_file,
    )
st.write(question)

