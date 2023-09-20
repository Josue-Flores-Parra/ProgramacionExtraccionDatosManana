
from mysql.connector import connect, Error

try:
    dbConexion = connect(host="localhost", user="root",
                         password="12345", database="olimpiadas")
    cursor = dbConexion.cursor()
    sql = "Select * from Genero"
    val = [("FEMENINO", 1), ("Masculino",)]
    cursor.execute(sql)
    lista_datos = cursor.fetchall()
    for item in lista_datos:
        print(item)
    #dbConexion.commit()
    #print(cursor.lastrowid)
    """
    sql = "show databases"
    cursor.execute(sql)
    lista_datos = cursor.fetchall()
    for item in lista_datos:
        print(item)
    """
except Error as e:
    print(e)
