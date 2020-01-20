"""
@File : matplotlib绘图.py

@Author: sivan Wu

@Date : 2020/1/11 11:07 上午

@Desc :
注意：彩色图像使用 OpenCV 加载时是 BGR 模式。但是 Matplotib 是 RGB 模式。所以彩色图像如果已经被 OpenCV 读取，
那它将不会被 Matplotib 正 确显示。具体细节请看练习

"""

import matplotlib.pyplot as plt
import cv2

IMAGE_PATH = "../data/timg.jpeg"
image = cv2.imread(IMAGE_PATH, cv2.IMREAD_COLOR)
plt.imshow(image, cmap='gray', interpolation='bicubic')
plt.xticks([])
plt.yticks([])
plt.show()
