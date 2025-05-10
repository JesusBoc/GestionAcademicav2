from flask import Blueprint, render_template, request, jsonify
#from app import db
from app.models.connections import Nivel

config_bp = Blueprint('cursos',__name__, url_prefix='/configurar')

@config_bp.route('/crear_nivel', methods=['POST'])
def crear_nivel():
    nombre = request.form.get('nombre')
    if not nombre:
        return jsonify({'success': False, 'message': 'El nombre es requerido.'}), 400

    nuevo_nivel = Nivel(nombre=nombre)
    #db.session.add(nuevo_nivel)
    #db.session.commit()
    return jsonify({
        'success': True,
        'message': 'Nivel creado correctamente.',
        'nivel': {'id': nuevo_nivel.id, 'nombre': nuevo_nivel.nombre}
    })