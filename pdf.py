import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import flash
from flask import Blueprint, abort, flash, redirect, render_template, url_for
from flask import current_app
from flask import send_from_directory
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from File import File
from flask_login.utils import current_user
from datetime import datetime
from sign_up import ALPHABET
import random

UPLOAD_FOLDER = '/pdfs'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

Base = declarative_base()    


engine = create_engine('postgresql://postgres:123456@localhost:5432/test')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


pdf = Blueprint('pdf',__name__)



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@pdf.route('/<string:group_id>/flleupload',  methods=['GET', 'POST'])
def upload_file(group_id):
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        data = request.files['file'].read()
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save('pdfs/' + filename) 
            #newly added
            file_id = ""
            for i in range(16):
                file_id = file_id + (random.choice(ALPHABET))   
            fl = File(group_id = group_id,file_id=file_id,owner_email=current_user.get_email(),filename = file.filename,file = data,upload_date=datetime.now())
            session.add(fl)
            session.commit()
            print("done")
            #newly added
            return redirect(url_for('pdf.uploaded_file',filename=filename))
    return render_template("file_upload.html")


@pdf.route('/pdfs/<filename>')
def uploaded_file(filename):
    return send_from_directory('pdfs/',filename)