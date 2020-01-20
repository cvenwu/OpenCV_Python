"""
@File : 总结一下.py

@Author: sivan Wu

@Date : 2020/1/11 11:00 上午

@Desc : 加载一个灰度图，显示图片，按下’s’键保存后退出，或者 按下 ESC 键退出不保存
        如果你用的是 64 位系统，你需要将 k = cv2.waitKey(0) 这行改成 k = cv2.waitKey(0)&0xFF
"""


import cv2

IMAGE_PATH = "../data/timg.jpeg"
image = cv2.imread(IMAGE_PATH, cv2.IMREAD_GRAYSCALE)
cv2.imshow("gray_image", image)
key = cv2.waitKey(0) & 0xFF  # 必选先点开图之后再按键盘
print(type(key))  # <class 'int'>
print(key)  # 119

if key == ord('s'):
    cv2.imwrite("保存的图像.png", image)
    cv2.destroyWindow("gray_image")
else:
    cv2.destroyWindow("gray_image")