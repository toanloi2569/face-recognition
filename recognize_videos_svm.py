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


# In[2]:


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


# In[4]:


print (x_name)


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
    cv2.rectangle(img, (startX, startY), (endX, endY),(0, 0, 255), 2)
    cv2.putText(img, text, (startX, startY), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
    return img


# In[6]:


with open('models/svm.pkl', 'rb') as f:
    svm = pickle.load(f)


# In[ ]:





# In[8]:


print ("[INFO] starting video stream...")
vs = cv2.VideoCapture(-1)
time.sleep(2.0)

# start the FPS throughput estimator
fps = FPS().start()

# loop over frames from the video file stream
while True:
    # grab the frame from the threaded video stream
    ret, frame = vs.read()
    
    boxs = get_boxs(frame)
       
    if boxs is not None: 
        for box in boxs:
            img = align_image(frame, box)
            yv = np.reshape(img2vect(img), (1, -1))
            
            dist = np.max(svm.decision_function(yv))
            print (svm.decision_function(yv))
            if dist < -0.2:
                print (dist)
                person = "unknow"
                print (person)
                print ('*'*60)
            else:
                lb = svm.predict(yv)
                for i, name in enumerate(x_name):
                    if x_label[i] == lb:
                        person = name
                        print (person)
                        print (dist)
                        print ('*'*60)
                
            draw(frame, person, box)
        
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    fps.update()
    if key == ord("q"):
        break
fps.stop()
cv2.destroyAllWindows()
vs.release()


# In[8]:


vs.release()


# In[ ]:




