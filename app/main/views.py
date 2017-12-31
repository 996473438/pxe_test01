from flask import request, render_template
from . import main
from app.models import User


@main.route('/test', methods=['GET', 'POST'])
def test():
    user = User(username='liuxin', password='123456').this_query()
    return user.this_note()
