import mysql.connector

def conectar():


    database = mysql.connector.connect(
        host = '127.0.0.1',
        port = 3306,
        user = 'root',
        passwd = '',
        database = 'curs_python'
    )

    cursor = database.cursor(buffered=True)

    return [ database, cursor ]