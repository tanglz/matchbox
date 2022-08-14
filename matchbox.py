from flask import Flask
from mysql_connector import init_mysqldb
import auth
import home

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev',
)

app.register_blueprint(auth.bp)
app.register_blueprint(home.he)

if __name__ == "__main__":
    with app.app_context():
        init_mysqldb()
    app.run(host='0.0.0.0')


