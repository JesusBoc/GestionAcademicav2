from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_class='app.config.Config'):
    app = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from app.routes import main as main_blueprint
    from app.routes.configurar import config_bp as config_blueprint
        
    app.register_blueprint(main_blueprint)
    app.register_blueprint(config_blueprint)
    return app