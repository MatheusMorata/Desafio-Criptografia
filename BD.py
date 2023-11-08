import mysql.connector as mysql

conexao = mysql.connect(host="localhost",user="root",password="",database="Desafio")

def Create(id, userDocument, creditCardToken, value):
    cursor = conexao.cursor()
    sql = "INSERT INTO creditCard(id, userDocument, creditCardToken, value) VALUES (%s,%s,%s,%s)"
    valores = (id, userDocument, creditCardToken, value)
    cursor.execute(sql,valores)
    conexao.commit()
    conexao.close()