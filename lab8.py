from flask import Blueprint, render_template

lab8 = Blueprint('lab8', __name__)


@lab8.route('/')
def index():
    return render_template('lab8/index.html')
