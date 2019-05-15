'''
Created on Apr 6, 2019

@author: toanloi
'''

import cv2

from PIL import Image
from IPython.display import display

def cv2_imshow(img):
    img = img.clip(0, 255).astype('uint8')
    if img.ndim == 3:
        if img.shape[2] == 4:
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    display(Image.fromarray(img))