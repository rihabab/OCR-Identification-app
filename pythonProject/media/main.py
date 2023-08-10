
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


# Page segmentation modes:
#   0    Orientation and script detection (OSD) only.
#   1    Automatic page segmentation with OSD.
#   2    Automatic page segmentation, but no OSD, or OCR. (not implemented)
#   3    Fully automatic page segmentation, but no OSD. (Default)
#   4    Assume a single column of text of variable sizes.
#   5    Assume a single uniform block of vertically aligned text.
#   6    Assume a single uniform block of text.
#   7    Treat the image as a single text line.
#   8    Treat the image as a single word.
#   9    Treat the image as a single word in a circle.
#  10    Treat the image as a single character.
#  11    Sparse text. Find as much text as possible in no particular order.
#  12    Sparse text with OSD.
#  13    Raw line. Treat the image as a single text line,
#        bypassing hacks that are Tesseract-specific.




myconfig = r"--psm 11 --oem 3"




# plt.imshow(img)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# th, threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
# text1 = pytesseract.image_to_data(threshed,output_type='data.frame')
# text2 = pytesseract.image_to_string(threshed, lang="ind")
# # print(text2)
# text = text1[text1.conf != -1]
# lines = text.groupby('block_num')['text'].apply(list)
# conf = text.groupby(['block_num'])['conf'].mean()

# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', text.shape[0]+1)
# d = pytesseract.image_to_data(img, output_type=Output.DICT)
# print(d.keys())

# n_boxes = len(text1['text'])
# for i in range(n_boxes):
#     if int(text1['conf'][i]) > 98:
#         (x, y, w, h) = (text1['left'][i], text1['top'][i], text1['width'][i], text1['height'][i])
#         img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)



# plt.figure(figsize=(10,10))
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# plt.show()








# def grayscale(image):
#     return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# gray_image = grayscale(img)
# cv2.imwrite("media/temp/gray.jpg", gray_image)


# thresh, im_bw = cv2.threshold(gray_image, 150, 230, cv2.THRESH_BINARY)
# cv2.imwrite("media/temp/bw_image.jpg", im_bw)



img = cv2.imread(r"C:\Users\Rihab\PycharmProjects\pythonProject\pythonProject\media\img_ID_Card_Benin.jpg")

def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
gray_image = grayscale(img)

cv2.imwrite(r"C:\Users\Rihab\PycharmProjects\pythonProject\pythonProject\media\temp\gray.jpg", gray_image)





# thresh, im_bw = cv2.threshold(gray_image, 117, 170, cv2.THRESH_BINARY)
# cv2.imwrite(r"C:\Users\Rihab\PycharmProjects\pythonProject\pythonProject\media\temp\bw_image.jpg", im_bw)

# def noise_removal(image):
#     import numpy as np
#     kernel = np.ones((1, 1), np.uint8)
#     image = cv2.dilate(image, kernel, iterations=1)
#     kernel = np.ones((1, 1), np.uint8)
#     image = cv2.erode(image, kernel, iterations=1)
#     image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
#     image = cv2.medianBlur(image, 3)
#     return (image)


# no_noise = noise_removal(im_bw)
# cv2.imwrite(r"C:\Users\Rihab\PycharmProjects\pythonProject\pythonProject\media\temp\no_noise.jpg", no_noise)


text1 = pytesseract.image_to_data(gray_image, output_type='data.frame')
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


array=[]
i=0
for line in text_lines:
    array.append(line.split(" "))
    i+=1
    print(line)
print(array)









# height, width, _ = img.shape

# boxes = pytesseract.image_to_boxes(gray_image, config=myconfig)

# for box in boxes.splitlines():
#     box = box.split(" ")
#     gray_image = cv2.rectangle(gray_image, (int(box[1]), height - int(box[2])), (int(box[3]), height - int(box[4])), (0, 255, 0), 2)

# cv2.imshow(gray_image)
# cv2.waitKey(0)






# path = os.path.join(dir_path, "temp/gray.jpg")

# text = pytesseract.image_to_string(PIL.Image.open(path), config=myconfig)


# print(text)


