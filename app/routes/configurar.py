from flask import Blueprint, render_template, request, jsonify
from app.utils.functions import commit
from sqlalchemy.exc import SQLAlchemyError
from app import db
from app.models.connections import Nivel

config_bp = Blueprint('cursos',__name__, url_prefix='/configurar')

@config_bp.route('/crear_nivel', methods=['POST'])
def crear_nivel():
    nombre = request.form.get('nombre')
    if not nombre:
        return jsonify({'success': False, 'message': 'El nombre es requerido.'}), 400

    nuevo_nivel = Nivel(nombre=nombre)
    return commit(nuevo_nivel,
           "Nivel creado correctamente",
           "No se pudo crear el nivel")