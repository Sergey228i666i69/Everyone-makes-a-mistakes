from flask import Flask
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
