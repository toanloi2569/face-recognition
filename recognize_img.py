#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import the necessary packages
#from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import pickle
import time
import cv2
import os
from cv2_imshow import cv2_imshow
from align import AlignDlib
from matplotlib import pyplot as plt


# In[2]:
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to img need recognize")
args = vars(ap.parse_args())
img_to_recognize = cv2.imread(args["image"], 1)

from model import create_model


# In[3]:


print ('[INFO] loading face detector')
nn4_small_pretrained = create_model()
nn4_small_pretrained.load_weights('weights/nn4.small2.v1.h5')

print ('[INFO] loading emb face')
import pickle 
with open('database/x_vector.pkl', 'rb') as f:
    x_vector = pickle.load(f)
    
with open('database/x_label.pkl', 'rb') as f:
    x_label = pickle.load(f)
    
with open('database/x_name.pkl', 'rb') as f:
    x_name = pickle.load(f)

# In[5]:


alignment = AlignDlib('models/landmarks.dat')
def align_image(img, box):
    return alignment.align(96, img, box,
                           landmarkIndices=AlignDlib.OUTER_EYES_AND_NOSE)

def get_boxs(img):
    return alignment.getAllFaceBoundingBoxes(img)

def img2vect(img):
    img = (img / 255.).astype(np.float32)
    img = np.expand_dims(img, axis=0)
    return nn4_small_pretrained.predict(img)[0]

def draw(img, text, box):
    startX = box.left()
    startY = box.top()
    endX = startX + box.width()
    endY = startY + box.height()
    cv2.rectangle(img, (startX, startY), (endX, endY),(0, 255, 0), 2)
    cv2.putText(img, text, (startX, startY), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    return img


boxs = get_boxs(img_to_recognize)  
if boxs is not None: 
    for box in boxs:
        img = align_image(img_to_recognize, box)
        yv = img2vect(img)
        
        minimum = 999
        person = "unknow"
        acc = 1
        for xv, xn in zip(x_vector, x_name):
            dist = np.sum(np.square(xv - yv))
            if dist > 0.5: continue
            if dist < minimum: 
                minimum = dist
                person = xn
                acc = (0.5 - dist)/0.5
        
        img_to_recognize = draw(img_to_recognize, person, box)
        plt.imshow(img_to_recognize)
        plt.show()

else:
    print ("No image found or The photo does not have a human face")

# In[ ]:



