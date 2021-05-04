from mysql.connector import connect

params = None

def execute(sql, params= None):
    with connect(host= "localhost", user = "root", password = "123456", database = "locadora")as conn:
        with conn.cursos() as cursor:
            cursor.execute(sql,params)
            conn.commit()



def query(sql,params=None):
    with connect(host = "localhost", user = "root",password = "123456",database = "locadora" )as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql,params)
            return cursor.fetchall()

