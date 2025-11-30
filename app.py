from flask import Flask, url_for, request, redirect, render_template, abort 
import datetime
app = Flask(__name__)

log_journal = []

@app.errorhandler(404)
def not_found(err):
    ip = request.remote_addr
    time_now = datetime.datetime.now()
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


@app.route("/lab1/error500")
def make_error():
    return 1 / 0


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


@app.route("/lab2/a")
def a():
    return 'ok'


@app.route("/lab2/a/")
def a2():
    return 'ok-ok, very good'

flower_list = [
    {"name": "роза",      "price": 300},
    {"name": "тюльпан",   "price": 310},
    {"name": "незабудка", "price": 320},
    {"name": "ромашка",   "price": 330},
]


@app.route("/lab2/flowers")
def all_flowers():
    """Страница со всеми цветами, с ценами и ссылками на удаление."""
    return render_template("flowers.html", flowers=flower_list)


@app.route("/lab2/flowers/<int:flower_id>")
def flower_detail(flower_id):
    """Страница одного цветка по номеру."""
    if flower_id < 0 or flower_id >= len(flower_list):
        abort(404)

    flower = flower_list[flower_id]
    return render_template(
        "flower_detail.html",
        flower=flower,
        flower_id=flower_id,
        total=len(flower_list)
    )


@app.route("/lab2/add_flower/<name>")
def add_flowers(name):
    """
    Добавление нового цветка по имени (как было в задании).
    Цена для новых задаётся автоматически по простой формуле,
    чтобы были 300, 310, 320, 330, 340 и т.д.
    """
    base_price = 300
    new_price = base_price + len(flower_list) * 10
    flower_list.append({"name": name, "price": new_price})
    return redirect(url_for("all_flowers"))


@app.route("/lab2/add_flower/", methods=["GET"])
def add_flower_no_name():
    """Случай, когда имя цветка не задано вообще."""
    return "вы не задали имя цветка", 400


@app.route("/lab2/add_flower_form", methods=["POST"])
def add_flowers_form():
    """
    Обработчик формы на странице всех цветов.
    Берёт имя из поля, если оно пустое — 400, иначе
    перенаправляет на /lab2/add_flower/<name>.
    """
    name = request.form.get("name", "").strip()
    if not name:
        return "вы не задали имя цветка", 400

    return redirect(url_for("add_flowers", name=name))


@app.route("/lab2/del_flower/<int:flower_id>")
def del_flower(flower_id):
    """
    Удаление одного цветка по номеру.
    Если такого номера нет — 404, если есть — удаляем
    и возвращаемся на список цветов.
    """
    if flower_id < 0 or flower_id >= len(flower_list):
        abort(404)

    del flower_list[flower_id]
    return redirect(url_for("all_flowers"))


@app.route("/lab2/flowers/clear")
def clear_flowers():
    """Полная очистка списка цветов."""
    flower_list.clear()
    return redirect(url_for("all_flowers"))



@app.route("/lab2/example")
def example():
    name = 'Серёжа Генерозов'
    group = 'ФБИ-33'
    course = '3'
    number = '2'
    fruits = [
    {'name': 'яблоки',    'price': 100},
    {'name': 'груши',     'price': 120},
    {'name': 'апельсины', 'price': 80},
    {'name': 'мандарины', 'price': 95},
    {'name': 'манго',     'price': 321}
]
    return render_template('example.html', name=name, group=group, course=course, number=number, fruits=fruits)


@app.route("/lab2/")
def lab2():
    return render_template('lab2.html')


@app.route("/lab2/filters")
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase = phrase)



@app.route("/lab2/calc/<int:a>/<int:b>")
def calc(a, b):
    return render_template("calc.html", a=a, b=b)


@app.route("/lab2/calc/")
def calc_default():
    return redirect(url_for("calc", a=1, b=1))


@app.route("/lab2/calc/<int:a>")
def calc_with_one_param(a):
    return redirect(url_for("calc", a=a, b=1))






books_list = [
    {
        "author": "Джоан Роулинг",
        "title": "Гарри Поттер и философский камень",
        "genre": "Фэнтези",
        "pages": 432
    },
    {
        "author": "Джоан Роулинг",
        "title": "Гарри Поттер и Тайная комната",
        "genre": "Фэнтези",
        "pages": 384
    },
    {
        "author": "Джордж Оруэлл",
        "title": "1984",
        "genre": "Антиутопия",
        "pages": 320
    },
    {
        "author": "Рэй Брэдбери",
        "title": "451 градус по Фаренгейту",
        "genre": "Фантастика",
        "pages": 256
    },
    {
        "author": "Фёдор Достоевский",
        "title": "Преступление и наказание",
        "genre": "Роман",
        "pages": 672
    },
    {
        "author": "Лев Толстой",
        "title": "Война и мир",
        "genre": "Роман-эпопея",
        "pages": 1300
    },
    {
        "author": "Артур Конан Дойл",
        "title": "Собака Баскервилей",
        "genre": "Детектив",
        "pages": 256
    },
    {
        "author": "Жюль Верн",
        "title": "Двадцать тысяч лье под водой",
        "genre": "Приключения",
        "pages": 480
    },
    {
        "author": "Александр Дюма",
        "title": "Граф Монте-Кристо",
        "genre": "Приключения",
        "pages": 1200
    },
    {
        "author": "Стивен Кинг",
        "title": "Зелёная миля",
        "genre": "Мистика",
        "pages": 544
    }
]


