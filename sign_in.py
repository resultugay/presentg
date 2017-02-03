from flask.blueprints import Blueprint
from flask.templating import render_template
from flask import flash
from forms import LoginForm
from user import get_user
from passlib import hash
from flask_login import login_user
from flask import current_app, request,redirect
from flask import Blueprint, abort, flash, redirect, render_template, url_for


sign_in = Blueprint('sign_in',__name__)

@sign_in.route('/signin',methods=['GET','POST'])
def sign_in_page():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.data['username']
        password = form.data['password']
        print(password)
        user = get_user(username)
        if user is not None:
            if hash.sha512_crypt.verify(password,user.password):
                login_user(user)
                flash('You have logged in.')
                next_page = request.args.get('next', url_for('home.home_page'))
                return redirect(next_page)
        flash('invalid')            
    return render_template("sign_in.html",form = form)
