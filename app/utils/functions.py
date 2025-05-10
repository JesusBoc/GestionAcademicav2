from app import db
from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError

def commit(modelo, on_succes="Operacion realizada con éxito", on_error="Operación fallida"):
    try:
        db.session.add(modelo)
        db.session.commit()
        return jsonify({
            'success': True,
            'message': on_succes,
        })
    except SQLAlchemyError as e:
        return jsonify({
                'message': f"{on_error}: {e}",
                'status': 400,
            }), 400