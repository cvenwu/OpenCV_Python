"""
@File : 读入图像.py

@Author: sivan Wu

@Date : 2020/1/11 10:26 上午

@Desc : 使用cv2.imread()读取一幅图像
        警告：就算图像的路径是错的，OpenCV 也不会提醒你的， 但是当你使用命 令print img时得到的结果是None
"""

import cv2

IMAGE_PATH = "../data/timg.jpeg"

# 读入彩色图, 第二个参数是cv2.IMREAD_COLOR(默认为该参数)
# 读入一副彩色图像。 图像的透明度会被忽略， 这是默认参数
image = cv2.imread(IMAGE_PATH, cv2.IMREAD_COLOR)  # 返回的类型是<class 'numpy.ndarray'>， cv2.IMREAD_COLOR = 1
print("--------------彩色图像开始--------------")
print(image.shape)
print(type(image))
print("--------------彩色图像开始--------------")
# 读入灰色图像，第二个参数是cv2.IMREAD_GRAYSCALE
image_gray = cv2.imread(IMAGE_PATH, cv2.IMREAD_GRAYSCALE)  # cv2.IMREAD_GRAYSCALE = 0
print("--------------灰色图像开始--------------")
print(image_gray.shape)
print(type(image_gray))
print("--------------灰色图像开始--------------")
# cv2.IMREAD_UNCHANGED：读入一幅图像，并且包括图像的 alpha 通道
image_gray_with_alpha = cv2.imread(IMAGE_PATH, cv2.IMREAD_UNCHANGED)
print("--------------读取带alpha通道的图像开始--------------")
print(image_gray_with_alpha.shape)
print(type(image_gray_with_alpha))
print("--------------读取带alpha通道的图像开始--------------")



