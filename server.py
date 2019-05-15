import sys
from flask import Flask, jsonify, request, render_template, flash, redirect, url_for,send_from_directory
from werkzeug.utils import secure_filename
import os
import shutil
import urllib
from process_image import ProcessImage

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
UPLOAD_FOLDER = 'static/uploaded_file/'
TMP_FOLDER = 'static/tmp/'
PATH_PROJECT = os.getcwd()

prosess_image = ProcessImage()
pathfile = ''

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if "upload-file" in request.form:
            return up_file(request)

        if "search" in request.form:
            # detected_path, align_path = face_detect(pathfile)
            filename = pathfile.split('/')[-1]
            # return render_template('search_img.html', filename=filename, detected_path=detected_path, align_path=align_path)
            detected, align = detected(pathfile)
            detected_path = urllib.quote(detected_path)
            return render_template('search_img.html', filename=filename, detected_path=detected_path)

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
    global pathfile
    pathfile = os.path.join(UPLOAD_FOLDER, filename)
    file.save(pathfile)
    return render_template('search_img.html', filename=filename)

# def search():

def face_detect(pathfile):
    shutil.rmtree(os.path.join(PATH_PROJECT, TMP_FOLDER))
    os.mkdir(os.path.join(PATH_PROJECT, TMP_FOLDER))

    img = prosess_image.load_img(pathfile)
    box = prosess_image.get_max_box(img)
    align = prosess_image.align_image(img, box)
    detected = prosess_image.draw(img, '', box)

    # detected_path = os.path.join(PATH_PROJECT, TMP_FOLDER, 'detected.png')
    # align_path = os.path.join(PATH_PROJECT, TMP_FOLDER, 'align.png')
    # prosess_image.save_img(detected, detected_path)
    # prosess_image.save_img(align, align_path)
    # return (detected_path.split('/')[-1] , align_path.split('/')[-1])
    return (detected, align)

# def find_db():

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port listening')
    args = parser.parse_args()
    port = args.port
    app.secret_key = 'super secret key'
    app.run(host='0.0.0.0', port=port)