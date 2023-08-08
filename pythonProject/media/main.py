import pytesseract
import PIL.Image
import cv2

import os
import json



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

# # Get the directory of the current script
# dir_path = os.path.dirname(os.path.realpath(__file__))

# # Create the full path to the image
# image_path = os.path.join(dir_path, "table.png")

# text = pytesseract.image_to_string(PIL.Image.open(image_path), config=myconfig)


# print(text)


# data = {'var': text}  # The data you want to share
# with open('data.json', 'w') as f:
#     json.dump(data, f)




# import pytesseract
# from PIL import Image

# # Open an image file
# img = Image.open(r'media\text.png')

# # Use Tesseract to do OCR on the image
# text = pytesseract.image_to_string(img)

# # Print the text
# print(text)

# import os
# print(os.getcwd())







# Get the directory of the current script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Create the full path to the image
image_path = os.path.join(dir_path, "DL.jpg")


img = cv2.imread(image_path)




def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_image = grayscale(img)
cv2.imwrite("media/temp/gray.jpg", gray_image)


thresh, im_bw = cv2.threshold(gray_image, 130, 100, cv2.THRESH_BINARY)
cv2.imwrite("media/temp/bw_image.jpg", im_bw)



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
# cv2.imwrite("media/temp/no_noise.jpg", no_noise)






path = os.path.join(dir_path, "temp/gray.jpg")

text = pytesseract.image_to_string(PIL.Image.open(path), config=myconfig)


print(text)



# thresh, im_bw = cv2.threshold(gray_image, 210, 230, cv2.THRESH_BINARY)
# cv2.imwrite("media/temp/bw_image.jpg", im_bw)

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
# cv2.imwrite("media/temp/no_noise.jpg", no_noise)