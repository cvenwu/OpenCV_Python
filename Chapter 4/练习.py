"""
@File : 练习.py

@Author: sivan Wu

@Date : 2020/1/11 11:26 上午

@Desc : 当你用 OpenCV 加载一个彩色图像，并用 Matplotib 显示它时会遇 到一些困难。请阅读this discussion并且尝试理解它

"""
import numpy as np

import cv2

IMAGE_PATH = "../data/timg.jpeg"
image = cv2.imread(IMAGE_PATH, cv2.IMREAD_COLOR)
img2 = image[:,:,::-1]
import matplotlib.pyplot as plt
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)
plt.show()