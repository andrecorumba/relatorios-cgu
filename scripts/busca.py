import requests
import datetime
import os
import time 

# Importa bibliotecas locais
import download

def get_timestamp():
    now = datetime.datetime.now()
    timestamp = int(now.timestamp() * 1000)
    return str(timestamp)

# Função para acessar as URLs da pesquisa de relatorios
def pesquisa_pagina_relatorios_cgu():
    
    # Define os nomes padrões da pasta de destino e dos arquivos
    folder = 'paginas'
    
    # define o offset 0 para pegar a primeira página
    offset = 0
    i = 0

    # Quantidade de relatórios por página: 15, 30 ou 50
    page = 50

    # Loop para pegar todas as páginas. Útimo offste: 9900
    while offset <= 9900:
        file_name = f'pagina_{i}_offset_{offset}.json'

        timestamp = get_timestamp()
        
        # Útimo offste: 9900
        # https://eaud.cgu.gov.br/api/relatorios?colunaOrdenacao=dataPublicacao&direcaoOrdenacao=DESC&tamanhoPagina=15&offset=9985&_=1680980308
        
        # Agora com 50 em cada página
        # https://eaud.cgu.gov.br/api/relatorios?colunaOrdenacao=dataPublicacao&direcaoOrdenacao=DESC&tamanhoPagina=50&offset=9900&_=1680980215294
        url =f"https://eaud.cgu.gov.br/api/relatorios?colunaOrdenacao=dataPublicacao&direcaoOrdenacao=DESC&tamanhoPagina={page}&offset={offset}&_={timestamp}"
   
        response = requests.get(url)

        # if response.text == '{"draw":0,"recordsTotal":0,"recordsFiltered":0,"data":[],"error":null}':
        #     print("Final do offset!")
        #     break
   
        file_path = os.path.join(folder, file_name)
   
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(response.text)

        download.save_log("log_paginas.txt", file_path)

        print(f'Arquivo {file_name} salvo com sucesso!')

        # Incrementa o offset para pegar a próxima página com cinquenta relatórios
        offset = offset + 50
        i = i + 1

        # Aguarda 5 segundos para não sobrecarregar o servidor
        time.sleep(5)
    print("Fim do processo!")

if __name__ == '__main__':
    pesquisa_pagina_relatorios_cgu()