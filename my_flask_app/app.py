from flask import Flask
from modules.routes import routes_blueprint

app = Flask(__name__)

app.register_blueprint(routes_blueprint)
 
if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=8080)
    app.run(debug=True)


