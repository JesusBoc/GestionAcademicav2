from flask import Blueprint, render_template

cursos_bp = Blueprint('cursos',__name__, url_prefix='/cursos')

@cursos_bp.route('/')
def mostrarCursos():
    return