from flask.blueprints import Blueprint
from flask.templating import render_template
from flask import current_app, request
from passlib.apps import custom_app_context as pwd_context
from passlib import hash
import bcrypt
import random


sign_up = Blueprint('sign_up',__name__)
ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


@sign_up.route('/sign_up', methods=['GET', 'POST'])
def sign_up_page():
    if request.method == 'GET':
        return render_template("sign_up.html")
    else:
        username = request.form['reg_username']
        password = request.form['reg_password']
        #for the salt create 16 character long salt and use it for hash
        salt = ""
        for i in range(16):
            salt = salt + (random.choice(ALPHABET))                
        hashed_password = hash.sha512_crypt.using(salt=salt).hash(password)        
        #k = hash.sha512_crypt.verify(password, hashed_password) for verifying hash        
        email    =  request.form['reg_email']
        firstname =  request.form['reg_firstname']
        surname =  request.form['reg_surname']   
        gender = request.form['reg_gender']
        
        return render_template("home.html")
