from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return "hello"

@app.route("/db")
def get_thing():
    return app.db["foo"]
