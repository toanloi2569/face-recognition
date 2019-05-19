
import os
from os.path import join as osjoin
from tqdm import tqdm
import pickle
import cv2
import shutil
import numpy as np
from align import AlignDlib
from process_image import ProcessImage


PATH_NEW_DATABASE = osjoin(os.getcwd(), 'newdatabase')
PATH_DATABASE = osjoin(os.getcwd(), 'static', 'database')
PATH_DATABASE_IMAGE = osjoin(PATH_DATABASE, 'image')

if not os.path.isfile(osjoin(PATH_DATABASE, 'x_vector.pkl')) or not os.path.isfile(osjoin(PATH_DATABASE, 'x_label.pkl')):
    if not os.path.isfile(osjoin(PATH_DATABASE, 'x_name.pkl')) or not os.path.isfile(osjoin(PATH_DATABASE, 'x_name_map.pkl')):
        x_vector = []
        x_label = []
        x_name = []
        x_name_map = []
else:
    with open(osjoin(PATH_DATABASE, 'x_vector.pkl'), 'rb') as f:
        x_vector = pickle.load(f)
    with open(osjoin(PATH_DATABASE, 'x_label.pkl'), 'rb') as f:
        x_label = pickle.load(f)
    with open(osjoin(PATH_DATABASE, 'x_name.pkl'), 'rb') as f:
        x_name = pickle.load(f)
    with open(osjoin(PATH_DATABASE, 'x_name_map.pkl'), 'rb') as f:
        x_name_map = pickle.load(f)

# Đọc ảnh, cut ảnh trong newdatabase và paste vào database nếu đọc được
# Tính toán các vector, gán nhãn và lấy tên người trong ảnh
if len(x_label) > 0: 
    count = x_label[-1]+1
else:
    count = 0

process_image = ProcessImage()
for root, directories, files in os.walk(PATH_NEW_DATABASE):
    for d in tqdm(directories):
        directory = osjoin(PATH_NEW_DATABASE, d)
        for mtimg in os.listdir(directory):
            pathimg = osjoin(directory, mtimg)
            ext = os.path.splitext(pathimg)[1]
            if ext != '.jpg' and  ext != '.jpeg':
                shutil.move(pathimg, osjoin(PATH_DATABASE_IMAGE, 'x'))   
                continue
            img = process_image.load_img(pathimg)
            
            try:  
                box = process_image.get_max_box(img)
                img = process_image.align_image(img, box)
                v = process_image.img2vect(img)
                x_vector.append(v)
                x_label.append(count)
                x_name.append(d)
                x_name_map.append(osjoin(directory, mtimg))
            except: 
                print (osjoin(PATH_DATABASE_IMAGE, 'x'))
                shutil.move(pathimg, osjoin(PATH_DATABASE_IMAGE, 'x')) 
                continue
        count += 1
        shutil.move(directory, osjoin(PATH_DATABASE_IMAGE, d))

# Lưu vector, nhãn và tên người 
with open(osjoin(PATH_DATABASE, 'x_vector.pkl'), 'wb') as f:
    pickle.dump(x_vector, f)
with open(osjoin(PATH_DATABASE, 'x_label.pkl'), 'wb') as f:
    pickle.dump(x_label, f)
with open(osjoin(PATH_DATABASE, 'x_name.pkl'), 'wb') as f:
    pickle.dump(x_name, f)
with open(osjoin(PATH_DATABASE, 'x_name_map.pkl'), 'wb') as f:
    pickle.dump(x_name_map, f)