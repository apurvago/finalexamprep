#hello1.py
from flask import Flask , jsonify 

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, Apurva!!!!"
    #return jsonify()
app.run()