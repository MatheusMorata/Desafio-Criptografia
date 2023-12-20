from flask import Flask,request
import BD

app = Flask(__name__)

# Endpoint para inserir dados no banco
@app.route("/create", methods=['POST'])
def Create():
    # JSON do usuário
    JSON = request.json
    return BD.Create(JSON)

# Endpoint para ler todos os campos
@app.route("/read", methods=['GET'])
def Read():
    return BD.Read()

# Endpoint para atualizar os dados no banco
@app.route("/update/<int:id>", methods=['POST'])
def Update(id):
    # JSON do usuário
    JSON = request.json
    return BD.Update(id,JSON)

# Endpoint para deletar os dados no banco
@app.route("/delete/<int:id>", methods=['GET'])
def Delete(id):
    return BD.Delete(id)

app.run()