# TODO inicializar todo :(
from app import create_app
from flask import Flask, render_template, request, redirect

app = create_app()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registrar")
def registrar():
    return render_template("registrar.html")

if __name__ == '__main__':
    app.run(debug=True)