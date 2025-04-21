# Usar imagem oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia todos os arquivos da aplicação para dentro do container
COPY . /app

# Instala as dependências, se o arquivo requirements.txt existir
RUN if [ -f "requirements.txt" ]; then pip install --no-cache-dir -r requirements.txt; fi

# Comando para rodar a aplicação ao iniciar o container
CMD ["python", "mensagem.py"]
