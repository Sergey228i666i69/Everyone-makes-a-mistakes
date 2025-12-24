from flask import Blueprint, render_template, request, jsonify

lab7 = Blueprint('lab7', __name__)

films = [
    # ... список фильмов
]

@lab7.route('/lab7')
def lab():
    return render_template('lab7/index.html')

@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    return jsonify(films)

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    if id < 0 or id >= len(films):
        return '', 404
    return films[id]

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id):
    if id < 0 or id >= len(films):
        return '', 404
    del films[id]
    return '', 204

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_film(id):
    film = request.get_json()
    
    if (not film.get('title') or film['title'].strip() == '') and film.get('title_ru'):
        film['title'] = film['title_ru']
    
    required_fields = ['title_ru', 'year', 'description']
    for field in required_fields:
        if field not in film or not str(film[field]).strip():
            return {field: 'Это поле обязательно для заполнения'}, 400
    
    if id < 0 or id >= len(films):
        return '', 404
    
    films[id] = film
    return films[id]

@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_film():
    data = request.get_json()
    
    if not data:
        return '', 400
    
    if (not data.get('title') or data['title'].strip() == '') and data.get('title_ru'):
        data['title'] = data['title_ru']
    
    required_fields = ['title_ru', 'year', 'description']
    for field in required_fields:
        if field not in data or not str(data[field]).strip():
            return {field: 'Это поле обязательно для заполнения'}, 400
    
    try:
        year = int(data['year'])
        if year < 1888 or year > 2100:
            return {'year': 'Некорректный год выпуска'}, 400
    except ValueError:
        return {'year': 'Год должен быть числом'}, 400
    
    new_film = {
        'title': data.get('title', ''),
        'title_ru': data['title_ru'],
        'year': year,
        'description': data['description']
    }
    
    films.append(new_film)
    return str(len(films) - 1), 201