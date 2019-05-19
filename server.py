import sys
from flask import Flask, jsonify, request, render_template, flash, redirect, url_for,send_from_directory
from werkzeug.utils import secure_filename
import os
from os.path import join as osjoin
import pickle
import numpy as np

from process_image import ProcessImage

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
UPLOAD_FOLDER = 'static/uploaded_file/'
TMP_FOLDER = 'static/tmp/'
PATH_PROJECT = os.getcwd()

process_image = ProcessImage()
pathfile = ''

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

with open('models/svm.pkl', 'rb') as f:
    svm = pickle.load(f)

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if "upload-file" in request.form:
            return up_file(request)

        if "search" in request.form:
            filename = pathfile.split('/')[-1]

            detected, align = face_detect(pathfile)
            name_of_nearest_faces, path_to_nearest_faces  = search(align)

            detected_b64 = process_image.img2base64(detected)
            align_b64 = process_image.img2base64(align)
            return render_template('search_img.html', filename=filename, 
                detected=detected_b64, align=align_b64, 
                name_of_nearest_faces=name_of_nearest_faces, path_to_nearest_faces=path_to_nearest_faces)

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
    img = process_image.load_img(pathfile)
    box = process_image.get_max_box(img)
    align = process_image.align_image(img, box)
    detected = process_image.draw(img[...,::-1], '', box)
    return (detected, align)

def search(align):
    x_name, x_label, x_name_map = load_data()
    yv = np.reshape(process_image.img2vect(align), (1, -1))
    
    list_dist = svm.decision_function(yv)
    list_label = svm.classes_
    nearest_dist = list_dist.argsort()[0][-5:][::-1]
    nearest_label = list_label[nearest_dist]

    path_to_nearest_faces = []
    name_of_nearest_faces = []
    for nlb in nearest_label:
        for i, lb in enumerate(x_label):
            if nlb == lb and x_name[i] not in name_of_nearest_faces:
                name_of_nearest_faces.append(x_name[i])
                path_to_nearest_faces.append(x_name_map[i].split('/')[-1])
    return (name_of_nearest_faces, path_to_nearest_faces)

def load_data():
    print ("Load face emb")
    with open(osjoin(PATH_PROJECT, 'static', 'database', 'x_label.pkl'), 'rb') as f:
        x_label = pickle.load(f)
    with open(osjoin(PATH_PROJECT, 'static', 'database', 'x_name.pkl'), 'rb') as f:
        x_name = pickle.load(f)
    with open(osjoin(PATH_PROJECT, 'static', 'database', 'x_name_map.pkl'), 'rb') as f:
        x_name_map = pickle.load(f)
    return (x_name, x_label, x_name_map)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port listening')
    args = parser.parse_args()
    port = args.port
    app.secret_key = 'super secret key'
    app.run(host='0.0.0.0', port=port, debug=True)