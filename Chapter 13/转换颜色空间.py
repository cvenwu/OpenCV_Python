"""
@File : 转换颜色空间.py

@Author: sivan Wu

@Date : 2020/1/13 6:46 下午

@Desc : 转换颜色空间

cv2.cvtColor(input_image，ﬂag)，其中 ﬂag 就是转换类型。

对于 BGR↔Gray 的转换，我们要使用的 ﬂag 就是 cv2.COLOR_BGR2GRAY。
同样对于 BGR↔HSV 的转换，我们用的 ﬂag 就是 cv2.COLOR_BGR2HSV。 你还可以通过下面的命令得到所有可用的 ﬂag

"""

import cv2

# 颜色空间转换函数可以用的所有flag可以通过如下方式获得
flag_list = [i for i in dir(cv2) if i.startswith("COLOR_")]
print(flag_list)
print(len(flag_list))


IMAGE_PATH = "../data/angela.jpeg"

image = cv2.imread(IMAGE_PATH)


image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
image_YCrCb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
print(image_gray.shape)
print(image_HSV.shape)

cv2.imshow("frame", image_HSV)
cv2.imshow("frame2", image_YCrCb)
cv2.waitKey(0)
cv2.destroyAllWindows()




