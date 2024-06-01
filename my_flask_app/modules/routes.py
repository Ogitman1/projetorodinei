from flask import Blueprint, render_template, jsonify
from modules.graficos import generate_graph, plotar_grafico


routes_blueprint = Blueprint('routes', __name__)

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