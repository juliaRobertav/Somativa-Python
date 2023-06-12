import mysql.connector

def conect():
    conecta = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='colombo'
    )
    cursor = conecta.cursor()
    return conecta, cursor

