from flask import Flask, url_for, request, redirect, abort, render_template, session
import os
from datetime import datetime
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab7 import lab7

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'секретно-секретный секрет')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')

app.register_blueprint(lab1, url_prefix='/lab1')
app.register_blueprint(lab2, url_prefix='/lab2')
app.register_blueprint(lab3, url_prefix='/lab3')
app.register_blueprint(lab4, url_prefix='/lab4')
app.register_blueprint(lab7, url_prefix='/lab7')

log_journal = []

@app.errorhandler(404)
def not_found(err):
    ip = request.remote_addr
    time_now = datetime.now()
    url = request.url

    log_journal.append({
        "time": time_now,
        "ip": ip,
        "url": url
    })

    journal_items = ""
    for item in log_journal:
        journal_items += (
            f"<li>[{item['time']}] пользователь {item['ip']} "
            f"зашёл на адрес: <a href=\"{item['url']}\">{item['url']}</a></li>"
        )

    img_path = url_for("static", filename="error404.jpg")

    return f"""
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Страница не найдена</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f5f5f5;
                color: #333;
                max-width: 900px;
                margin: 40px auto;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 15px rgba(0,0,0,0.15);
            }}
            h1 {{
                font-size: 42px;
                margin-bottom: 10px;
            }}
            p {{
                font-size: 18px;
                margin-bottom: 10px;
            }}
            img {{
                max-width: 300px;
                height: auto;
                margin: 20px 0;
                display: block;
            }}
            a {{
                color: #0066cc;
                text-decoration: none;
            }}
            a:hover {{
                text-decoration: underline;
            }}
            h2 {{
                margin-top: 30px;
                font-size: 24px;
            }}
            ul.log {{
                list-style-type: disc;
                padding-left: 25px;
                font-size: 14px;
            }}
            ul.log li {{
                margin-bottom: 4px;
            }}
        </style>
    </head>
    <body>
        <h1>404</h1>
        <p>Упс! Такой страницы у нас нет.</p>
        <img src="{img_path}" alt="Страница не найдена">

        <p><b>Ваш IP:</b> {ip}</p>
        <p><b>Дата и время доступа:</b> {time_now}</p>
        <p><a href="/">Перейти на главную страницу</a></p>

        <h2>Журнал</h2>
        <ul class="log">
            {journal_items}
        </ul>
    </body>
</html>
""", 404


@app.route("/")
@app.route("/index")
def index():
    return """
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            <h1>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</h1>
        </header>

        <main>
            <nav>
                <ul>
                    <li><a href="/lab1">Первая лабораторная</a></li>
                    <li><a href="/lab2/">Вторая лабораторная</a></li>
                    <li><a href="/lab3/">Третья лабораторная</a></li>
                    <li><a href="/lab4/">Четвертая лабораторная</a></li>
                    <li><a href="/lab7/">Седьмая лабораторная</a></li>
                </ul>
            </nav>
        </main>

        <footer>
            <p>Генерозов Сергей Евгеньевич, группа ФБИ-33, 3 курс, 2025 год</p>
        </footer>
    </body>
</html>
"""


@app.errorhandler(500)
def internal_error(err):
    return """
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Внутренняя ошибка сервера</title>
    </head>
    <body>
        <h1>Ошибка 500</h1>
        <p>Похоже, произошла какая-то внутренняя ошибка. Компенсации не ждите. Спасибо за внимание.</p>
    </body>
</html>
""", 500
