from flask import Blueprint, render_template, request, redirect, url_for, abort

lab2 = Blueprint('lab2', __name__)

# Списки данных для лабораторной
flower_list = [
    {"name": "роза",      "price": 300},
    {"name": "тюльпан",   "price": 310},
    {"name": "незабудка", "price": 320},
    {"name": "ромашка",   "price": 330},
]

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

cats_list = [
    {
        "name": "Британская короткошёрстная",
        "image": "/static/cats/british_shorthair.jpeg",  # Абсолютный путь
        "description": "Спокойная, солидная и немного флегматичная кошка с плюшевой шерстью."
    },
    {
        "name": "Сфинкс",
        "image": "/static/cats/sphynx.jpeg",
        "description": "Лысый, очень нежный и любящий тепло кот, который обожает людей."
    },
    {
        "name": "Мейн-кун",
        "image": "/static/cats/maine_coon.jpeg",
        "description": "Крупный и дружелюбный «рысиный» кот с длинной шерстью и кисточками на ушах."
    },
    {
        "name": "Сиамская кошка",
        "image": "/static/cats/siamese.jpeg",
        "description": "Очень разговорчивая, умная и активная кошка с голубыми глазами."
    },
    {
        "name": "Русская голубая",
        "image": "/static/cats/russian_blue.jpeg",
        "description": "Грациозная кошка с серебристо-голубой шерстью и спокойным характером."
    },
    {
        "name": "Персидская кошка",
        "image": "/static/cats/persian.jpeg",
        "description": "Пушистая, немного ленивая аристократка, любящая комфорт и тишину."
    },
    {
        "name": "Бенгальская кошка",
        "image": "/static/cats/bengal.jpeg",
        "description": "Активная кошка с леопардовым окрасом и очень живым характером."
    },
    {
        "name": "Абиссинская кошка",
        "image": "/static/cats/abyssinian.jpeg",
        "description": "Подвижная, любопытная и очень игривая кошка, похожая на маленького пуму."
    },
    {
        "name": "Скоттиш-фолд",
        "image": "/static/cats/scottish_fold.jpeg",
        "description": "Кошка с забавно загнутыми ушами и мягким, дружелюбным нравом."
    },
    {
        "name": "Ориентальная кошка",
        "image": "/static/cats/oriental.jpeg",
        "description": "Очень стройная, изящная и разговорчивая кошка с большими ушами."
    },
    {
        "name": "Рэгдолл",
        "image": "/static/cats/ragdoll.jpeg",
        "description": "Кошка, которая расслабляется на руках как тряпичная кукла, очень ласковая."
    },
    {
        "name": "Невская маскарадная",
        "image": "/static/cats/neva.jpeg",
        "description": "Пушистая кошка с «маской» на мордочке и яркими голубыми глазами."
    },
    {
        "name": "Сибирская кошка",
        "image": "/static/cats/siberian.jpeg",
        "description": "Крупная, выносливая и независимая кошка с густой шерстью."
    },
    {
        "name": "Манчкин",
        "image": "/static/cats/munchkin.jpeg",
        "description": "Кот с короткими лапками, выглядит как такса в кошачьем мире."
    },
    {
        "name": "Шотландская прямоухая",
        "image": "/static/cats/scottish_straight.jpeg",
        "description": "Спокойная, уравновешенная кошка с классическими ушками и круглой мордочкой."
    },
    {
        "name": "Домашняя дворовая кошка",
        "image": "/static/cats/domestic.jpeg",
        "description": "Самая универсальная порода: умная, выносливая, бывает любой внешности."
    },
    {
        "name": "Турецкая ангорская",
        "image": "/static/cats/turkish_angora.jpeg",
        "description": "Изящная, часто белая кошка с длинной шерстью и живым темпераментом."
    },
    {
        "name": "Корат",
        "image": "/static/cats/korat.jpeg",
        "description": "Редкая кошка с серебристо-голубой шерстью и зелёными глазами, символ удачи в Таиланде."
    },
    {
        "name": "Бурманская кошка",
        "image": "/static/cats/burmese.jpeg",
        "description": "Очень общительная, ориентированная на человека кошка с мягкой шерстью."
    },
    {
        "name": "Американская короткошёрстная",
        "image": "/static/cats/american_shorthair.jpeg",
        "description": "Неприхотливая, крепкая и дружелюбная кошка, хорошо ладит с людьми и детьми."
    }
]

