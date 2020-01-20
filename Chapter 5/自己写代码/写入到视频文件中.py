"""
@File : 写入到视频文件中.py

@Author: sivan Wu

@Date : 2020/1/12 10:20 上午

@Desc :


VideoWriter(filename, fourcc, fps, frameSize[, isColor]) -> <VideoWriter object>
1. 第一个参数是要保存的文件的路径
2. fourcc 指定编码器: 使用cv2.VideoWriter_fourcc(*'I420')创建的编码，可用编码列表参考 http://www.fourcc.org/codecs.php#letter_i
3. fps 要保存的视频的帧率
4. frameSize 要保存的文件的画面尺寸
5. isColor 指示是黑白画面还是彩色的画面

"""

import cv2

# 下面的编码采用I420, MJPG都可以
# fourcc = cv2.VideoWriter_fourcc(*'I420')
fourcc = cv2.VideoWriter_fourcc(*'MJPG')

cap = cv2.VideoCapture(0)
frame_width = int(cap.get(3))  # 获取宽度
frame_height = int(cap.get(4))  # 获取高度
# frame_width, frame_height 不能修改为其他值
writer = cv2.VideoWriter("out.avi", fourcc, 20.0, (frame_width, frame_height))
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame, 0)
        writer.write(frame)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()

writer.release()
cv2.destroyAllWindows()
