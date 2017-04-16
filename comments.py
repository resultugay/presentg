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
from Comment import get_last_3_comments
from psycopg2._json import json

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
    comment = request.args.get('comme', 0)
    comment_date = datetime.now()
    new_comment = Comment(owner_email=owner_email,file_id=file_id,comment=comment,comment_date=comment_date)
    session.add(new_comment)
    session.commit()    

    com = get_last_3_comments(file_id)  
    comments = []  
    dates = []
    for a in com:
        print(a.comment)  
        comments.append(a.comment)  
        dates.append(a.comment_date.strftime("%Y-%m-%d %H:%M:%S"))
        print(a.comment_date.strftime("%Y-%m-%d %H:%M:%S"))
    
    
    li = ['1','2','3']
    #return jsonify(result=comments2)
    com = "dsada"
    return json.dumps({'status':'OK','comments':list(reversed(comments)),'dates':list(reversed(dates)),'aa':"bb"}) 

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, datetime):
        serial = obj.isoformat()
        return serial
    raise TypeError ("Type not serializable")