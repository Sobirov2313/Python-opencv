# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SbNLWZcwsw8hjFQPV0w9AloC6tX7ucFF
"""

pip install opencv-python

from google.colab.patches import cv2_imshow
import cv2
rasm= cv2.imread("download.jpg")
cv2_imshow(rasm)

qoraoq= cv2.cvtColor(rasm, cv2.COLOR_BGR2GRAY)
cv2_imshow(qoraoq)

from google.colab.patches import cv2_imshow
import cv2
rasm2= cv2.imread("download2.jpg")
cv2_imshow(rasm2)

qoraoq= cv2.cvtColor(rasm2, cv2.COLOR_BGR2GRAY)
cv2_imshow(qoraoq)

from google.colab.patches import cv2_imshow
import cv2
rasm3= cv2.imread("download3.jpg")
cv2_imshow(rasm3)

qoraoq= cv2.cvtColor(rasm3, cv2.COLOR_BGR2GRAY)
cv2_imshow(qoraoq)

from google.colab.patches import cv2_imshow
import cv2
rasm4= cv2.imread("download4.jpg")
cv2_imshow(rasm4)

qoraoq= cv2.cvtColor(rasm4, cv2.COLOR_BGR2GRAY)
cv2_imshow(qoraoq)