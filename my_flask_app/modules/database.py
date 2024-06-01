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