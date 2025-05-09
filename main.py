# TODO inicializar todo :(

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registrar")
def registrar():
    return render_template("registrar.html")

if __name__ == '__main__':
    app.run(debug=True)