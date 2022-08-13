from flask import Flask
from flaskr.mysql_connector import init_mysqldb


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    with app.app_context():
            init_mysqldb()

    from . import auth
    from . import home
    app.register_blueprint(auth.bp)
    app.register_blueprint(home.he)
    return app