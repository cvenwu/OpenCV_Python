"""
@File : 打开视频文件.py

@Author: sivan Wu

@Date : 2020/1/11 8:48 下午

@Desc :

"""


import cv2


VIDEO_PATH = './10秒.mp4'
cap = cv2.VideoCapture(VIDEO_PATH)

count = 0
# 如果成功获取到文件或者摄像头
while cap.isOpened():
    ret, frame = cap.read()

    # 如果视频文件没有到结尾
    if ret == True:
        print(frame.shape)
        count += 1
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", frame_gray)
        if cv2.waitKey(28) & 0xFF == ord('q'):
            break
        print(count)
        if count % 28 == 0:
            cv2.imwrite("{}.png".format(count), frame_gray)
    else:
        break
print(count / 28)
cap.release()
cv2.destroyAllWindows()

