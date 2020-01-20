"""
@File : 显示图像.py

@Author: sivan Wu

@Date : 2020/1/11 10:36 上午

@Desc : 显示图像：使用函数 cv2.imshow() 显示图像。窗口会自动调整为图像大小。第一 个参数是窗口的名字
，其次才是我们的图像。你可以创建多个窗口，只要你喜 欢，但是必须给他们不同的名字

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

# 显示图像
print("--------------显示图像开始--------------")
cv2.imshow("灰色图像", image_gray)  #
cv2.imshow("彩色图像", image)  #
cv2.waitKey(0)
cv2.destroyWindow("灰色图像")  # 想删除特定的窗口可以使用 cv2.destroyWindow()，在括号内输入你想删除的窗口名
cv2.destroyAllWindows()  # 可以轻易删除所有我们建立的窗口
print("--------------显示图像结束--------------")

# 另外一种情形：首先创建窗口，之后加载图像
cv2.namedWindow("窗口", cv2.WINDOW_NORMAL)
cv2.imshow("窗口", image_gray)
cv2.waitKey(0)
cv2.destroyWindow("窗口")
