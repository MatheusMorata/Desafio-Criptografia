from flask import Flask,request,make_response,jsonify
import BD
app = Flask(__name__)

@app.route("/create", methods=['POST'])
def Create():
    JSON = request.json
    BD.Create(JSON['id'],JSON['userDocument'],JSON['creditCardToken'],JSON['value'])
    return make_response(jsonify(BD.Read())) 
@app.route("/read", methods=['GET'])
def Read():
    return make_response(jsonify(BD.Read())) 

@app.route("/update", methods=['PUT'])
def Update():
    JSON = request.json
    BD.Update(JSON["userDocument"], JSON["creditCardToken"], JSON["value"], JSON["id"])
    return make_response(jsonify(BD.Read())) 

@app.route("/delete/<int:id>", methods=['DELETE'])
def Delete(id):
    BD.Delete(id)
    return make_response(jsonify(BD.Read())) 
    

app.run()