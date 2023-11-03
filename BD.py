import mysql.connector as mysql

BD_conexao = mysql.connect(host="localhost",user="root",password="",database="Desafio")

BD_conexao.close()
