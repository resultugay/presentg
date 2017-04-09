from flask.blueprints import Blueprint
from flask.templating import render_template
from flask import flash
from forms import LoginForm
from User import get_user
from passlib import hash
from flask_login import login_user
from flask import current_app, request,redirect
from flask import Blueprint, abort, flash, redirect, render_template, url_for
from wtforms.validators import Email, InputRequired, ValidationError



sign_in = Blueprint('sign_in',__name__)

@sign_in.route('/signin',methods=['GET','POST'])
def sign_in_page():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.data['email']
        password = form.data['password']
        user = get_user(username)   
        if user is not None:
            if hash.sha512_crypt.verify(password,user.password):
                login_user(user)
                flash('You have logged in.')
                next_page = request.args.get('next', url_for('home.home_page'))
                return redirect(next_page)
        flash('Invalid Credentials')    
        
    return render_template("sign_in.html",form = form)
