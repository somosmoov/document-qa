# 📄 Document question answering template

A simple Streamlit app that answers questions about an uploaded document via OpenAI's GPT-3.5.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://document-question-answering-template.streamlit.app/)

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run main_page.py
   $ streamlit run streamlit_app.py
   $ python -m streamlit run streamlit_app.py --server.port 8000 --server.address 0.0.0.0
      ```
# para garantir o acesso ao key vault

#### Azure App Service
1. **Portal do Azure**:
   - Vá para o seu App Service.
   - No menu à esquerda, selecione **Identidade**.
   - Verifique se a opção **Sistema** (ou **Usuário**) está configurada e habilitada.
