from flask.blueprints import Blueprint
from flask.templating import render_template


sign_in = Blueprint('sign_in',__name__)

@sign_in.route('/')
def home_page():
    return render_template("sign_in.html")
