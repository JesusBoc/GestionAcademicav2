from flask import Blueprint, render_template, request, redirect, url_for
from app.models.connections import Nivel

def getMainBP() -> Blueprint:
    main = Blueprint('main',__name__)

    @main.route('/')
    def index():
        return render_template('index.html')

    @main.route('/configurar')
    def configurar():
        #niveles = Nivel.query.all()
        return render_template('configuracion.html')
    
    return main