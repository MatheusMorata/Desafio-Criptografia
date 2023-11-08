import mysql.connector as mysql
import hashlib


def Create(id, userDocument, creditCardToken, value):
    conexao = mysql.connect(host="localhost",user="root",password="",database="Desafio")
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


def Update(id, userDocument, creditCardToken, value):
    conexao = mysql.connect(host="localhost",user="root",password="",database="Desafio")
    cursor = conexao.cursor()
    sql = "UPDATE creditCard SET userDocument = %s, creditCardToken = %s, value = %s WHERE id = %s"

    #Aqui são criadas as hashes
    hash = hashlib.sha512()
    hash1 = hashlib.sha512()
    hash.update(userDocument.encode('utf-8'))
    hash1.update(creditCardToken.encode('utf-8'))
    userDocument = hash.hexdigest()
    creditCardToken = hash1.hexdigest() 

    valores = (userDocument,creditCardToken,value,id)
    cursor.execute(sql,valores)
    conexao.commit()
    conexao.close()

def Read():
    json = {"dados":"nda"}
    lista = []
    sql = "SELECT * FROM creditCard"
    conexao = mysql.connect(host="localhost",user="root",password="",database="Desafio")
    cursor = conexao.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()
    for i in range(0,len(resultado)):
        lista.append({"id":resultado[i][0], "userDocument": resultado[i][1], "creditCardToken": resultado[i][2], "value":resultado[i][3]})
    json["dados"] = lista
    conexao.close()
    return json
    
def Delete(id):
    conexao = mysql.connect(host="localhost",user="root",password="",database="Desafio")
    id_tupla = (id,)
    sql = "DELETE FROM creditCard WHERE id = %s"
    cursor = conexao.cursor()
    cursor.execute(sql,id_tupla)
    conexao.commit()
    conexao.close()


Read()