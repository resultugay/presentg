from flask.blueprints import Blueprint
from flask.templating import render_template
from flask_login import current_user, login_required, login_user, logout_user
from datetime import datetime
from Group import get_group2
from Group import Group
from Group_member import get_groups
from Group import get_group_using_group_id

home = Blueprint('home',__name__)

@home.route('/')
def home_page():
    if current_user.is_authenticated:
        gr = get_groups(current_user.get_user_id())      
        gr_names = []
        for g in gr:
            gr_names.append(get_group_using_group_id(g.group_id))
        return render_template("home.html",groups=gr_names)
    else:
        return render_template("home.html")



@home.route('/test')
@login_required
def test_page():
    return render_template("home.html")
