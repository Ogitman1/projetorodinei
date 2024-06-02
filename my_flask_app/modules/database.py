import pymysql

def conectar():
    # Conectar ao banco de dados
    connection = pymysql.connect(
        host='italo.mysql.uhserver.com',
        user='logica2024',
        password='@Aluno2024',
        database='italo'
    )

    return connection

def verificar_status_banco_dados():
    try:
        # Tente abrir uma conexão com o banco de dados
        conn = conectar()
        # Se a conexão for bem-sucedida, o banco de dados está online
        return "Online"
    except Exception as e:
        # Se ocorrer algum erro, o banco de dados está offline
        return "Offline"