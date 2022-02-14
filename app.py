from flask import Flask

app = Flask(__name__)

COUNTER = 0

@app.route("/")
def index():
    return "Hello World!"

@app.route("/counter")
def counter():
    global COUNTER
    COUNTER += 1
    return(dict(counter=COUNTER))