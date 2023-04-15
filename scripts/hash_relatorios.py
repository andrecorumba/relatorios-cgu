# Módulo que gera os hashes dos relatórios

import os
import hashlib

def hash_relatorios(folder):
    # Folder é a pasta com os relatórios em pdf baixados pela parte 1 e 2 dos downloads  
    files_in_folder = os.listdir(folder)

    # Inicializar dicionário de hash de todos os arquivos em ambas as pastas
    hash_total = {}
        
    # Calcular hash de cada arquivo em ambas as pastas e adicioná-lo ao dicionário hash_total
    for file_name in files_in_folder:
        
        # Não considerar arquivos ocultos
        if file_name.startswith('.'):
            continue    
        
        else:
            
            # Abrir arquivo em modo binário
            with open(os.path.join(folder, file_name), 'rb') as f:
                conteudo = f.read()
        
                # Aplicar hash sha256
                hash = hashlib.sha256(conteudo).hexdigest()

                # Receber uma lista de arquivos com o mesmo hash
                if hash in hash_total:
                    hash_total[hash].append(file_name)
                
                else:
                    hash_total[hash] = [file_name]
    return hash_total

# Função para contar quantos arquivos possuem o mesmo hash em hash_total
def contagem_hash(hash_total):
    contagem = {}

    for hash, arquivos in hash_total.items():
        contagem[hash] = len(arquivos)
        
    # Imprimir o número de arquivos para cada hash em ordem decrescente
    for hash, num_arquivos in sorted(contagem.items(), key=lambda x: x[1], reverse=True):
        print(f"{hash}: {num_arquivos} arquivos")

# Função para criar uma lista de arquivos únicos
def arquivos_com_hash_exclusivo(hash_total):
    # Inicializar lista de arquivos únicos
    arquivos_exclusivos = []
    
    # Adicionar primeiro arquivo de cada hash à lista de arquivos únicos.
    # Ainda que o hash tenha mais de um arquivo, o primeiro arquivo será o 
    # único a ser adicionado à lista.
    for hash, arquivos in hash_total.items():
        arquivos_exclusivos.append(arquivos[0])
            
    return arquivos_exclusivos

# Funçao que recebe uma lista de arquivos unicos em uma pasta e copia esses 
# arquivos para outra pasta
def copiar_arquivos_unicos(arquivos_unicos, pasta_origem, pasta_destino):
    for arquivo in arquivos_unicos:
        os.system(f'cp {os.path.join(pasta_origem, arquivo)} {os.path.join(pasta_destino, arquivo)}')
    
    print (f"{len(arquivos_unicos)} arquivos copiados com sucesso!")

if __name__ == "__main__":
    
    # Pasta com os relatórios em pdf baixados pela parte 1 e 2 dos downloads
    folder='relatorios_pdf'
    
    hash_total = hash_relatorios(folder)
    
    contagem_hash(hash_total)
    
    arquivos_unicos = arquivos_com_hash_exclusivo(hash_total)

    print(f"Existem {len(arquivos_unicos)} arquivos únicos.")
    print(arquivos_unicos)

    copiar_arquivos_unicos(arquivos_unicos, folder, "pasta_arquivos_unicos")


