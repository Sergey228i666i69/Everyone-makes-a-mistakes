import os

from flask import Blueprint, render_template, request, jsonify, session, current_app, url_for
from flask_login import current_user

lab9 = Blueprint('lab9', __name__)

GIFT_LIMIT = 3
SURPRISE_IMAGE_PREFIX = 'surprice_'
SPECIAL_GIFT_IDS = {8, 9, 10}

GIFTS = [
    {
        'id': 1,
        'content': {
            'text': 'Пусть новый год принесет море вдохновения и ярких идей!',
            'image': 'item_1'
        },
        'is_taken': False
    },
    {
        'id': 2,
        'content': {
            'text': 'Пусть каждый день будет наполнен радостью и добром!',
            'image': 'item_2'
        },
        'is_taken': False
    },
    {
        'id': 3,
        'content': {
            'text': 'Желаю уверенности, силы и побед во всем, за что берешься!',
            'image': 'item_3'
        },
        'is_taken': False
    },
    {
        'id': 4,
        'content': {
            'text': 'Пусть праздничное настроение остается с тобой весь год!',
            'image': 'item_4'
        },
        'is_taken': False
    },
    {
        'id': 5,
        'content': {
            'text': 'Пусть в доме будет уют, а в сердце — спокойствие.',
            'image': 'item_5'
        },
        'is_taken': False
    },
    {
        'id': 6,
        'content': {
            'text': 'Желаю тепла, улыбок и приятных сюрпризов!',
            'image': 'item_6'
        },
        'is_taken': False
    },
    {
        'id': 7,
        'content': {
            'text': 'Пусть Новый год подарит тебе новые возможности!',
            'image': 'item_7'
        },
        'is_taken': False
    },
    {
        'id': 8,
        'content': {
            'text': 'Желаю невероятных открытий и вдохновляющих встреч.',
            'image': 'item_8'
        },
        'is_taken': False
    },
    {
        'id': 9,
        'content': {
            'text': 'Пусть удача будет твоим постоянным спутником!',
            'image': 'item_9'
        },
        'is_taken': False
    },
    {
        'id': 10,
        'content': {
            'text': 'Желаю счастья, здоровья и исполнения заветных желаний!',
            'image': 'item_10'
        },
        'is_taken': False
    }
]

GIFT_POSITIONS = {
    1: {'top': 40, 'left': 60},
    2: {'top': 70, 'left': 320},
    3: {'top': 120, 'left': 560},
    4: {'top': 200, 'left': 140},
    5: {'top': 230, 'left': 420},
    6: {'top': 280, 'left': 680},
    7: {'top': 360, 'left': 80},
    8: {'top': 390, 'left': 360},
    9: {'top': 430, 'left': 600},
    10: {'top': 480, 'left': 250}
}


@lab9.route('/')
def index():
    remaining_count = sum(1 for gift in GIFTS if not gift['is_taken'])
    surprise_images = {
        gift['id']: _resolve_image(f"{SURPRISE_IMAGE_PREFIX}{gift['id']}")
        for gift in GIFTS
    }

    return render_template(
        'lab9/index.html',
        gifts=GIFTS,
        remaining_count=remaining_count,
        gift_positions=GIFT_POSITIONS,
        surprise_images=surprise_images,
        special_gift_ids=SPECIAL_GIFT_IDS
    )


@lab9.route('/get-gift', methods=['POST'])
def get_gift():
    data = request.get_json(silent=True) or {}
    gift_id = data.get('id')
    try:
        gift_id = int(gift_id)
    except (TypeError, ValueError):
        return jsonify(result='error', message='Некорректный идентификатор подарка.'), 400

    gift = next((item for item in GIFTS if item['id'] == gift_id), None)
    if not gift:
        return jsonify(result='error', message='Подарок не найден.'), 404

    if gift['is_taken']:
        return jsonify(result='error', message='Этот подарок уже открыт.', is_taken=True), 409

    if gift_id in SPECIAL_GIFT_IDS and not current_user.is_authenticated:
        return jsonify(
            result='error',
            message='Этот подарок доступен только авторизованным пользователям.'
        ), 403

    opened_count = session.get('saved_gift_count', 0)
    if opened_count >= GIFT_LIMIT:
        return jsonify(result='error', message='Можно открыть не более 3-х подарков.'), 403

    gift['is_taken'] = True
    session['saved_gift_count'] = opened_count + 1

    remaining_count = sum(1 for item in GIFTS if not item['is_taken'])
    image_filename = _resolve_image(gift['content']['image'])

    return jsonify(
        result='success',
        text=gift['content']['text'],
        image_url=url_for('static', filename=f'lab9/{image_filename}'),
        is_taken=True,
        remaining_count=remaining_count
    )


@lab9.route('/reset', methods=['POST'])
def reset_gifts():
    if not current_user.is_authenticated:
        return jsonify(result='error', message='Недостаточно прав доступа.'), 403

    for gift in GIFTS:
        gift['is_taken'] = False

    session['saved_gift_count'] = 0

    remaining_count = sum(1 for gift in GIFTS if not gift['is_taken'])
    return jsonify(result='success', remaining_count=remaining_count)


def _resolve_image(base_name):
    static_dir = os.path.join(current_app.root_path, 'static', 'lab9')
    base_lower = base_name.lower()
    try:
        for filename in os.listdir(static_dir):
            name, _ext = os.path.splitext(filename)
            if name.lower() == base_lower:
                return filename
    except FileNotFoundError:
        return f'{base_name}.png'

    return f'{base_name}.png'
