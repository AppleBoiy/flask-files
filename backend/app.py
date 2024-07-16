from flask import Flask

from backend.config import Config
from backend.models import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.drop_all()
        db.create_all()  # Create database tables if they do not exist

    # Register blueprints
    from backend.routes import bp
    app.register_blueprint(bp)

    return app
