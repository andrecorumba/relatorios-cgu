# Módulo para consultar as páginas de pesquisa de relatórios da CGU
# e salvar os arquivos json com os dados dos relatórios

# Importa bibliotecas externas
import requests
import datetime
import os
import time 

# Importa bibliotecas locais
import save_log

# Função para pegar o timestamp
def get_timestamp():
    now = datetime.datetime.now()
    timestamp = int(now.timestamp() * 1000)
    return str(timestamp)

# Função para acessar as URLs da pesquisa de relatorios
def pesquisa_pagina_relatorios_cgu(max_offset):
    
    # Define os nomes padrões da pasta de destino e dos arquivos. 
    # Altere o nome da pasta se desejar
    folder = 'paginas'
    
    # define o offset 0 para pegar a primeira página
    offset = 0
    i = 0

    # Quantidade de relatórios por página: 15, 30 ou 50
    page = 50

    # Loop para pegar todas as páginas. Útimo offste: 9900
    # Eu preferi fixar o offset máximo para não ficar rodando
    
    # max_offset = 9900
    # max_offset = 50 para testes
    while offset <= max_offset: 
        file_name = f'pagina_{i}_offset_{offset}.json'

        timestamp = get_timestamp()
        
        # Exemplo com 50 em cada página
        # https://eaud.cgu.gov.br/api/relatorios?colunaOrdenacao=dataPublicacao&direcaoOrdenacao=DESC&tamanhoPagina=50&offset=9900&_=1680980215294
        
        # url substituindo o offset e o timestamp
        url =f"https://eaud.cgu.gov.br/api/relatorios?colunaOrdenacao=dataPublicacao&direcaoOrdenacao=DESC&tamanhoPagina={page}&offset={offset}&_={timestamp}"
        
        try: 
            # Faz a requisição da página
            response = requests.get(url)
            
            # NÃO UTILIZEI O CÓDIGO ABAIXO PORQUE FIXEI O OFFSET EM 9900
            # Verifica se a página está vazia. Se estiver, para o loop.
            # if response.text == '{"draw":0,"recordsTotal":0,"recordsFiltered":0,"data":[],"error":null}':
            #     print("Final do offset!")
            #     break
    
            # Caminho completo do arquivo
            file_path = os.path.join(folder, file_name)
    
            # Salva o arquivo json
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(response.text)

            # Salva o log
            save_log.save_log("log_sucess_paginas.txt", file_path)

            print(f'Arquivo {file_name} salvo com sucesso!')

            # Incrementa o offset para pegar a próxima página com cinquenta relatórios
            offset = offset + 50
            i = i + 1

            # Aguarda 2 segundos para não sobrecarregar o servidor
            time.sleep(2)
        except:
            # Salva o log de erro
            save_log.save_log("log_error_paginas.txt", file_name)
    
    print("Fim do processo!")

if __name__ == '__main__':
    # max_offset = 9900
    # max_offset = 50 para testes
    pesquisa_pagina_relatorios_cgu(50)