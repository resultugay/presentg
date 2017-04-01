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
from User import User
from datetime import datetime
from flask_login.utils import current_user
from datetime import datetime
from Group import Group

Base = declarative_base()    


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

groups  = Blueprint('groups',__name__)
ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


@groups.route('/create_new_group', methods=['GET', 'POST'])
def group_page():
    if request.method == 'GET':
        return render_template("sign_up.html")
    else:
        group_name = request.form['create_group_name']
        group_id = ""
        for i in range(16):
            group_id = group_id + (random.choice(ALPHABET))   
        creator_email = current_user.get_email()
        creation_date = datetime.now()
        new_group = Group(group_id =group_id, group_name = group_name,creator_email=creator_email,creation_date=creation_date)
        session.add(new_group)
        session.commit()
        return render_template("home.html")
