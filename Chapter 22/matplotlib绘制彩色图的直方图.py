"""
@File : matplotlib绘制彩色图的直方图.py

@Author: sivan Wu

@Date : 2020/1/12 4:20 下午

@Desc :

"""

import cv2
import matplotlib.pyplot as plt

image = cv2.imread("../data/angela.jpeg")

color = ['b', 'g', 'r']
# 绘制彩色图不同通道的直方图
for i, col in enumerate(color):
    hist = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])  # 包括256
plt.show()
