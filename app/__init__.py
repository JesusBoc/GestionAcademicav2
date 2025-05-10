from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .routes import main
from .routes.cursos import cursos_bp

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()
        
    app.register_blueprint(main)
    app.register_blueprint(cursos_bp)
    return app