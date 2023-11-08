from flask import Flask
app = Flask(__name__)

@app.route("/create", methods=['POST'])
def create():
    
app.run()