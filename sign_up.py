from flask.blueprints import Blueprint
from flask.templating import render_template
from flask import current_app, request
from passlib.apps import custom_app_context as pwd_context
from passlib import hash
import bcrypt
import random
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ctypes.wintypes import BOOLEAN
from sqlalchemy.sql.sqltypes import BINARY

Base = declarative_base()    

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(40), nullable=False)
    email = Column(String(40), nullable=False)
    name = Column(String(40), nullable=False)
    surname = Column(String(40), nullable=False)
    password = Column(String(40), nullable=False)
    salt = Column(String(40), nullable=False)
    gender = Column(String(1),nullable=False)
    
engine = create_engine('postgresql://postgres:123456@localhost:5432/test')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

''' 
# Insert a Person in the person table
new_person = Users(username='new person',email='ss',name='aa',surname='aa',password='testtt',salt='aa',gender = 'M')
session.add(new_person)
session.commit()
'''

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
        name =  request.form['reg_name']
        surname =  request.form['reg_surname']   
        if request.form['reg_gender'] == "male":
            gender = 'M'
        else:
            gender = 'F'
        new_user = Users(username=username,email=email,name=name,surname=surname,password=hashed_password,salt=salt,gender = gender)
        session.add(new_user)
        session.commit()
        return render_template("home.html")
