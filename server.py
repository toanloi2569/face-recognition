import sys
from flask import Flask, jsonify, request, render_template, flash, redirect, url_for,send_from_directory
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
UPLOAD_FOLDER = 'static/uploaded_file/'

# Instantiate our Node
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if "upload-file" in request.form:
            return up_file(request)
                                        
    return render_template('search_img.html')

def up_file(request):
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and not allowed_file(file.filename):
        flash('The file is not properly formatted')
        return redirect(request.url)
    
    filename = secure_filename(file.filename)
    pathfile = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(pathfile)
    return render_template('search_img.html', filename=filename)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port listening')
    args = parser.parse_args()
    port = args.port
    app.secret_key = 'super secret key'
    app.debug = True
    app.run(host='0.0.0.0', port=port)