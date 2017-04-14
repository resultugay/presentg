from flask.blueprints import Blueprint
from flask.templating import render_template
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Flask, jsonify, render_template, request
from flask_login.utils import  login_required
from flask_login.utils import current_user
from Comment import Comment
from datetime import datetime

Base = declarative_base()    

engine = create_engine('postgresql://rsltgy:123456@localhost:5432/itu')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

''' 
# Insert a Person in the person table
new_person = Users(username='new person',email='ss',name='aa',surname='aa',password='testtt',salt='aa',gender = 'M')
session.add(new_person)
session.commit()
'''

comments  = Blueprint('comments',__name__)



@comments.route('/comments')
@login_required
def comments_page():   
    owner_email = current_user.get_email()
    file_id = request.args.get('file_id', 0)
    comment = request.args.get('come', 0)
    comment_date = datetime.now()
    new_comment = Comment(owner_email=owner_email,file_id=file_id,comment=comment,comment_date=comment_date)
    session.add(new_comment)
    session.commit()    
    return jsonify(result=comment)

