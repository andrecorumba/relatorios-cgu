# Module: save_log
# Path: scripts/save_log.py
# Salva o log dos arquivos baixados

import os
import datetime

def save_log(log_name, file_name):

    # Pasta onde os logs serão salvos. Substitua pelo caminho da sua pasta
    folder = 'log'

    # Nome final do arquivo
    file_path = os.path.join(folder, log_name)

    # Salva o log
    with open(file_path, 'a') as file:

        # Salva o log no formato: 
        # Arquivo: relatorios_pdf/relatorio_1.pdf, 2023-04-15 03:49:47.524944
        file.write(f"Arquivo: {file_name}, {datetime.datetime.now()}\n")