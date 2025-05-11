from flask import Blueprint, render_template, request, jsonify
from app.utils.functions import commit
from app import db
from app.models.connections import Nivel, Grado

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

@config_bp.route('/crear_grado', methods=['POST'])
def crear_grado():
    nivel_id = request.form.get('nivel')
    nombre = request.form.get('nombre')
    if not nombre or not nivel_id:
        return jsonify({'success': False, 'message': 'El nombre y el nivel son requeridos.'}), 400
    
    grado = Grado(nombre=nombre,nivel_id=nivel_id)
    return commit(grado,
                  "Grado creado correctamente",
                  "No pudo crearse el grado",
                  )