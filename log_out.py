from flask.blueprints import Blueprint
from flask.templating import render_template
from flask import flash
from forms import LoginForm
from User import get_user
from passlib import hash
from flask_login import logout_user
from flask import current_app, request,redirect
from flask import Blueprint, abort, flash, redirect, render_template, url_for
from User import get_user
from flask_login.utils import current_user

log_out = Blueprint('log_out',__name__)

@log_out.route('/logout')
def log_out_page():
    logout_user()
    flash('You have logged out.')
    return redirect(url_for('home.home_page'))
