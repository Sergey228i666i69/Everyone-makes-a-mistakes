from flask import Blueprint, render_template, request, make_response, redirect

lab3 = Blueprint('lab3', __name__)

@lab3.route('/')
def lab():
    name = request.cookies.get('name')
    name_color = request.cookies.get('name_color')
    return render_template('lab3/lab3.html', name=name, name_color=name_color)

@lab3.route('/cookie')
def cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'magenta')
    return resp

@lab3.route('/del_cookie')
def del_cookie():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp

@lab3.route('/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните имя!'
    er_age = {}
    age = request.args.get('age')
    if age == '':
        er_age['age'] = 'Заполните возраст!'
    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user=user, age=age, sex=sex, errors=errors, er_age=er_age)

@lab3.route('/order')
def order():
    return render_template('/lab3/order.html')

@lab3.route('/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70
    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10
    return render_template('lab3/pay.html', price=price)

@lab3.route('/payment')
def payment():
    price = request.args.get('price')
    return render_template('lab3/payment.html', price=price)

@lab3.route('/settings')
def settings():
    # Получаем параметры из формы (GET-запроса)
    color = request.args.get('color')
    bg_color = request.args.get('bg_color')
    font_size = request.args.get('font_size')
    
    # Если параметры переданы (форма отправлена)
    if color or bg_color or font_size:
        # Создаем ответ с перенаправлением
        resp = make_response(redirect('/lab3/settings'))
        
        # Устанавливаем cookies с переданными значениями
        if color:
            resp.set_cookie('color', color)
        if bg_color:
            resp.set_cookie('bg_color', bg_color)
        if font_size:
            resp.set_cookie('font_size', font_size)
        
        return resp
    
    # Если параметры не переданы, читаем из cookies или используем значения по умолчанию
    color = request.cookies.get('color', '#000000')
    bg_color = request.cookies.get('bg_color', '#ffffff')
    font_size = request.cookies.get('font_size', '16')
    
    # Отображаем шаблон с текущими значениями
    return render_template('lab3/settings.html', 
                         color=color, 
                         bg_color=bg_color, 
                         font_size=font_size)

@lab3.route('/ticket')
def ticket():
    errors = {}
    
    fio = request.args.get('fio')
    shelf = request.args.get('shelf')
    linen = request.args.get('linen') == 'on'
    luggage = request.args.get('luggage') == 'on'
    age_str = request.args.get('age')
    departure = request.args.get('departure')
    destination = request.args.get('destination')
    travel_date = request.args.get('travel_date')
    insurance = request.args.get('insurance') == 'on'
    
    form_submitted = any([fio, shelf, age_str, departure, destination, travel_date])
    
    if form_submitted:
        if not fio:
            errors['fio'] = 'Заполните ФИО пассажира'
        if not shelf:
            errors['shelf'] = 'Выберите полку'
        if not age_str:
            errors['age'] = 'Заполните возраст'
        elif not age_str.isdigit() or not (1 <= int(age_str) <= 120):
            errors['age'] = 'Возраст должен быть от 1 до 120 лет'
        if not departure:
            errors['departure'] = 'Заполните пункт выезда'
        if not destination:
            errors['destination'] = 'Заполните пункт назначения'
        if not travel_date:
            errors['travel_date'] = 'Выберите дату поездки'
        
        if errors:
            return render_template('lab3/ticket.html', 
                                 errors=errors,
                                 fio=fio,
                                 shelf=shelf,
                                 linen=linen,
                                 luggage=luggage,
                                 age=age_str,
                                 departure=departure,
                                 destination=destination,
                                 travel_date=travel_date,
                                 insurance=insurance,
                                 show_result=False)
        
        age = int(age_str)
        if age < 18:
            price = 700
        else:
            price = 1000
        
        if shelf in ['lower', 'side_lower']:
            price += 100
        if linen:
            price += 75
        if luggage:
            price += 250
        if insurance:
            price += 150
        
        return render_template('lab3/ticket.html',
                             fio=fio,
                             shelf=shelf,
                             linen=linen,
                             luggage=luggage,
                             age=age,
                             departure=departure,
                             destination=destination,
                             travel_date=travel_date,
                             insurance=insurance,
                             price=price,
                             show_result=True)
    
    return render_template('lab3/ticket.html', show_result=False)

@lab3.route('/clear_settings')
def clear_settings():
    resp = make_response(redirect('/lab3/settings'))
    resp.delete_cookie('color')
    resp.delete_cookie('bg_color') 
    resp.delete_cookie('font_size')
    return resp

# Список произведений классической русской литературы
russian_classics = [
    {"title": "Евгений Онегин", "price": 1500, "year": 1833, "author": "Александр Пушкин"},
    {"title": "Война и мир", "price": 1800, "year": 1869, "author": "Лев Толстой"},
    {"title": "Преступление и наказание", "price": 1200, "year": 1866, "author": "Фёдор Достоевский"},
    {"title": "Отцы и дети", "price": 1400, "year": 1862, "author": "Иван Тургенев"},
    {"title": "Герой нашего времени", "price": 1100, "year": 1840, "author": "Михаил Лермонтов"},
    {"title": "Мёртвые души", "price": 950, "year": 1842, "author": "Николай Гоголь"},
    {"title": "Анна Каренина", "price": 850, "year": 1877, "author": "Лев Толстой"},
    {"title": "Обломов", "price": 1000, "year": 1859, "author": "Иван Гончаров"},
    {"title": "Братья Карамазовы", "price": 1300, "year": 1880, "author": "Фёдор Достоевский"},
    {"title": "Горе от ума", "price": 900, "year": 1825, "author": "Александр Грибоедов"},
    {"title": "Идиот", "price": 1600, "year": 1869, "author": "Фёдор Достоевский"},
    {"title": "Капитанская дочка", "price": 1250, "year": 1836, "author": "Александр Пушкин"},
    {"title": "Ревизор", "price": 1150, "year": 1836, "author": "Николай Гоголь"},
    {"title": "Бесы", "price": 1350, "year": 1872, "author": "Фёдор Достоевский"},
    {"title": "Дворянское гнездо", "price": 1050, "year": 1859, "author": "Иван Тургенев"},
    {"title": "Борис Годунов", "price": 1450, "year": 1825, "author": "Александр Пушкин"},
    {"title": "Рудин", "price": 950, "year": 1856, "author": "Иван Тургенев"},
    {"title": "Шинель", "price": 800, "year": 1842, "author": "Николай Гоголь"},
    {"title": "Воскресение", "price": 750, "year": 1899, "author": "Лев Толстой"},
    {"title": "Невский проспект", "price": 1700, "year": 1835, "author": "Николай Гоголь"},
    {"title": "Станционный смотритель", "price": 1550, "year": 1831, "author": "Александр Пушкин"},
    {"title": "Бесприданница", "price": 1100, "year": 1879, "author": "Александр Островский"},
    {"title": "Гроза", "price": 1200, "year": 1860, "author": "Александр Островский"}
]

@lab3.route('/literature')
def literature():
    min_price_cookie = request.cookies.get('min_price', '')
    max_price_cookie = request.cookies.get('max_price', '')
    
    min_price_arg = request.args.get('min_price', min_price_cookie)
    max_price_arg = request.args.get('max_price', max_price_cookie)
    reset = request.args.get('reset')
    
    if reset:
        resp = make_response(redirect('/lab3/literature'))
        resp.delete_cookie('min_price')
        resp.delete_cookie('max_price')
        return resp
    
    min_price_all = min(book['price'] for book in russian_classics)
    max_price_all = max(book['price'] for book in russian_classics)
    
    filtered_books = russian_classics
    message = ""
    
    if min_price_arg or max_price_arg:
        try:
            min_price = int(min_price_arg) if min_price_arg else min_price_all
            max_price = int(max_price_arg) if max_price_arg else max_price_all
            
            if min_price > max_price:
                min_price, max_price = max_price, min_price
            
            filtered_books = [
                book for book in russian_classics
                if min_price <= book['price'] <= max_price
            ]
            
            count = len(filtered_books)
            if count == 0:
                message = "Не найдено ни одной книги в заданном диапазоне цен"
            else:
                message = f"Найдено книг: {count}"
                
            if min_price_arg or max_price_arg:
                resp = make_response(render_template('lab3/literature.html',
                    books=filtered_books,
                    min_price=min_price,
                    max_price=max_price,
                    min_price_all=min_price_all,
                    max_price_all=max_price_all,
                    message=message
                ))
                if min_price_arg:
                    resp.set_cookie('min_price', min_price_arg)
                if max_price_arg:
                    resp.set_cookie('max_price', max_price_arg)
                return resp
                
        except ValueError:
            message = "Ошибка: введите корректные числовые значения"
    
    return render_template('lab3/literature.html',
        books=filtered_books,
        min_price=min_price_arg,
        max_price=max_price_arg,
        min_price_all=min_price_all,
        max_price_all=max_price_all,
        message=message or f"Всего книг: {len(filtered_books)}"
    )