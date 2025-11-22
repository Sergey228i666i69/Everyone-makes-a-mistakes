from flask import Flask, url_for, request, redirect
import datetime
app = Flask(__name__)


@app.errorhandler(404)
def not_found(err):
    return "Да нету такой страницы!", 404


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
                </ul>
            </nav>
        </main>

        <footer>
            <p>Генерозов Сергей Евгеньевич, группа ФБИ-33, 3 курс, 2025 год</p>
        </footer>
    </body>
</html>
"""


@app.route("/lab1")
def lab1():
    return """
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Лабораторная 1</title>
    </head>
    <body>
        <p>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые ба-
            зовые возможности.
        </p>

        <p><a href="/">Список работ</a></p>
    </body>
</html>
"""


@app.route("/lab1/web")
def web():
    return """<doctype html> 
        <html> 
            <body> 
                <h1>Web-сервер на flask</h1>
                <a href="/author">author</a>  
            </body> 
        </html>""", 200, {"X-Server": "sample",
        'Content-Type': 'text/plain; charset=utf-8'                  
    }

@app.route("/lab1/author")
def author():
    name = "Генерозов Сергей Евгеньевич"
    group = "ФБИ-33"
    faculty = "ФБ"

    return """
        <html> 
            <body> 
                <p>Студент: """ + name + """</p>
                <p>Группа: """ + group + """</p>
                <p>Факультет: """ + faculty + """</p>
                <a href="/web">web</a> 
            </body> 
        </html>"""


@app.route("/lab1/image")
def image():
    path = url_for("static", filename="oak.jpg")
    css_path = url_for("static", filename="lab1.css")
    return f"""
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="{css_path}">
    </head>
    <body>
        <h1>Дуб</h1>
        <img class="oak" src="{path}">
    </body>
</html>
"""

count = 0

@app.route("/lab1/counter")
def counter():
    global count
    count += 1
    
    time = datetime.datetime.today()
    url = request.url
    client_ip = request.remote_addr

    return '''
<!doctype html>
<html>
    <body>
        <h1>Счётчик</h1>
            <p>Внимание! Вас поставили на счётчик! Вы должны создателю страницы ''' + str(count) + ''' миллионов рублей</p>
            <p>Дата и время: ''' + str(time) + '''</p>
            <p>Запрошенный адрес: ''' + str(url) + '''</p>
            <p>Ваш IP-адрес: ''' + str(client_ip) + '''</p>
            <p><a href="/counter/reset">Очистить счётчик</a></p>
    </body>
</html>
'''


@app.route("/lab1/counter/reset")
def reset_counter():
    global count
    count = 0
    return '''
<!doctype html>
<html>
    <body>
        <h1>Счётчик очищен</h1>
        <p>Значение счётчика сброшено.</p>
        <p><a href="/counter">Вернуться к счётчику</a></p>
    </body>
</html>
'''


@app.route("/lab1/info")
def info():
    return redirect("/lab1/author")

@app.route("/lab1/created")
def created():
    return '''
<!doctype html>
<html>
    <body>
        <h1>Создано успешно</h1>
            <div><i>Что-то создано...</i></div>
    </body>
</html>
''', 201


@app.route("/lab1/error400")
def error_400():
    return """
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>400 Bad Request</title>
    </head>
    <body>
        <h1>400 Bad Request</h1>
        <p>Ошибка 400. Неверный запрос.</p>
    </body>
</html>
""", 400


@app.route("/lab1/error401")
def error_401():
    return """
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>401 Unauthorized</title>
    </head>
    <body>
        <h1>401 Unauthorized</h1>
        <p>Ошибка 401. Требуется аутентификация.</p>
    </body>
</html>
""", 401


@app.route("/lab1/error402")
def error_402():
    return """
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>402 Payment Required</title>
    </head>
    <body>
        <h1>402 Payment Required</h1>
        <p>Ошибка 402. Требуется оплата.</p>
    </body>
</html>
""", 402


@app.route("/lab1/error403")
def error_403():
    return """
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>403 Forbidden</title>
    </head>
    <body>
        <h1>403 Forbidden</h1>
        <p>Ошибка 403. Доступ к ресурсу запрещён.</p>
    </body>
</html>
""", 403


@app.route("/lab1/error405")
def error_405():
    return """
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>405 Method Not Allowed</title>
    </head>
    <body>
        <h1>405 Method Not Allowed</h1>
        <p>Ошибка 405. HTTP-метод не допускается для этого ресурса.</p>
    </body>
</html>
""", 405


@app.route("/lab1/error418")
def error_418():
    return """
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>418 I'm a teapot</title>
    </head>
    <body>
        <h1>418 I'm a teapot</h1>
        <p>Ошибка 418. Я — чайник.</p>
    </body>
</html>
""", 418

