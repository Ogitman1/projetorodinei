from flask import Flask, render_template, jsonify
import pymysql
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

def generate_graph():
    # Conectar ao banco de dados
    connection = pymysql.connect(
        host='italo.mysql.uhserver.com',
        user='logica2024',
        password='@Aluno2024',
        database='italo'
    )

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
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    return f"data:image/png;base64,{graph_url}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/grafalunos', methods=['POST'])
def gerar_grafico():
    try:
        graph_url = generate_graph()
        return jsonify(success=True, graph_url=graph_url)
    except Exception as e:
        print(f"Error generating graph: {e}")
        return jsonify(success=False)

if __name__ == '__main__':
    app.run(debug=True)
