from app import create_app
from app.utils.serverless_functions import menu

app = create_app()

with app.app_context():
    menu()