# README

Este é um código Python que baixa relatórios da Controladoria-Geral da União (CGU), aplica hashes para identificar relatórios únicos e copia esses arquivos para uma pasta separada. O código consiste em vários módulos e scripts diferentes, cada um com uma função específica.

A busca e download de relatórios da CGU segue os seguintes passos:

1. Acesso às várias páginas de buscas no link: http://auditoria.cgu.gov.br. 
Sendo que cada página da consulta retorna uma relação com 15, 30 ou 50 
relatórios.

2. Após percorrer todas essas páginas, o script `busca.py` salva o conteúdo 
de cada uma delas em um arquivo `.json` que contém o `id` dos relatórios.

3. A partir desses arquivos `.json`, realiza-se o download da primeira parte 
de relatórios, `download_parte_1.py`. Essa primeira parte conta na data de 
hoje, 15.04.2023, com cerca de 10 mil relatórios.

4. O download da segunda parte de relatórios é realizado por meio do script 
`download_parte_2.py`. Essa segunda parte trouxe cerca de 13 mil arquivos de 
relatórios.

**Importante** mencionar que tanto na primeira parte, quanto
na segunda parte de downloads foram encontrados relatórios publicados em
duplicidade. O somatótio das duas consultas resutou em mais de 23 mil 
arquivos, mas é necessário localizar e excluir arquivos com conteúdo
duplicado, o que é realizado a seguir.

5. O script `hash.py` aplica um hash em cada arquivo e salva em um dicionário
com o nome dos arquivos. Hash único com mais de um arquivo indica duplicidade
de conteúdos.

6. Por último o script `copia.py` faz a cópia dos arquivos dos arquivos para
outra pasta. Se houver arquivos com contúdo duplicado, o script copia apenas
um de modo a deixar na pasta apenas uma cópia de cada relatório. Essa limpeza
reduziu a quantidade de relatórios de cerca de 23 mil para **15.861** arquivos
de relatórios na data de 15.04.2023.

7. Após a cópia é possível apagar a pasta onde os downloads inciais foram 
realizados (a que contém cerca de 23 mil arquivos) para não ocupar espaço
já que foram copiados para outra pasta. Não implementei script para deletar
os arquivos.

## Uso

O módulo principal é `main.py`, que coordena os outros módulos para baixar e processar os relatórios. Para usar o código, basta chamar o módulo principal:

```python
python main.py
```

## Dependências

Este código requer as seguintes bibliotecas externas:

- `requests`
- `datetime`
- `os`
- `time`
- `hashlib`

## Módulos

### `busca_pagina.py`

Este módulo contém uma função que consulta as páginas de pesquisa de relatórios da CGU e salva os arquivos JSON com os dados dos relatórios. A função `pesquisa_pagina_relatorios_cgu(max_offset)` recebe um número máximo de offsets a serem pesquisados e salva os arquivos JSON na pasta `paginas`.

O formato do arquivo `.json` com três relatórios está apresentado a seguir:

```
{"draw":0,
"recordsTotal":10000,
"recordsFiltered":10000,
"data":[{"id":1110235,
         "idArquivo":1159682,
        "tipoServico":"Avaliação",
        "grupoAtividade":"Outros",
        "linhaAcao":"Auditoria interna governamental",
        "avaliacaoPoliticaPublica":"Não",
        "titulo":"Publicação - SRP na Codevasf - Contratos n º 155/2020 e 164/2020 decorrentes da ARP 17/2020 para pavimentação em TSD",
        "dataPublicacao":"06/04/2023",
        "localidades":"Brasília/DF",
        "trecho":""},
        
        {"id":1199168,
        "idArquivo":1174885,
        "tipoServico":"Avaliação",
        "grupoAtividade":"Outros",
        "linhaAcao":"Auditoria interna governamental",
        "avaliacaoPoliticaPublica":"Não",
        "titulo":"Publicação - Avaliação de uso de SRP em obras de pavimentação pela CODEVASF - ação com a CGU/MA (contratos 8.469.00/2019, 8.470.00/2019 e 8.482.00/2019)",
        "dataPublicacao":"06/04/2023",
        "localidades":"Lago da Pedra/MA, São Luís/MA, Vitorino Freire/MA",
        "trecho":""},
        
        {"id":1438749,
        "idArquivo":1174159,
        "tipoServico":"Apuração",
        "grupoAtividade":"Outros",
        "linhaAcao":"Auditoria interna governamental",
        "avaliacaoPoliticaPublica":"Não",
        "titulo":"Relatório de Apuração 875361 - Análise de pagamentos de exames laboratoriais realizados pela Secretaria Municipal de Saúde de Criciúma/SC ",
        "dataPublicacao":"06/04/2023",
        "localidades":"Criciúma/SC",
        "trecho":""}],
        
"error":null}
```

### `download_parte_1.py`

Este módulo contém uma função que baixa relatórios da primeira parte da CGU, que estão disponíveis no site da CGU com um ID específico. A função `download_part_1(page_folder, reports_folder)` recebe duas pastas como argumentos: a pasta `page_folder` com os arquivos JSON baixados com o módulo `busca_pagina.py` e a pasta `reports_folder` para salvar os arquivos PDF baixados.

### `download_parte_2.py`

Este módulo contém uma função que baixa relatórios da segunda parte da CGU, que estão disponíveis no site da CGU com um número sequencial. A função `download_part_2(folder)` recebe uma pasta `folder` como argumento para salvar os arquivos PDF baixados.

### `hash_relatorios.py`

Este módulo contém funções para gerar hashes dos relatórios baixados e identificar relatórios únicos. A função `hash_relatorios(folder)` gera um hash para cada arquivo na pasta `folder`. A função `contagem_hash(hash_total)` conta quantos arquivos possuem o mesmo hash em `hash_total`. A função `arquivos_com_hash_exclusivo(hash_total)` cria uma lista de arquivos únicos. A função `copiar_arquivos_unicos(arquivos_unicos, pasta_origem, pasta_destino)` copia os arquivos únicos para outra pasta.

### `save_log.py`

Este módulo contém uma função que salva o log dos arquivos baixados.

## Como usar

1. Clone este repositório:

   ```bash
   git clone https://github.com/secom/cgu-reports-downloader.git
   ```

2. Navegue até a pasta clonada:

   ```bash
   cd cgu-reports-downloader
   ```

3. Crie um ambiente virtual e instale as dependências:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. Execute o módulo principal:

   ```bash
   python main.py
   ```

   Os relatórios baixados estarão na pasta `pasta_arquivos_unicos`.