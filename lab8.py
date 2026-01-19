from flask import Blueprint, render_template, request, redirect, abort
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import or_

from db import db
from db.models import users, articles

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

    password_hash = generate_password_hash(password, method='pbkdf2:sha256')
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
def articles_list():
    user_articles = articles.query.filter_by(login_id=current_user.id).all()
    return render_template('lab8/articles.html', articles=user_articles)


@lab8.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'GET':
        return render_template('lab8/create.html')

    title = request.form.get('title')
    article_text = request.form.get('article_text')
    is_public = bool(request.form.get('is_public'))

    if not title or not article_text:
        return render_template('lab8/create.html', error='Заполните все поля')

    new_article = articles(
        login_id=current_user.id,
        title=title,
        article_text=article_text,
        is_public=is_public
    )
    db.session.add(new_article)
    db.session.commit()
    return redirect('/lab8/articles')


@lab8.route('/edit/<int:article_id>', methods=['GET', 'POST'])
@login_required
def edit(article_id):
    article = articles.query.get(article_id)
    if not article:
        abort(404)
    if article.login_id != current_user.id:
        abort(403)

    if request.method == 'GET':
        return render_template('lab8/edit.html', article=article)

    title = request.form.get('title')
    article_text = request.form.get('article_text')
    is_public = bool(request.form.get('is_public'))

    if not title or not article_text:
        return render_template(
            'lab8/edit.html',
            article=article,
            error='Заполните все поля'
        )

    article.title = title
    article.article_text = article_text
    article.is_public = is_public
    db.session.commit()
    return redirect('/lab8/articles')


@lab8.route('/delete/<int:article_id>', methods=['POST'])
@login_required
def delete(article_id):
    article = articles.query.get(article_id)
    if not article:
        abort(404)
    if article.login_id != current_user.id:
        abort(403)

    db.session.delete(article)
    db.session.commit()
    return redirect('/lab8/articles')


@lab8.route('/public')
def public_articles():
    public_list = articles.query.filter_by(is_public=True).all()
    return render_template('lab8/public.html', articles=public_list)


@lab8.route('/search')
def search():
    query = request.args.get('q', '').strip()
    if not query:
        return render_template('lab8/search.html', query=query, articles=[])

    pattern = f'%{query}%'
    search_filter = or_(
        articles.title.ilike(pattern),
        articles.article_text.ilike(pattern)
    )

    if current_user.is_authenticated:
        results = articles.query.filter(
            search_filter,
            or_(
                articles.is_public.is_(True),
                articles.login_id == current_user.id
            )
        ).all()
    else:
        results = articles.query.filter(
            search_filter,
            articles.is_public.is_(True)
        ).all()

    return render_template('lab8/search.html', query=query, articles=results)


@lab8.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/lab8/')
