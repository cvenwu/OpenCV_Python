"""
@File : 保存图像.py

@Author: sivan Wu

@Date : 2020/1/11 10:50 上午

@Desc : 使用函数cv2.imwrite(param1, param2) param1是一个字符串的文件名字，param2是一个cv2读取到的ndarray对象

"""

import cv2

IMAGE_PATH = "../data/timg.jpeg"
image = cv2.imread(IMAGE_PATH, cv2.IMREAD_COLOR)  # cv2.IMREAD_GRAYSCALE = 0
cv2.imwrite("大头儿子.png", image)  # 如果原文件夹有该文件将会覆盖
