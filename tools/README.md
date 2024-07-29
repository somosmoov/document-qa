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
