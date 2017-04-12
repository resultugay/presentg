from flask_login import logout_user
from flask import Blueprint, flash, redirect, url_for

log_out = Blueprint('log_out',__name__)

@log_out.route('/logout')
def log_out_page():
    logout_user()
    flash('You have logged out.')
    return redirect(url_for('home.home_page'))
