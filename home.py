from flask.blueprints import Blueprint
from flask.templating import render_template
from flask_login import current_user, login_required, login_user, logout_user
from datetime import datetime
from Group import get_group2
from Group import Group

home = Blueprint('home',__name__)

@home.route('/')
def home_page():
    if current_user.is_authenticated:
        gr = get_group2("First")
        return render_template("home.html",groups=gr)
    else:
        return render_template("home.html")



@home.route('/test')
@login_required
def test_page():
    return render_template("home.html")