@app.route("/lab2/books")
def books():
    return render_template("books.html", books=books_list)



cats_list = [
    {
        "name": "Британская короткошёрстная",
        "image": "/cats/british_shorthair.jpeg",
        "description": "Спокойная, солидная и немного флегматичная кошка с плюшевой шерстью."
    },
    {
        "name": "Сфинкс",
        "image": "cats/sphynx.jpeg",
        "description": "Лысый, очень нежный и любящий тепло кот, который обожает людей."
    },
    {
        "name": "Мейн-кун",
        "image": "cats/maine_coon.jpeg",
        "description": "Крупный и дружелюбный «рысиный» кот с длинной шерстью и кисточками на ушах."
    },
    {
        "name": "Сиамская кошка",
        "image": "cats/siamese.jpeg",
        "description": "Очень разговорчивая, умная и активная кошка с голубыми глазами."
    },
    {
        "name": "Русская голубая",
        "image": "cats/russian_blue.jpeg",
        "description": "Грациозная кошка с серебристо-голубой шерстью и спокойным характером."
    },
    {
        "name": "Персидская кошка",
        "image": "cats/persian.jpeg",
        "description": "Пушистая, немного ленивая аристократка, любящая комфорт и тишину."
    },
    {
        "name": "Бенгальская кошка",
        "image": "cats/bengal.jpeg",
        "description": "Активная кошка с леопардовым окрасом и очень живым характером."
    },
    {
        "name": "Абиссинская кошка",
        "image": "cats/abyssinian.jpeg",
        "description": "Подвижная, любопытная и очень игривая кошка, похожая на маленького пуму."
    },
    {
        "name": "Скоттиш-фолд",
        "image": "cats/scottish_fold.jpeg",
        "description": "Кошка с забавно загнутыми ушами и мягким, дружелюбным нравом."
    },
    {
        "name": "Ориентальная кошка",
        "image": "cats/oriental.jpeg",
        "description": "Очень стройная, изящная и разговорчивая кошка с большими ушами."
    },
    {
        "name": "Рэгдолл",
        "image": "cats/ragdoll.jpeg",
        "description": "Кошка, которая расслабляется на руках как тряпичная кукла, очень ласковая."
    },
    {
        "name": "Невская маскарадная",
        "image": "cats/neva.jpeg",
        "description": "Пушистая кошка с «маской» на мордочке и яркими голубыми глазами."
    },
    {
        "name": "Сибирская кошка",
        "image": "cats/siberian.jpeg",
        "description": "Крупная, выносливая и независимая кошка с густой шерстью."
    },
    {
        "name": "Манчкин",
        "image": "cats/munchkin.jpeg",
        "description": "Кот с короткими лапками, выглядит как такса в кошачьем мире."
    },
    {
        "name": "Шотландская прямоухая",
        "image": "cats/scottish_straight.jpeg",
        "description": "Спокойная, уравновешенная кошка с классическими ушками и круглой мордочкой."
    },
    {
        "name": "Домашняя дворовая кошка",
        "image": "cats/domestic.jpeg",
        "description": "Самая универсальная порода: умная, выносливая, бывает любой внешности."
    },
    {
        "name": "Турецкая ангорская",
        "image": "cats/turkish_angora.jpeg",
        "description": "Изящная, часто белая кошка с длинной шерстью и живым темпераментом."
    },
    {
        "name": "Корат",
        "image": "cats/korat.jpeg",
        "description": "Редкая кошка с серебристо-голубой шерстью и зелёными глазами, символ удачи в Таиланде."
    },
    {
        "name": "Бурманская кошка",
        "image": "cats/burmese.jpeg",
        "description": "Очень общительная, ориентированная на человека кошка с мягкой шерстью."
    },
    {
        "name": "Американская короткошёрстная",
        "image": "cats/american_shorthair.jpeg",
        "description": "Неприхотливая, крепкая и дружелюбная кошка, хорошо ладит с людьми и детьми."
    }
]



@app.route("/lab2/cats")
def cats():
    return render_template("cats.html", cats=cats_list)

