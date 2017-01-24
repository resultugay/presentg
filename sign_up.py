from flask.blueprints import Blueprint
from flask.templating import render_template


sign_up = Blueprint('sign_up',__name__)

@sign_up.route('/sign_up')
def sign_up_page():
    return render_template("sign_up.html")


