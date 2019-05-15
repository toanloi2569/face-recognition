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
from process_image import ProcessImage


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to img need recognize")
args = vars(ap.parse_args())
img_to_recognize = cv2.imread(args["image"], 1)


print ('[INFO] loading emb face')
import pickle 
with open('database/x_vector.pkl', 'rb') as f:
    x_vector = pickle.load(f)
with open('database/x_label.pkl', 'rb') as f:
    x_label = pickle.load(f)
with open('database/x_name.pkl', 'rb') as f:
    x_name = pickle.load(f)


process_image = ProcessImage()
boxs = process_image.get_boxs(img_to_recognize)  
if boxs is not None: 
    for box in boxs:
        img = process_image.align_image(img_to_recognize, box)
        yv = process_image.img2vect(img)
        
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
        
        img_to_recognize = process_image.draw(img_to_recognize, person, box)
        plt.imshow(img_to_recognize)
        plt.show()

else:
    print ("No image found or The photo does not have a human face")