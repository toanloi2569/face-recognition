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
from process_image import ProcessImage


print ('[INFO] loading emb face')
with open('database/x_vector.pkl', 'rb') as f:
    x_vector = pickle.load(f)
with open('database/x_label.pkl', 'rb') as f:
    x_label = pickle.load(f)  
with open('database/x_name.pkl', 'rb') as f:
    x_name = pickle.load(f)


process_image = ProcessImage()

print ("[INFO] starting video stream...")
vs = cv2.VideoCapture(-1)
time.sleep(2.0)

# start the FPS throughput estimator
fps = FPS().start()

# loop over frames from the video file stream
while True:
    # grab the frame from the threaded video stream
    ret, frame = vs.read()
    boxs = process_image.get_boxs(frame)
       
    if boxs is not None: 
        for box in boxs:
            img = process_image.align_image(frame, box)
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
            
            process_image.draw(frame, person + ' ' + str(acc), box)
        
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    fps.update()
    if key == ord("q"):
        break

fps.stop()
cv2.destroyAllWindows()
vs.release()