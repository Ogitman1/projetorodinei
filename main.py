import pymysql
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox

def plotar_grafico():

    Nota = []
    total = []
    contagem = []
    # Conectar ao banco de dados
    conexao = pymysql.connect(host='italo.mysql.uhserver.com',
                              user='logica2024',
                              password='@Aluno2024',
                              database='italo')

    # Criar um cursor para executar consultas SQL
    cursor = conexao.cursor()

    try:
        
        # Executar uma consulta SQL para ler a tabela retorno
        consulta = "SELECT * FROM retorno"
        cursor.execute(consulta)

        # Obter os resultados da consulta e guarda em resultados
        resultados = cursor.fetchall()
        
        #percorre linha por linha
        for linha in resultados:
            Nota.append(linha[2])   
            # var = len(Nota)                                                #adicionando a terceira coluna (nota) da tabela na lista Nota.
           # print(var)
        for ocorrencia in Nota:
            if total.count(ocorrencia)==0:                                          #verifica se a nota ja esta na lista "total". O count retorna quantas vezes a nota ocorre na lista
                total.append(ocorrencia)                                            #Se a nota não estiver na lista total, ela é adicionada.
                contagem.append(Nota.count(ocorrencia))  
        cursor.close()                                                              #ocorre a contagem (usando novamente o count) da lista Nota e é adicionada a lista contagem, registrando quantas vezes aquela nota aparece.

        nota_nome = ['Ruim', 'Insatisfeito', 'Regular', 'Satisfeito', 'Ótimo', ""]  #nome das notas em ordem, o ultimo está vazio por ser o zero.

        cores = ['red', 'orange', 'yellow', 'green', 'blue', 'black']               #cores a serem usadas nas barras em ordem.

        plt.bar(total, contagem, color=cores)                                       #grafico de barra com base nos dados das listas total (eixo x) e contagem (eixo y) utilizando as cores contidas em "cores".
        plt.title('Nota de atendimento')                                            #titulo do gráfico
        
        plt.ylabel('Número de respostas')                                           #titulo do eixo y
        
        plt.xticks(total, nota_nome)                                                #aqui é substituido os numeros do eixo x pelos nomes contidos em "nota_nome"
        plt.xlim(0.5, 5.5)                                                          #limita o grafico entre 1 e 5
        plt.show()                                                                  #mostra o gráfico

    #mensagem de erro  
    except pymysql.Error as e:
        messagebox.showerror("Erro", f"Erro ao acessar o banco de dados: {e}")




# basicamente cria uma janela de 300x100
root = Tk()
root.title("Visualizador de Dados")
root.geometry("300x100")

# apenas um botão pra executar a função principal
btn_plotar = Button(root, text="Gerar gráfico", command=plotar_grafico)
btn_plotar.pack(pady=25)

#Inicia tudo basicamente
root.mainloop()
