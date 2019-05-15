import os
import cv2
import shutil
import numpy as np
from align import AlignDlib
from model import create_model

class ProcessImage:
    def __init__(self):
        self.nn4_small_pretrained = create_model()
        self.nn4_small_pretrained.load_weights('weights/nn4.small2.v1.h5')
        self.alignment = AlignDlib('models/landmarks.dat')

    def align_image(self, img, box):
        return self.alignment.align(96, img, box,
                           landmarkIndices=AlignDlib.OUTER_EYES_AND_NOSE)

    def get_boxs(self,img):
        return self.alignment.getAllFaceBoundingBoxes(img)

    def get_max_box(self, img):
        return self.alignment.getLargestFaceBoundingBox(img)

    def img2vect(self, img):
        img = (img / 255.).astype(np.float32)
        img = np.expand_dims(img, axis=0)
        return self.nn4_small_pretrained.predict(img)[0]

    def draw(self, img, text, box):
        startX = box.left()
        startY = box.top()
        endX = startX + box.width()
        endY = startY + box.height()
        cv2.rectangle(img, (startX, startY), (endX, endY),(0, 0, 255), 5)
        cv2.putText(img, text, (startX, startY), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 5)
        return img

    def load_img(self, path):
        img = cv2.imread(path, 1)
        return img

    def save_img(self, img, path):
        cv2.imwrite(path,img)