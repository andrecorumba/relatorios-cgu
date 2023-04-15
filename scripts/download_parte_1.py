# Trata-se da primeira parte do dowload dos relatórios da CGU, que estão disponíveis no site da CGU.
# Nessa primeira parte, a url é formada pelo campo "id":1110235
# url = f"https://eaud.cgu.gov.br/relatorios/download/{relatorio}"
# ex.: https://eaud.cgu.gov.br/relatorios/download/1110235

# Importa bibliotecas
import os
import json
import requests
import time
import datetime

# Importa bibliotecas locais
import save_log

# Download dos relatórios da primeira parte
def download_from_id(id, reports_folder):
    
    # Pasta onde os relatórios serão salvos. Substitua pelo caminho da sua pasta

    # Nome final do arquivo
    file_name = os.path.join(reports_folder, f"relatorio_{id}.pdf") 
    
    # Url do relatório no padrão de ID
    url = f"https://eaud.cgu.gov.br/relatorios/download/{id}"
    
    # Faz a requisição do relatório
    response = requests.get(url)
    
    # Salva o relatório
    with open(file_name, 'wb') as file:
        file.write(response.content)

    return file_name

# Faz o download dos relatórios da primeira parte a partir
# da pasta que contém os arquivos json das páginas
# baixadas com o busca.py
def download_part_1(page_folder, reports_folder):
    data = {}
    
    # Percorre os arquivos da pasta
    for file_name in os.listdir(page_folder):
       
        print(f"Iniciando Arquivo: {file_name}")

        # Verifica se o arquivo é um json
        if file_name.endswith('.json'):
            
            # Nome completo do arquivo
            file_path = os.path.join(page_folder, file_name)
            
            # Abre o arquivo json
            with open(file_path, 'r', encoding='utf-8') as file:
                content = json.load(file) 

                # Percorre os dados da página
                for item in content['data']:
                    
                    # Pega o id do relatório
                    id = item['id']
                    
                    try: 
                       
                        print(f"Baixando relatório: {id}")

                        # Baixa o relatório a partir do id
                        report = download_from_id(id, reports_folder)
                        
                        # Salva o log dos arquivos baixados
                        save_log.save_log("log_sucess_part_1.txt", file_name)
                        
                        # Aguarda 5 segundos para não sobrecarregar o servidor
                        time.sleep(5)
                    except:
                        # Salva o log de erro
                        save_log.save_log("log_error_part_1.txt", file_name)
                
            print(f"Fim da página: {len(content['data'])} arquivos baixados!")
            print("Aguardando 1 segundo para baixar a próxima página...")

            # Aguarda 1 segundos para não sobrecarregar o servidor
            time.sleep(1)
    
    print("Fim do processo!")

if __name__ == "__main__":
    download_part_1('paginas', 'relatorios_pdf')