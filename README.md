
# 📋 Sistema de Controle de Visitantes

Este projeto é uma aplicação web simples desenvolvida com **Flask** (Python) que se conecta a um banco de dados **Firebird** para consultar e exibir a quantidade de visitantes por setor. O usuário pode filtrar os dados por **data inicial**, **data final** e **setor**, visualizando os resultados em uma tabela dinâmica.

---

## 🚀 Funcionalidades

- 🔍 Filtrar visitas por data e setor
- 📊 Exibir quantidade de visitas por setor em uma tabela
- 🗃️ Obter dinamicamente a lista de setores disponíveis
- 🎨 Interface responsiva e estilizada com CSS

---

## 🛠️ Tecnologias Utilizadas

- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [FirebirdSQL](https://firebirdsql.org/)
- HTML5 & CSS3

---

## 📁 Estrutura do Projeto

```
controle_visitantes/
├── app.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── fUNDO.png
└── README.md
```

---

## ⚙️ Como Funciona

### 🔌 Backend - `app.py`

- Estabelece conexão com o banco **Firebird**.
- Rota principal (`/`) aceita filtros de data e setor via query string.
- Função `get_data_from_firebird()` realiza a consulta SQL com filtros opcionais.
- Função `get_setores_from_firebird()` retorna os setores disponíveis para o `<select>` no formulário.
- Usa `render_template()` para renderizar a página HTML com os dados retornados do banco.

### 🖼️ Frontend - `index.html`

- Contém o formulário com campos:
  - Data inicial
  - Data final
  - Seleção de setor
- Exibe os dados retornados do backend em uma **tabela responsiva**.
- Utiliza Jinja2 para exibir dinamicamente as opções de setor e os resultados da consulta.

### 🎨 Estilo - `style.css`

- Estiliza formulário, botões, tabela e responsividade.
- Exibe um logotipo no canto superior direito.
- Design limpo e adaptável para dispositivos móveis.

---

## 🧪 Como Executar o Projeto

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/controle_visitantes.git
   cd controle_visitantes
   ```

2. **Crie um ambiente virtual e ative**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install flask firebirdsql
   ```

4. **Configure o caminho do banco de dados no `app.py`**:
   ```python
   database='C:\\caminho\\para\\seu\\SGI.FDB'
   ```

5. **Inicie o servidor Flask**:
   ```bash
   python app.py
   ```

6. **Acesse via navegador**:
   ```
   http://localhost:5000
   ```

---

## 🔐 Observações de Segurança

- A senha do banco (`masterkey`) está hardcoded no código — recomenda-se usar variáveis de ambiente para produção.
- Evite expor o endereço IP do banco de dados em ambientes públicos.

---

## 📝 Licença

Este projeto é de uso interno e educacional. Modifique livremente conforme sua necessidade.

# 📋 Sistema de Controle de Visitantes

Este projeto é uma aplicação web simples desenvolvida com **Flask** (Python) que se conecta a um banco de dados **Firebird** para consultar e exibir a quantidade de visitantes por setor. O usuário pode filtrar os dados por **data inicial**, **data final** e **setor**, visualizando os resultados em uma tabela dinâmica.

---

## 🚀 Funcionalidades

- 🔍 Filtrar visitas por data e setor
- 📊 Exibir quantidade de visitas por setor em uma tabela
- 🗃️ Obter dinamicamente a lista de setores disponíveis
- 🎨 Interface responsiva e estilizada com CSS

---

## 🛠️ Tecnologias Utilizadas

- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [FirebirdSQL](https://firebirdsql.org/)
- HTML5 & CSS3

---

## 📁 Estrutura do Projeto

```
controle_visitantes/
├── app.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── fUNDO.png
└── README.md
```

---

## ⚙️ Como Funciona

### 🔌 Backend - `app.py`

- Estabelece conexão com o banco **Firebird**.
- Rota principal (`/`) aceita filtros de data e setor via query string.
- Função `get_data_from_firebird()` realiza a consulta SQL com filtros opcionais.
- Função `get_setores_from_firebird()` retorna os setores disponíveis para o `<select>` no formulário.
- Usa `render_template()` para renderizar a página HTML com os dados retornados do banco.

### 🖼️ Frontend - `index.html`

- Contém o formulário com campos:
  - Data inicial
  - Data final
  - Seleção de setor
- Exibe os dados retornados do backend em uma **tabela responsiva**.
- Utiliza Jinja2 para exibir dinamicamente as opções de setor e os resultados da consulta.

### 🎨 Estilo - `style.css`

- Estiliza formulário, botões, tabela e responsividade.
- Exibe um logotipo no canto superior direito.
- Design limpo e adaptável para dispositivos móveis.

---

## 🧪 Como Executar o Projeto

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/controle_visitantes.git
   cd controle_visitantes
   ```

2. **Crie um ambiente virtual e ative**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install flask firebirdsql
   ```

4. **Configure o caminho do banco de dados no `app.py`**:
   ```python
   database='C:\\caminho\\para\\seu\\SGI.FDB'
   ```

5. **Inicie o servidor Flask**:
   ```bash
   python app.py
   ```

6. **Acesse via navegador**:
   ```
   http://localhost:5000
   ```

---

## 🔐 Observações de Segurança

- A senha do banco (`masterkey`) está hardcoded no código — recomenda-se usar variáveis de ambiente para produção.
- Evite expor o endereço IP do banco de dados em ambientes públicos.

---

## 📝 Licença

Este projeto é de uso interno e educacional. Modifique livremente conforme sua necessidade.

