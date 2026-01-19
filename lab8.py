from flask import Blueprint, render_template, request, redirect
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

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
    login_user(new_user)
    return redirect('/lab8/')


@lab8.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('lab8/login.html')

    login = request.form.get('login')
    password = request.form.get('password')

    if not login or not password:
        return render_template('lab8/login.html', error='Заполните поля')

    user = users.query.filter_by(login=login).first()
    if not user or not check_password_hash(user.password, password):
        return render_template('lab8/login.html', error='Логин или пароль неверны')

    remember = bool(request.form.get('remember'))
    login_user(user, remember=remember)
    return redirect('/lab8/')


@lab8.route('/articles')
@login_required
def articles():
    return render_template('lab8/articles.html')


@lab8.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/lab8/')
