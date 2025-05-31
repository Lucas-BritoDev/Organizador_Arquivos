from pathlib import Path
import logging

# Configura o logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define o diretório de downloads
downloads_path = Path(r"c:\Users\lucas\Downloads")

# Lista de arquivos no diretório de downloads
try:
    lista_arquivos = [arquivo for arquivo in downloads_path.iterdir() if arquivo.is_file()]
except Exception as e:
    logging.error(f"Erro ao listar arquivos: {e}")
    exit()

# Cria diretórios para cada extensão e para arquivos sem extensão
try:
    lista_tipos = {arquivo.suffix.lower().lstrip('.') for arquivo in lista_arquivos if arquivo.suffix}
    lista_tipos.add("SemExtensao")  # Adiciona a pasta para arquivos sem extensão

    for tipo in lista_tipos:
        (downloads_path / tipo).mkdir(exist_ok=True)
        logging.info(f"Diretório '{tipo}' criado ou verificado.")
except Exception as e:
    logging.error(f"Erro ao criar diretórios: {e}")
    exit()

# Organiza os arquivos nas pastas correspondentes
for arquivo in lista_arquivos:
    try:
        if arquivo.suffix:  # Verifica se o arquivo tem uma extensão
            pasta_destino = arquivo.suffix.lower().lstrip('.')
        else:
            pasta_destino = "SemExtensao"

        destino = downloads_path / pasta_destino / arquivo.name
        arquivo.replace(destino)
        logging.info(f"Arquivo {arquivo.name} movido para {pasta_destino}")
    except Exception as e:
        logging.error(f"Erro ao mover o arquivo {arquivo.name}: {e}")