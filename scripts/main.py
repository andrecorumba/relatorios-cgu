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
    os.makedirs('paginas', exist_ok=True)
    os.makedirs('relatorios_pdf', exist_ok=True)
    os.makedirs('log', exist_ok=True)
    os.makedirs('pasta_arquivos_unicos', exist_ok=True)

def main():
    # Cria pastas
    cria_pastas()

    # Buscar página de relatórios
    busca_pagina.pesquisa_pagina_relatorios_cgu(50)

    # Baixar relatórios
    download_parte_1.download_part_1('paginas', 'relatorios_pdf')
    download_parte_2.download_part_2('relatorios_pdf')

    # Aplicar hashes
    hash_total = hash_relatorios.hash_relatorios('relatorios_pdf') 
    hash_relatorios.contagem_hash(hash_total)
    
    arquivos_unicos = hash_relatorios.arquivos_com_hash_exclusivo(hash_total)
    
    # Copiar arquivos únicos
    hash_relatorios.copiar_arquivos_unicos(arquivos_unicos, 'relatorios_pdf', "pasta_arquivos_unicos")

if __name__ == '__main__':
    main()