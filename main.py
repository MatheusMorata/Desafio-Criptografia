from flask import Flask,request
app = Flask(__name__)

@app.route("/create", methods=['POST'])
def create():
    return "Recebi um post"
    

app.run()