import sys
import pytesseract
import PIL.Image
import cv2
from pytesseract import Output
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import easyocr
sys.stdout.reconfigure(encoding='utf-8')
reader = easyocr.Reader(['en', 'fr'])




myconfig = r"--psm 11 --oem 3"






# Get the directory of the current script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Create the full path to the image
image_path = os.path.join(dir_path, "img_ID_Card_Benin.jpg")


img = cv2.imread(image_path)


# def grayscale(image):
#     return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# gray_image = grayscale(img)
# cv2.imwrite("media/temp/gray.jpg", gray_image)


# img = cv2.imread("media/temp/gray.jpg")

if img is None:
    print("Failed to load image.")


plt.imshow(img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("media/temp/gray.jpg", gray)
th, threshed = cv2.threshold(gray, 200, 255, cv2.THRESH_TRUNC)

# threshed = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

text1 = pytesseract.image_to_data(threshed, output_type='data.frame')
text = text1[text1.conf != -1]


grouped_lines = text.groupby(['block_num', 'par_num', 'line_num'])

text_lines = []

# for _, group in grouped_lines:
#     sorted_group = group.sort_values(by='left')  
#     text_line = ' '.join(sorted_group.text) 

for _, group in grouped_lines:
    sorted_group = group.sort_values(by='left')  
    text_line = ' '.join(sorted_group.text)
    text_lines.append(text_line)



for line in text_lines:
    print(line)



