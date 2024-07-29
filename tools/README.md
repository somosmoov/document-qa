Explicação das Funções:
Função read_pdf:

Usa fitz (PyMuPDF) para abrir e ler o texto de um arquivo PDF.
Função read_docx:

Usa Document da biblioteca python-docx para abrir e ler o texto de um arquivo DOCX.
Função read_doc:

Usa mammoth para converter e extrair texto de um arquivo DOC.
Função read_ppt_pptx:

Usa Presentation da biblioteca python-pptx para abrir e ler o texto de um arquivo PPT ou PPTX.
Função read_txt_md:

Lê arquivos TXT e MD diretamente como texto.
Considerações Adicionais:
Tratamento de Erros: Adicione tratamento de erros apropriado para lidar com possíveis falhas na leitura dos arquivos.
Desempenho: Para arquivos muito grandes, considere técnicas para processamento em partes ou streaming.
Segurança: Certifique-se de validar e sanitizar o conteúdo dos arquivos, especialmente se for compartilhar ou processar informações sensíveis.


Para adicionar tratamento de erros adequado ao código, vamos envolver as operações de leitura de arquivos em blocos try-except para capturar e tratar exceções. Isso garantirá que a aplicação não falhe de maneira abrupta ao encontrar um erro.

Código Ajustado com Tratamento de Erros
python
Copiar código
import streamlit as st
from docx import Document
import fitz  # PyMuPDF
from pptx import Presentation
import mammoth

# Função para ler arquivos PDF
def read_pdf(file):
    try:
        document = fitz.open(stream=file.read(), filetype="pdf")
        text = ""
        for page in document:
            text += page.get_text()
        return text
    except Exception as e:
        st.error(f"Erro ao ler arquivo PDF: {e}")
        return ""

# Função para ler arquivos DOCX
def read_docx(file):
    try:
        document = Document(file)
        text = ""
        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"
        return text
    except Exception as e:
        st.error(f"Erro ao ler arquivo DOCX: {e}")
        return ""

# Função para ler arquivos DOC usando mammoth
def read_doc(file):
    try:
        result = mammoth.extract_raw_text(file)
        return result.value
    except Exception as e:
        st.error(f"Erro ao ler arquivo DOC: {e}")
        return ""

# Função para ler arquivos PPT e PPTX
def read_ppt_pptx(file):
    try:
        presentation = Presentation(file)
        text = ""
        for slide in presentation.slides:
            for shape in slide.shapes:
                if hasattr(shape, "text"):
                    text += shape.text + "\n"
        return text
    except Exception as e:
        st.error(f"Erro ao ler arquivo PPT/PPTX: {e}")
        return ""

# Função para ler arquivos TXT e MD
def read_txt_md(file):
    try:
        return file.read().decode()
    except Exception as e:
        st.error(f"Erro ao ler arquivo TXT/MD: {e}")
        return ""

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

    if document_text:
        messages = [
            {
                "role": "user",
                "content": f"Here's a document: {document_text} \n\n---\n\n {question}",
            }
        ]
        
        st.write(messages)  # Para fins de depuração, você pode exibir as mensagens no Streamlit

# Certifique-se de instalar as dependências necessárias
# pip install pymupdf python-docx python-pptx mammoth
Explicação das Alterações:
Blocos try-except:

Cada função de leitura de arquivo agora está envolta em um bloco try-except para capturar exceções específicas que possam ocorrer durante a leitura do arquivo.
Quando uma exceção é capturada, uma mensagem de erro é exibida usando st.error e a função retorna uma string vazia.
Verificação de document_text:

Após a tentativa de leitura do arquivo, verificamos se document_text não está vazio antes de processar a mensagem. Isso impede que mensagens inválidas sejam geradas em caso de erro de leitura.
Considerações Finais:
Tratamento de Erros: A exibição de mensagens de erro ajuda o usuário a entender o que deu errado e, potencialmente, a corrigir o problema.
Extensibilidade: O tratamento de erros pode ser facilmente expandido para incluir logs ou outras formas de diagnóstico, se necessário.
Segurança: Garantir que a aplicação continue a funcionar de maneira controlada mesmo quando ocorrem erros melhora a experiência do usuário e a robustez da aplicação.
