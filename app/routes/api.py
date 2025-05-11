from typing import List
from flask import Blueprint, jsonify
from app.utils.functions import commit
from app.models.connections import Nivel, Grado

api_bp = Blueprint('api',__name__, url_prefix='/api')

@api_bp.route('')
def api():
    return jsonify(
        {
            'message': 'Esta es la api que tengo dispuesta para el proyecto',
            'endpoints': ['get_niveles','get_all_grados','get_asignaturas']
        }
    )

@api_bp.route('/get_niveles') 
def get_niveles():
    niveles: List[Nivel] = Nivel.query.all()
    out = [nivel.to_dict() for nivel in niveles]
    return jsonify(out)

@api_bp.route('/get_all_grados')
def get_all_grados():
    grados: List[Grado] = Grado.query.all()
    out = [grado.to_dict() for grado in grados]
    return jsonify(out)

""" @api_bp.route('/grado/<int:grado_id>')
def get_all_grados(grado_id):
    grado = Grado.query.get_or_404(grado_id)
    out = {}
    for grado in grados:
        out[grado.id] = {
            'nombre': grado.nombre,
            'nivel_id': grado.nivel_id,
        }
    return jsonify(out) """