import streamlit as st
import requests

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

login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")


bugs = st.Page("reports/bugs.py", title="Log de erros", icon=":material/bug_report:")#, default=True)
alerts = st.Page("reports/alerts.py", title="Alertas", icon=":material/notification_important:")#, default=True)

upload = st.Page("tools/upload.py", title="Carrega Edital", icon=":material/upload:", default=True)
search = st.Page("tools/search.py", title="Pesquisas", icon=":material/search:")#, default=True)
history = st.Page("tools/history.py", title="Historico", icon=":material/history:")#, default=True)

# Substitua 'SUA_API_KEY' pela sua chave da API do Cohere
api_key = st.secrets["api_cohere"]
st.write(api_key)

# Endpoint da API do Cohere para verificação de saúde
endpoint = 'https://api.cohere.com/healthcheck'

# Enviar uma solicitação GET ao endpoint
response = requests.get(endpoint, headers={'Authorization': f'Bearer {api_key}'})
st.write(endpoint) 

# Verificar o status da resposta
if response.status_code == 200:
    st.write("A API do Cohere está funcionando corretamente!")
else:
    st.write("A API do Cohere não está acessível. Verifique sua chave API e sua conexão à Internet.")
    st.write(response.status_code)


if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Acesso": [logout_page],
            "Ferramentas": [upload],# search],history],
            #"Relatórios": [bugs, alerts],
            
        }
    )
else:
   pg = st.navigation([login_page])

pg.run()
