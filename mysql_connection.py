import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host = 'yh-db.chyowr2bx2g2.ap-northeast-2.rds.amazonaws.com',
        database = 'posting_db',
        user = 'posting_user',
        password = 'posting1234'
    )
    return connection