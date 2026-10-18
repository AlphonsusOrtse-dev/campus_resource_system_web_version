from flask import Flask

from app.extensions import db


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///campus.db"

    db.init_app(app)

    from app import models

    from app.routes import main
    app.register_blueprint(main)

    return app