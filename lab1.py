from flask import Blueprint, url_for, redirect, request
import datetime

lab1 = Blueprint('lab1', __name__)

count = 0

@lab1.route("/")
def lab():
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

        <p><a href="/">На главную</a></p>

        <h2>Список роутов</h2>
        <ul>
            <li><a href="/lab1/web">/lab1/web</a> — Web-страница</li>
            <li><a href="/lab1/author">/lab1/author</a> — Автор</li>
            <li><a href="/lab1/image">/lab1/image</a> — Красивый дуб</li>
            <li><a href="/lab1/counter">/lab1/counter</a> — Счётчик</li>
            <li><a href="/lab1/counter/reset">/lab1/counter/reset</a> — Сброс счётчика</li>
            <li><a href="/lab1/info">/lab1/info</a> — Открыть "Автор" слегка другим способом</li>
            <li><a href="/lab1/created">/lab1/created</a> — Создать что-то</li>
            <li><a href="/lab1/error400">/lab1/error400</a> — Вызвать ошибку 400</li>
            <li><a href="/lab1/error401">/lab1/error401</a> — Вызвать ошибку 401</li>
            <li><a href="/lab1/error402">/lab1/error402</a> — Вызвать ошибку 402</li>
            <li><a href="/lab1/error403">/lab1/error403</a> — Вызвать ошибку 403</li>
            <li><a href="/lab1/error405">/lab1/error405</a> — Вызвать ошибку 405</li>
            <li><a href="/lab1/error418">/lab1/error418</a> — Вызвать ошибку 418</li>
            <li><a href="/lab1/error500">/lab1/error500</a> — Вызвать ошибку 500</li>
        </ul>
    </body>
</html>
"""

@lab1.route("/web")
def web():
    return """<doctype html> 
        <html> 
            <body> 
                <h1>Web-сервер на flask</h1>
                <a href="/lab1/author">author</a>  
            </body> 
        </html>""", 200, {"X-Server": "sample",
        'Content-Type': 'text/plain; charset=utf-8'                  
    }

@lab1.route("/author")
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
                <a href="/lab1/web">web</a> 
            </body> 
        </html>"""


@lab1.route("/image")
def image():
    path = url_for("static", filename="oak.jpg")
    css_path = url_for("static", filename="lab1.css")

    html = f"""
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Изображение дуба</title>
        <link rel="stylesheet" href="{css_path}">
    </head>
    <body>
        <h1>Дуб</h1>
        <img class="oak" src="{path}">
    </body>
</html>
"""

    return html, 200, {
        "Content-Type": "text/html; charset=utf-8",
        "Content-Language": "ru",
        "X-Student": "Generozov-SE",
        "X-Lab": "Lab1"
    }


@lab1.route("/counter")
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
            <p><a href="/lab1/counter/reset">Очистить счётчик</a></p>
    </body>
</html>
'''


@lab1.route("/counter/reset")
def reset_counter():
    global count
    count = 0
    return '''
<!doctype html>
<html>
    <body>
        <h1>Счётчик очищен</h1>
        <p>Значение счётчика сброшено.</p>
        <p><a href="/lab1/counter">Вернуться к счётчику</a></p>
    </body>
</html>
'''


@lab1.route("/info")
def info():
    return redirect("/lab1/author")

@lab1.route("/created")
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


@lab1.route("/error400")
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


@lab1.route("/error401")
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


@lab1.route("/error402")
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


@lab1.route("/error403")
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


@lab1.route("/error405")
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


@lab1.route("/error418")
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


@lab1.route("/error500")
def make_error():
    return 1 / 0