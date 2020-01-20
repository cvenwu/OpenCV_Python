"""
@File : numpy统计直方图.py

@Author: sivan Wu

@Date : 2020/1/12 4:13 下午

@Desc :

"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread("../data/angela.jpeg", cv2.IMREAD_GRAYSCALE)
# 第一种方法：使用np.histogram()统计直方图
hist = np.histogram(image.ravel(), 256, [0, 256])
# 第二种方法：使用np.bincount()统计直方图
hist2 = np.bincount(image.ravel(), minlength=256)

# plt.plot(np.array(list(hist)))
plt.plot(hist2)
plt.show()
# plt.show()
# print(np.array(hist))
print(type(hist))
print(type(hist2))
# print(hist)
print(len(hist))
print(len(hist2))