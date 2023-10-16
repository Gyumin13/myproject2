from flask import Flask
from pybo.views.main_views import bp as main_bp

def create_app():
    app = Flask(__name__)

    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app
