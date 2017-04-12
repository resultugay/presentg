from flask.blueprints import Blueprint
from flask.templating import render_template
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_login.utils import  login_required
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



@groups_options.route('/groupsoptions')
@login_required
def group_options_page():
        return render_template("groups_options.html")

