"""
@File : matplotlib绘制灰色图的直方图.py

@Author: sivan Wu

@Date : 2020/1/12 4:20 下午

@Desc :

"""

import cv2
import matplotlib.pyplot as plt

image = cv2.imread("../data/angela.jpeg", cv2.IMREAD_GRAYSCALE)

## 使用opencv 统计直方图函数 和 matplotlib显示
## 返回的hist 是一个 256x1 的数组，每一个值代表了与次灰度值对应的像素点数 目
hist = cv2.calcHist([image], [0], None, [256], [0, 256])
print(hist)
plt.plot(hist)
plt.show()

import numpy as np

## 使用numpy统计直方图函数np.bincount() 和 matplotlib显示
image = cv2.imread("../data/angela.jpeg", cv2.IMREAD_GRAYSCALE)
hist2 = np.bincount(image.ravel(), minlength=256)
print(len(hist2))  # 256
print(type(hist2))  # <class 'numpy.ndarray'>
plt.plot(hist2)
plt.show()

## 使用numpy统计直方图函数np.histogram() 和 matplotlib显示
hist, bins = np.histogram(image.ravel(), 256, [0, 256])
print(type(hist))
print(len(hist))
plt.plot(hist)
plt.show()
