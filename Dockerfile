# Usa uma imagem base com Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY . .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Comando padrão ao iniciar o container
CMD ["python", "index.py"]