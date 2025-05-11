from typing import List
from flask import Blueprint, jsonify
from app.utils.functions import commit
from app.models.connections import *

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

@api_bp.route('/get_all_grados_deep')
def get_all_grados_deep():
    grados: List[Grado] = Grado.query.all()
    out = [grado.to_dict_deep() for grado in grados]
    return jsonify(out)

@api_bp.route('/get_all_salones')
def get_all_salones():
    salones: List[Salon] = Salon.query.all()
    out = [salon.to_dict() for salon in salones]
    return jsonify(out)

@api_bp.route('/get_all_salones_deep')
def get_all_salones_deep():
    salones: List[Salon] = Salon.query.all()
    out = [salon.to_dict_deep() for salon in salones]
    return jsonify(out)

@api_bp.route('/grado/<int:grado_id>')
def get_grado(grado_id):
    grado: Grado = Grado.query.get_or_404(grado_id)
    return jsonify(grado.to_dict())