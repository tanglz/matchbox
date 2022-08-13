from flask import (
    Blueprint, flash, redirect, render_template, request, session, url_for
)
from mysql.connector import Error
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.models.user import User

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        error = None
        if not firstname:
            error = 'firstname is required.'
        elif not lastname:
            error = 'lastname is required.'
        elif not email:
            error = 'email is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                pw = generate_password_hash(password)
                user = User(email,pw,firstname,lastname)
                user.insert()
            except Error:
                error = f"User {email} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        error = None
        user = User().queryByEmail(email)
        if user is None:
            error = 'Incorrect email.'
        elif not check_password_hash(user.password, password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('home.index'))

        flash(error)

    return render_template('auth/login.html')


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))