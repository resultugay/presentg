from flask.blueprints import Blueprint
from flask.templating import render_template
from flask_login import current_user, login_required, login_user, logout_user


home = Blueprint('home',__name__)

@home.route('/')
def home_page():
    return render_template("home.html")


@home.route('/test')
@login_required
def test_page():
    return render_template("home.html")
