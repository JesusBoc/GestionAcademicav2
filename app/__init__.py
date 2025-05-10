from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .routes import getMainBP
from routes.cursos import cursos_bp

db = SQLAlchemy()

def create_app(config_class='app.config.Config'):
    app = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)

    with app.app_context():
        db.create_all()
        
    app.register_blueprint(getMainBP())
    app.register_blueprint(cursos_bp)
    return app