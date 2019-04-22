#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from os.path import join as osjoin
from tqdm import tqdm
import cv2
import shutil
import numpy as np
from align import AlignDlib


# In[2]:

# Load model train sẵn
from model import create_model
nn4_small2_pretrained = create_model()
nn4_small2_pretrained.load_weights('weights/nn4.small2.v1.h5')


# In[3]:


#Load dữ liệu từ database
import pickle

PATH_NEW_DATABASE = osjoin(os.getcwd(), 'newdatabase')
PATH_DATABASE = osjoin(os.getcwd(), 'database')
PATH_DATABASE_IMAGE = osjoin(PATH_DATABASE, 'image')

if not os.path.isfile(osjoin(PATH_DATABASE, 'x_vector.pkl')) or not os.path.isfile(osjoin(PATH_DATABASE, 'x_label.pkl')) or not os.path.isfile(osjoin(PATH_DATABASE, 'x_name.pkl')):
	x_vector = []
	x_label = []
	x_name = []
else:
   with open(osjoin(PATH_DATABASE, 'x_vector.pkl'), 'rb') as f:
    	x_vector = pickle.load(f)
   with open(osjoin(PATH_DATABASE, 'x_label.pkl'), 'rb') as f:
   	x_label = pickle.load(f)
   with open(osjoin(PATH_DATABASE, 'x_name.pkl'), 'rb') as f:
   	x_name = pickle.load(f)


# In[4]:


# Hàm load ảnh
def load_img(path):
    img = cv2.imread(path, 1)
    return img[...,::-1]

# Hàm resize và align ảnh
alignment = AlignDlib('models/landmarks.dat')
def align_image(img):
    return alignment.align(96, img, alignment.getLargestFaceBoundingBox(img),
                           landmarkIndices=AlignDlib.OUTER_EYES_AND_NOSE)


# In[5]:


# Đọc ảnh, cut ảnh trong newdatabase và paste vào database nếu đọc được
# Tính toán các vector, gán nhãn và lấy tên người trong ảnh
if len(x_label) > 0: 
    count = x_label[-1]+1
else:
    count = 0

for mtimg in tqdm(os.listdir(PATH_NEW_DATABASE)):
    ext = os.path.splitext(osjoin(PATH_NEW_DATABASE, mtimg))[1]
    pathimg = osjoin(PATH_NEW_DATABASE,mtimg)
    if ext != '.jpg' and  ext != '.jpeg': 
        continue
    img = load_img(pathimg)
    if img is None : 
        continue
        
    shutil.move(pathimg, osjoin(PATH_DATABASE_IMAGE, mtimg))
    img = align_image(img)
    img = (img / 255.).astype(np.float32)
    img = np.expand_dims(img, axis=0)
    x_vector.append(nn4_small2_pretrained.predict(img)[0])
    x_label.append(count)
    x_name.append(mtimg[:mtimg.rfind(ext)])
    count += 1


# In[7]:


# Lưu vector, nhãn và tên người 
with open(osjoin(PATH_DATABASE, 'x_vector.pkl'), 'wb') as f:
    pickle.dump(x_vector, f)
with open(osjoin(PATH_DATABASE, 'x_label.pkl'), 'wb') as f:
    pickle.dump(x_label, f)
with open(osjoin(PATH_DATABASE, 'x_name.pkl'), 'wb') as f:
    pickle.dump(x_name, f)





