from flask import Blueprint, render_template, request, redirect
from werkzeug.security import generate_password_hash

from db import db
from db.models import users

lab8 = Blueprint('lab8', __name__)


@lab8.route('/')
def index():
    return render_template('lab8/index.html')


@lab8.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab8/register.html')

    login = request.form.get('login')
    password = request.form.get('password')

    if not login or not password:
        return render_template('lab8/register.html', error='Заполните поля')

    existing_user = users.query.filter_by(login=login).first()
    if existing_user:
        return render_template('lab8/register.html', error='Такой пользователь уже существует')

    password_hash = generate_password_hash(password)
    new_user = users(login=login, password=password_hash)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/lab8/')
