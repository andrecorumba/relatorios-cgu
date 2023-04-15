# Módulo principal com exemplo de uso
# Importar bibiotecas externas
import os

# Importar módulos internos
import busca_pagina
import download_parte_1
import download_parte_2
import hash_relatorios

def cria_pastas():
# Cria pastas
    paginas_path = os.path.abspath('paginas')
    relatorios_pdf_path = os.path.abspath('relatorios_pdf')
    log_path = os.path.abspath('log')
    pasta_arquivos_unicos_path = os.path.abspath('pasta_arquivos_unicos')
    hashes_path = os.path.abspath('hashes')
    
    os.makedirs(paginas_path, exist_ok=True)
    os.makedirs(relatorios_pdf_path, exist_ok=True)
    os.makedirs(log_path, exist_ok=True)
    os.makedirs(pasta_arquivos_unicos_path, exist_ok=True)
    os.makedirs(hashes_path, exist_ok=True)
    
    return (paginas_path, relatorios_pdf_path, log_path, pasta_arquivos_unicos_path, hashes_path)

def main():
    # Cria pastas
    paginas, relatorios_pdf, log, pasta_arquivos_unicos, hashes = cria_pastas()
    
    print("Pastas criadas: ")
    print (paginas, relatorios_pdf, log, pasta_arquivos_unicos, hashes)

    # Buscar página de relatórios
    busca_pagina.pesquisa_pagina_relatorios_cgu(50)

    # Baixar relatórios
    download_parte_1.download_part_1(paginas, relatorios_pdf)
    download_parte_2.download_part_2(relatorios_pdf)

    # Aplicar hashes
    hash_total = hash_relatorios.hash_relatorios(relatorios_pdf) 
    hash_relatorios.contagem_hash(hash_total)
    
    arquivos_unicos = hash_relatorios.arquivos_com_hash_exclusivo(hash_total)
    
    # Copiar arquivos únicos
    hash_relatorios.copiar_arquivos_unicos(arquivos_unicos, relatorios_pdf, pasta_arquivos_unicos)

if __name__ == '__main__':
    main()