from flask import Flask,request,make_response,jsonify
import BD
app = Flask(__name__)

@app.route("/create", methods=['POST'])
def Create():
    teste = request.json
    return teste

@app.route("/read", methods=['GET'])
def Read():
    return make_response(jsonify(BD.Read())) 

@app.route("/update", methods=['PUT'])
def Update():
    return "Recebi um PUT"

@app.route("/delete", methods=['DELETE'])
def Delete():
    return "Recebi um DELETE"

app.run()