# Основные маршруты
@lab2.route("/")
def lab():
    return render_template('lab2/lab2.html')

@lab2.route("/a")
def a():
    return 'ok'

@lab2.route("/a/")
def a2():
    return 'ok-ok, very good'

@lab2.route("/example")
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
    return render_template('lab2/example.html', name=name, group=group, course=course, number=number, fruits=fruits)

@lab2.route("/filters")
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('lab2/filter.html', phrase=phrase)

@lab2.route("/calc/<int:a>/<int:b>")
def calc(a, b):
    return render_template("lab2/calc.html", a=a, b=b)

@lab2.route("/calc/")
def calc_default():
    return redirect(url_for("lab2.calc", a=1, b=1))

@lab2.route("/calc/<int:a>")
def calc_with_one_param(a):
    return redirect(url_for("lab2.calc", a=a, b=1))

# Маршруты для цветов
@lab2.route("/flowers")
def all_flowers():
    """Страница со всеми цветами, с ценами и ссылками на удаление."""
    return render_template("lab2/flowers.html", flowers=flower_list)

@lab2.route("/flowers/<int:flower_id>")
def flower_detail(flower_id):
    """Страница одного цветка по номеру."""
    if flower_id < 0 or flower_id >= len(flower_list):
        abort(404)

    flower = flower_list[flower_id]
    return render_template(
        "lab2/flower_detail.html",
        flower=flower,
        flower_id=flower_id,
        total=len(flower_list)
    )

@lab2.route("/add_flower/<name>")
def add_flowers(name):
    """
    Добавление нового цветка по имени (как было в задании).
    Цена для новых задаётся автоматически по простой формуле,
    чтобы были 300, 310, 320, 330, 340 и т.д.
    """
    base_price = 300
    new_price = base_price + len(flower_list) * 10
    flower_list.append({"name": name, "price": new_price})
    return redirect(url_for("lab2.all_flowers"))

@lab2.route("/add_flower/", methods=["GET"])
def add_flower_no_name():
    """Случай, когда имя цветка не задано вообще."""
    return "вы не задали имя цветка", 400

@lab2.route("/add_flower_form", methods=["POST"])
def add_flowers_form():
    """
    Обработчик формы на странице всех цветов.
    Берёт имя из поля, если оно пустое — 400, иначе
    перенаправляет на /lab2/add_flower/<name>.
    """
    name = request.form.get("name", "").strip()
    if not name:
        return "вы не задали имя цветка", 400

    return redirect(url_for("lab2.add_flowers", name=name))

@lab2.route("/del_flower/<int:flower_id>")
def del_flower(flower_id):
    """
    Удаление одного цветка по номеру.
    Если такого номера нет — 404, если есть — удаляем
    и возвращаемся на список цветов.
    """
    if flower_id < 0 or flower_id >= len(flower_list):
        abort(404)

    del flower_list[flower_id]
    return redirect(url_for("lab2.all_flowers"))

@lab2.route("/flowers/clear")
def clear_flowers():
    """Полная очистка списка цветов."""
    flower_list.clear()
    return redirect(url_for("lab2.all_flowers"))

# Маршруты для книг
@lab2.route("/books")
def books():
    return render_template("lab2/books.html", books=books_list)

# Маршруты для котов
@lab2.route("/cats")
def cats():
    return render_template("lab2/cats.html", cats=cats_list)