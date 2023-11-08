from flask import Flask,request,make_response,jsonify
import BD

app = Flask(__name__)

#Endpoint para criar um campo
@app.route("/create", methods=['POST'])
def Create():
    JSON = request.json
    BD.Create(JSON['id'],JSON['userDocument'],JSON['creditCardToken'],JSON['value'])
    return make_response(jsonify(BD.Read())) 

#Endpoint para ler todos os campos
@app.route("/read", methods=['GET'])
def Read():
    return make_response(jsonify(BD.Read())) 

#Endpoint para atualizar um campo
@app.route("/update", methods=['POST'])
def Update():
    JSON = request.json
    BD.Update(JSON["userDocument"], JSON["creditCardToken"], JSON["value"], JSON["id"])
    return make_response(jsonify(BD.Read())) 


#Endpoint para deletar um campo
@app.route("/delete/<int:id>", methods=['GET'])
def Delete(id):
    BD.Delete(id)
    return make_response(jsonify(BD.Read())) 
    

app.run()