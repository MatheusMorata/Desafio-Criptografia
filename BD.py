import mysql.connector as mysql
import hashlib

conexao = mysql.connect(host="localhost",user="root",password="",database="Desafio")

def Create(id, userDocument, creditCardToken, value):
    sql = "INSERT INTO creditCard(id, userDocument, creditCardToken, value) VALUES (%s,%s,%s,%s)"
    cursor = conexao.cursor()
    
    #Aqui são criadas as hashes
    hash = hashlib.sha512()
    hash1 = hashlib.sha512()
    hash.update(userDocument.encode('utf-8'))
    hash1.update(creditCardToken.encode('utf-8'))
    userDocument = hash.hexdigest()
    creditCardToken = hash1.hexdigest()

    valores = (id,userDocument,creditCardToken,value)

    cursor.execute(sql,valores)
    conexao.commit()
    conexao.close()

