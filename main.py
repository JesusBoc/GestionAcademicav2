# TODO inicializar todo :(
from app import create_app
from flask import Flask, render_template, request, redirect

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)