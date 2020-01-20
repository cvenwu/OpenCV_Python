"""
@File : opencv统计直方图.py

@Author: sivan Wu

@Date : 2020/1/12 4:07 下午

@Desc :

"""


import cv2
import matplotlib.pyplot as plt
image = cv2.imread("../data/angela.jpeg", cv2.IMREAD_GRAYSCALE)

## 使用opencv 统计直方图函数
## 返回的hist 是一个 256x1 的数组，每一个值代表了与次灰度值对应的像素点数 目
hist = cv2.calcHist([image], [0], None, [256], [0, 256])
print(hist)
plt.plot(hist)
plt.show()
