"""
@File : 保存视频.py

@Author: sivan Wu

@Date : 2020/1/11 9:50 下午

@Desc : 捕获视频，并对每一帧都进行加工之后我们想要保存这个视频
        下面的代码是从摄像头中捕获视频，沿水平方向旋转每一帧并保存它。
"""

import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (60.0, 48.0))

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        # 第一个参数表示要旋转的视频，第二个参数表示旋转的方向，0表示绕x轴旋转，大于0的数表示绕y轴旋转，小于0的负数表示绕x和y轴旋转
        frame = cv2.flip(frame, 0)
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
