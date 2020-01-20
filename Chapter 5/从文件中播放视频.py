"""
@File : 从文件中播放视频.py

@Author: sivan Wu

@Date : 2020/1/11 3:45 下午

@Desc :
            与从摄像头中捕获一样，你只需要把设备索引号改成视频文件的名字。在播放每一帧时，使用 cv2.waiKey() 设置适当的持续时间。
            如果设置的太低视 频就会播放的非常快，如果设置的太高就会播放的很慢（你可以使用这种方法 控制视频的播放速度）。
            通常情况下 25 毫秒就可以了
"""


import cv2
import numpy as np

cap = cv2.VideoCapture("./自己写代码/10秒.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow("frame", frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
