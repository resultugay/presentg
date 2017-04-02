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
from flask_login.utils import current_user, login_required
from datetime import datetime
from Group import Group
from Group_member import Group_member
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

groups_options  = Blueprint('groups_options',__name__)
ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"



@groups_options.route('/<string:group_id>')
@login_required
def group_options_page(group_id):
        return render_template("groups.html")

