from flask import Blueprint, render_template, jsonify, current_app
from modules.database import conectar, verificar_status_banco_dados
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import io
import base64
from modules.database import conectar

routes_blueprint = Blueprint('routes', __name__)

def generate_graph():
    fig = Figure()
    ax = fig.subplots() 

    connection = conectar()
    cursor = connection.cursor()
    cursor.execute("SELECT nota, nome from psq")
    data = cursor.fetchall()
    connection.close()

    y_values = [row[0] for row in data]
    x_values = [row[1] for row in data]

    
    ax.plot(x_values, y_values)
    ax.set_xlabel('notas')
    ax.set_ylabel('qualidade')
    ax.set_title('Gráfico de notas dos alunos')
    ax.set_xticks(range(len(x_values)))
    ax.set_xticklabels(x_values, rotation=45, ha='right')
    
    img = io.BytesIO()
    fig.savefig(img, format='png', bbox_inches='tight')
    plt.close()
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    return f"data:image/png;base64,{graph_url}"

def plotar_grafico():
    with current_app.app_context():    
        fig = Figure()
        ax = fig.subplots()
        Nota = []
        total = []
        contagem = []
        # Conectar ao banco de dados
        conexao = conectar()

        # Criar um cursor para executar consultas SQL
        cursor = conexao.cursor()

            
            # Executar uma consulta SQL para ler a tabela retorno
        consulta = "SELECT * FROM retorno"
        cursor.execute(consulta)

            # Obter os resultados da consulta e guarda em resultados
        resultados = cursor.fetchall()
            
            #percorre linha por linha
        for linha in resultados:
            Nota.append(linha[2])   
                
        for ocorrencia in Nota:
            if total.count(ocorrencia)==0:                                          #verifica se a nota ja esta na lista "total". O count retorna quantas vezes a nota ocorre na lista
                total.append(ocorrencia)                                            #Se a nota não estiver na lista total, ela é adicionada.
                contagem.append(Nota.count(ocorrencia))  
        cursor.close()                                                              #ocorre a contagem (usando novamente o count) da lista Nota e é adicionada a lista contagem, registrando quantas vezes aquela nota aparece.

        nota_nome = ['Ruim', 'Insatisfeito', 'Regular', 'Satisfeito', 'Ótimo']  #nome das notas em ordem, o ultimo está vazio por ser o zero.

        cores = ['red', 'orange', 'yellow', 'green', 'blue', 'black']               #cores a serem usadas nas barras em ordem.
        plt.bar(total, contagem, color = cores)                                       
        plt.title('Nota de atendimento')                                            
        plt.xticks(total, nota_nome)    
        ax.set_ylabel('Número de respostas')                                           #titulo do eixo y
        ax.set_xticks(total)

        img = io.BytesIO()
        plt.savefig(img, format='jpg')
        plt.close()
        img.seek(0)
        graph_url = base64.b64encode(img.getvalue()).decode()
        return f"data:image/jpg;base64,{graph_url}"

@routes_blueprint.route('/')
def index():
    return render_template('index.html')

@routes_blueprint.route('/grafalunos', methods=['POST'])
def gerar_grafico():
    try:
        graph_url = generate_graph()
        return jsonify(success=True, graph_url=graph_url)
    except Exception as e:
        print(f"Error generating graph: {e}")
        return jsonify(success=False)
    

@routes_blueprint.route('/grafnotas', methods=['POST'])
def gerar_grafico_notas():
    try:
        graph_url = plotar_grafico()
        return jsonify(success=True, graph_url=graph_url)
    except Exception as e:
        print(f"Error generating graph: {e}")
        return jsonify(success=False)

@routes_blueprint.route('/status-banco-dados', methods=['GET'])
def verificar_status_servidor():
    try:
        status_banco_dados = verificar_status_banco_dados()
        return jsonify(success=True, status_banco_dados=status_banco_dados), 200
    except Exception as e:
        print(f"Erro ao verificar status do banco de dados: {e}")
        return jsonify(success=False), 500