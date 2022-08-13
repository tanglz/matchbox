from flask import (
    Blueprint, render_template, session
)

from flaskr.models.user import User

he = Blueprint('home', __name__, url_prefix='/home')


@he.route('/index', methods=('GET','POST'))
def index():
    user_id = session.get('user_id')
    if user_id is None:
        user = None
    else:
        user = User().query_by_id(user_id)
    return render_template('home/index.html', user=user)
