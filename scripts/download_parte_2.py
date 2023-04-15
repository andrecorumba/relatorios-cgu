# Trata-se da segunda parte do dowload dos relatórios da CGU, que estão disponíveis no site da CGU.
# Nessa segunda parte, a url é formada por um número sequencia de 1 a 13998
# Nessa nova sequencia de relatórios é necessário inclir .pdf ao final do link
# url = f"https://eaud.cgu.gov.br/relatorios/download/{i}.pdf"
# ex.: https://eaud.cgu.gov.br/relatorios/download/9.pdf

# Importa bibliotecas
import os
import requests
import time

# Importa bibliotecas locais
import save_log 

def download_part_2(folder):
    
    # Folder é a pasta onde os relatórios serão salvos. Substitua pelo caminho da sua pasta
    
    max = 3 # Teste com 3 arquivos antes de rodar o script completo
    #max = 13998 # 13998 é o número total de arquivos em 15.04.2023
    
    # Contador
    i = 1

    # Loop para baixar os relatórios da segunda parte
    while i <= max:
        file_name = os.path.join(folder, f"relatorio_{i}.pdf")
        
        # Url do relatório no padrão de número sequencial
        url = f"https://eaud.cgu.gov.br/relatorios/download/{i}.pdf"
        
        try:
            print(f"Baixando arquivo: {file_name} de 13998")
          
            # Faz a requisição do relatório          
            response = requests.get(url)

            # Salva o relatório
            with open(file_name, 'wb') as file:
                file.write(response.content)
            
            # Salva o log dos arquivos baixados
            save_log.save_log("log_sucess_part_2.txt", file_name)
        except:
            save_log.save_log("log_error_part_2.txt", file_name)
        
        # Incrementa o contador
        i = i + 1

        # Aguarda 1 segundo para não sobrecarregar o servidor
        time.sleep(1)
    
if __name__ == '__main__':
    download_part_2('relatorios_pdf')