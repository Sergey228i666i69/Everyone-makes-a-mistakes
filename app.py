from flask import Flask, url_for, request, redirect
import datetime
app = Flask(__name__)

@app.route("/web")
def web():
    return """<doctype html> 
        <html> 
            <body> 
                <h1>Web-сервер на flask</h1>
                <a href="/author">author</a>  
            </body> 
        </html>"""

@app.route("/author")
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


@app.route("/image")
def image():
    path = url_for("static", filename="oak.jpg")
    return '''
<!doctype html>
<html>
    <body>
        <h1>Дуб</h1>
        <image src="''' + path + '''">
    </body>
</html>
'''

count = 0

@app.route("/counter")
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
    </body>
</html>
'''

@app.route("/info")
def info():
    return redirect("/author")

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



