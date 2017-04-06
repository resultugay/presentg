import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import flash
from flask import Blueprint, abort, flash, redirect, render_template, url_for
from flask import current_app
from flask import send_from_directory


UPLOAD_FOLDER = '/pdfs'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])



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
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save('pdfs/' + filename) 
            return redirect(url_for('pdf.uploaded_file',filename=filename))
    return render_template("file_upload.html")


@pdf.route('/pdfs/<filename>')
def uploaded_file(filename):
    return send_from_directory('pdfs/',filename)