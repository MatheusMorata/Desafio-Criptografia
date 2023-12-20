import mysql.connector as mysql
import json
import hashlib


def hash(hash):
    # Criar um objeto hash SHA-512
    sha512 = hashlib.sha512()

    # Atualizar o hash com a string convertida para bytes
    sha512.update(hash.encode('utf-8'))

    # Obter o hash resultante em formato hexadecimal
    resultado = sha512.hexdigest()

    return resultado

def Create(json):
    # Função que realiza um INSERT no banco
    conexao = mysql.connect(host="127.0.0.1",user="root",password="",database="desafio")
    sql = "INSERT INTO creditCard(id, userDocument, creditCardToken, value) VALUES (%s,%s,%s,%s)"
    cursor = conexao.cursor()
    tupla = (json["id"],hash(json["userDocument"]),hash(json["creditCardToken"]),json["Value"])

    try:
        # Executar a consulta
        cursor.execute(sql,tupla)
        conexao.commit()

    except mysql.Error as erro:
        print(f"Erro ao executar a consulta: {erro}")

    finally:
        # Fechar o cursor e a conexão
        cursor.close()
        conexao.close()

    return Read()
def Update(id,json):
    # Função que realiza um UPDATE no banco
    conexao = mysql.connect(host="localhost",user="root",password="",database="Desafio")
    cursor = conexao.cursor()
    sql = "UPDATE creditCard SET id = %s, userDocument = %s, creditCardToken = %s, value = %s WHERE id = %s"
    tupla = (json["id"], hash(json["userDocument"]), hash(json["creditCardToken"]), json["Value"], id)
    
    try:
        # Executar a consulta
        cursor.execute(sql,tupla)
        conexao.commit()

    except mysql.Error as erro:
        print(f"Erro ao executar a consulta: {erro}")

    finally:
        # Fechar o cursor e a conexão
        cursor.close()
        conexao.close()
    return Read()

def Read():
    # Função que realiza o SELECT dentro do banco
    saida = []
    sql = "SELECT * FROM creditCard"
    conexao = mysql.connect(host="localhost",user="root",password="",database="Desafio")
    cursor = conexao.cursor()

    try:
        # Executar a consulta
        cursor.execute(sql)

        # Recuperar os resultados
        resultados = cursor.fetchall()

    except mysql.Error as erro:
        print(f"Erro ao executar a consulta: {erro}")

    finally:
        # Fechar o cursor e a conexão
        cursor.close()
        conexao.close()

    for i in range(0,len(resultados)):
        teste = {"id":resultados[i][0],
                 "userDocument":resultados[i][1],
                 "creditCardToken":resultados[i][2],
                 "Value":resultados[i][3]}
        saida.append(teste)
        teste = {} 

    return json.dumps(saida, indent=len(saida))

def Delete(id):
    # Função que realiza o DELETE dentro do banco
    tupla = (id,)
    conexao = mysql.connect(host="localhost",user="root",password="",database="Desafio")
    sql = "DELETE FROM creditCard WHERE id = %s"
    cursor = conexao.cursor()

    try:
        # Executar a consulta
        cursor.execute(sql,tupla)
        conexao.commit()
    except mysql.Error as erro:
        print(f"Erro ao executar a consulta: {erro}")

    finally:
        # Fechar o cursor e a conexão
        cursor.close()
        conexao.close()
    return Read()
