# Controle de Visitantes com Flask e Firebird

Este projeto consiste em uma aplicação web desenvolvida com Flask (um microframework Python) para fornecer uma interface de controle e visualização de dados de visitantes armazenados em um banco de dados Firebird.

## Funcionalidades

* **Filtragem de Dados:** Permite filtrar os dados de visitas por um período específico (data inicial e data final) e por setor.
* **Listagem de Visitas por Setor:** Exibe uma tabela mostrando os setores e a quantidade de visitas registradas em cada um, ordenados pela quantidade decrescente.
* **Seleção de Setores:** Um menu dropdown dinâmico é carregado com os setores distintos existentes no banco de dados, facilitando a seleção para filtragem.
* **Interface Amigável:** Uma interface web simples e responsiva para facilitar a interação do usuário.

## Pré-requisitos

* **Python 3.x:** Necessário para executar a aplicação Flask.
* **Flask:** O microframework web Python utilizado. Pode ser instalado com `pip install Flask`.
* **python-firebird:** O driver Python para conectar ao banco de dados Firebird. Pode ser instalado com `pip install python-firebird`.
* **Banco de Dados Firebird:** Uma instância do banco de dados Firebird contendo a tabela `VISITA` com as colunas `DT_VISITA` (data da visita) e `DESTINO` (setor de destino).
* **Acesso ao Banco de Dados Firebird:** As credenciais de acesso ao banco de dados (host, database path, usuário e senha) devem ser configuradas corretamente no código Python.

## Configuração

1.  **Instalar as dependências:**
    ```bash
    pip install Flask python-firebird
    ```

2.  **Configurar a conexão com o banco de dados Firebird:**
    No arquivo `app.py`, ajuste os parâmetros de conexão dentro das funções `get_data_from_firebird` e `get_setores_from_firebird`:
    ```python
    conn = firebirdsql.connect(
        host='192.168.0.139',  # Substitua pelo IP ou hostname do seu servidor Firebird
        database='C:\\sgi\\database\\SGI.FDB',  # Substitua pelo caminho do seu arquivo de banco de dados
        user='SYSDBA',          # Substitua pelo seu usuário do Firebird
        password='masterkey'   # Substitua pela sua senha do Firebird
    )
    ```

3.  **Arquivo de Banco de Dados:** Certifique-se de que o caminho para o arquivo do banco de dados Firebird (`C:\\sgi\\database\\SGI.FDB`) esteja correto.

4.  **Imagem da Logo:** A imagem `fUNDO.png` utilizada como logo deve estar presente na pasta `static/`.

## Execução da Aplicação

1.  **Salve os arquivos:** Salve o código Python como `app.py`, o HTML como `templates/index.html` e o CSS como `static/style.css`. Crie as pastas `templates` e `static` se não existirem.

2.  **Execute a aplicação Flask:**
    ```bash
    python app.py
    ```

3.  **Acesse no navegador:** Abra seu navegador web e acesse o endereço `http://127.0.0.1:5000/` ou o endereço IP e porta onde a aplicação estiver rodando (conforme indicado no terminal).

## Utilização

1.  **Página Inicial:** Ao acessar a página inicial, você verá um formulário com campos para selecionar a data inicial, a data final e um dropdown para escolher o setor. Inicialmente, a tabela exibirá todos os registros de visitas agrupados por setor.

2.  **Filtrando por Data:** Se você preencher os campos "Data Inicial" e/ou "Data Final" e clicar em "Filtrar", a tabela será atualizada para mostrar apenas as visitas dentro do período especificado.

3.  **Filtrando por Setor:** Ao selecionar um setor no dropdown e clicar em "Filtrar", a tabela mostrará apenas as visitas com o destino correspondente ao setor selecionado. A busca por setor é parcial, ou seja, se você digitar ou selecionar "ADM", serão exibidos setores como "ADMINISTRATIVO", "ADM FINANCEIRO", etc.

4.  **Limpando os Filtros:** Ao clicar no botão "Limpar Filtro", todos os filtros serão removidos e a tabela exibirá novamente todos os registros agrupados por setor.

