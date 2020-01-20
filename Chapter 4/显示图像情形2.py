"""
@File : 显示图像情形2.py

@Author: sivan Wu

@Date : 2020/1/11 10:44 上午

@Desc : 显示图像.py中我们首先读取图像之后才将创建窗口将图像送进去，现在我们可以先创建窗口，再将读取的图像送入
建 议：一 种 特 殊 的 情 况 是， 你 也 可 以 先 创 建 一 个 窗 口， 之 后 再 加 载 图 像。 这 种 情 况 下，
你 可 以 决 定 窗 口 是 否 可 以 调 整 大 小。 使 用 到 的 函 数 是 cv2.namedWindow()。 初 始 设 定 函 数
标 签 是 cv2.WINDOW_AUTOSIZE。 但 是 如 果 你 把 标 签 改 成 cv2.WINDOW_NORMAL， 你就可以调整窗口大小了。
当图像维度太大， 或者要添加轨迹条时，调整窗口大小将会很有用
"""


import cv2

IMAGE_PATH = "../data/timg.jpeg"
image_gray = cv2.imread(IMAGE_PATH, cv2.IMREAD_GRAYSCALE)  # cv2.IMREAD_GRAYSCALE = 0
cv2.namedWindow("win_name", cv2.WINDOW_AUTOSIZE)
cv2.imshow("win_name", image_gray)
cv2.waitKey(0)
cv2.destroyWindow("win_name")



