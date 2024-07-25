import streamlit as st

st.markdown("# Moov - Analisador de Editais 🎈")
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()

def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()

#@st.cache_data
def carrega():
    st.title("📝 Carregue o Edital")
    uploaded_file = st.file_uploader("Carregue o arquivo com o edital", type=("pdf","docx","txt", "md"))#,accept_multiple_files=True)
    question = st.text_input(
        "Faça um questionamento",
        placeholder="Pode fornecer um sumário?",
        disabled=not uploaded_file,
    )
    st.write(question)
    return uploaded_file

login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")


bugs = st.Page("reports/bugs.py", title="Log de erros", icon=":material/bug_report:")
alerts = st.Page(
    "reports/alerts.py", title="Alertas", icon=":material/notification_important:"
)

upload = st.Page("tools/upload.py", title="Carrega Edital", icon=":material/upload:", default=True,
    carrega)
search = st.Page("tools/search.py", title="Pesquisas", icon=":material/search:")
history = st.Page("tools/history.py", title="Historico", icon=":material/history:")

if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Acesso": [logout_page],
            "Ferramentas": [upload, search, history],
            "Relatórios": [bugs, alerts],
            
        }
    )
else:
   pg = st.navigation([login_page])

pg.run()
