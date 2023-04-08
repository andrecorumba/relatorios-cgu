import os
import json
import requests
import time
import datetime

# A url é formada pelo campo id
# "id":1110235
# url = f"https://eaud.cgu.gov.br/relatorios/download/{relatorio}"
# https://eaud.cgu.gov.br/relatorios/download/1110235

def save_log(log_name, file_name):
    folder = 'log'
    file_path = os.path.join(folder, log_name)

    with open(file_path, 'a') as file:
        file.write(f"Arquivo: {file_name}, {datetime.datetime.now()}\n")

def download_pdf(id):
    file_name = f"relatorios/relatorio_{id}.pdf"
    url = f"https://eaud.cgu.gov.br/relatorios/download/{id}"
    response = requests.get(url)
    with open(file_name, 'wb') as file:
        file.write(response.content)

    return file_name


def read_json_files(folder):
    data = {}
    for file_name in os.listdir(folder):
       
        print(f"Iniciando Arquivo: {file_name}")

        if file_name.endswith('.json'):
            
            file_path = os.path.join(folder, file_name)
            
            with open(file_path, 'r', encoding='utf-8') as file:
                content = json.load(file) 
                for item in content['data']:
                    
                    id = item['id']
                    
                    print(f"Baixando relatório: {id}")
                    
                    # Baixa o relatório
                    report = download_pdf(id)
                    
                    # Salva o log
                    save_log("log_downloaded_pdf.txt", report)
                    
                    # Aguarda 5 segundos para não sobrecarregar o servidor
                    time.sleep(5)
                
            print(f"Fim da página: {len(content['data'])} arquivos baixados!")
            print("Aguardando 5 segundos para baixar a próxima página...")
            time.sleep(5)
    
    print("Fim do processo!")


if __name__ == '__main__':
    read_json_files('paginas')



