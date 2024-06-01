# My Flask App

Este é um projeto Flask que demonstra a geração de gráficos a partir de dados de um banco de dados.

## Como Funciona

1. **Executando o Aplicativo:**
   - Certifique-se de ter Python e Flask instalados no seu ambiente.
   - Execute o arquivo `app.py` para iniciar o servidor Flask.
     ```bash
     python app.py
     ```
   - Navegue até o link fornecido no terminal para acessar o aplicativo.

2. **Interface do Usuário:**
   - Quando você acessa o aplicativo no navegador, você será direcionado para a página principal.
   - Na página principal, você verá dois botões: "Gerar Gráfico de Notas" e "Gerar Gráfico de Satisfação".

3. **Gerando Gráficos:**
   - Clique no botão "Gerar Gráfico de Notas" para gerar o primeiro gráfico.
   - Clique no botão "Gerar Gráfico de Satisfação" para gerar o segundo gráfico.

4. **Visualizando os Gráficos:**
   - Os gráficos serão exibidos na mesma página após você clicar nos botões correspondentes.

## Estrutura do Projeto

- `app.py`: Arquivo principal que inicializa a aplicação Flask e define as rotas.
- `modules/`:
  - `__init__.py`: Arquivo vazio que indica que `modules` é um pacote Python.
  - `database.py`: Contém funções para conectar-se ao banco de dados.
  - `graficos.py`: Contém funções para gerar gráficos a partir dos dados do banco de dados.
  - `routes.py`: Contém definições de rotas da aplicação Flask.
- `static/`: Diretório que contém arquivos estáticos como CSS e JavaScript.
- `templates/`: Diretório que contém os arquivos HTML usados nas rotas Flask.

## Requisitos

- Python
- Flask
- Pacotes Python necessários listados em `requirements.txt`
