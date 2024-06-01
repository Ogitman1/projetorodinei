import pymysql
import matplotlib.pyplot as plt
import io
import base64
from modules.database import conectar
connection = conectar()

def generate_graph():
    

    cursor = connection.cursor()
    cursor.execute("SELECT nota, nome from psq")
    data = cursor.fetchall()
    connection.close()

    # Suponha que 'data' contenha os valores para o gráfico
    x_values = [row[0] for row in data]
    y_values = [row[1] for row in data]

    plt.figure()
    plt.plot(x_values, y_values)
    plt.xlabel('notas')
    plt.ylabel('qualidade')
    plt.title('Gráfico de notas dos alunos')

    img = io.BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    return f"data:image/png;base64,{graph_url}"

def plotar_grafico():
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

    plt.bar(total, contagem, color=cores)                                       #grafico de barra com base nos dados das listas total (eixo x) e contagem (eixo y) utilizando as cores contidas em "cores".
    plt.title('Nota de atendimento')                                            #titulo do gráfico
        
    plt.ylabel('Número de respostas')                                           #titulo do eixo y
        
    plt.xticks(total, nota_nome)                                                #aqui é substituido os numeros do eixo x pelos nomes contidos em "nota_nome"
    #plt.xlim(0.5, 5.5)                                                          #limita o grafico entre 1 e 5
    img = io.BytesIO()
    plt.savefig(img, format='jpg')
    plt.close()
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    return f"data:image/jpg;base64,{graph_url}"
