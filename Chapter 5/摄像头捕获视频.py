"""
@File : 摄像头捕获视频.py

@Author: sivan Wu

@Date : 2020/1/11 12:03 下午

@Desc : 为了获取视频，你应该创建一个 VideoCapture 对象
他的参数可以是 设备的索引号，或者是一个视频文件。设备索引号就是在指定要使用的摄像头。 一般的笔记本电脑都有内置摄像头。所以参数就是 0。
你可以通过设置成 1 或 者其他的来选择别的摄像头。之后，你就可以一帧一帧的捕获视频了。但是最 后，别忘了停止捕获视频
"""

import cv2

cap = cv2.VideoCapture(0)

# while True:
while cap.isOpened():  # 检查是否成功初始化摄像头, 如果返回值为True,就没有问题了，否则就需要使用函数cap.open()
    # Capture frame-by-frame
    # cap.read() 返回一个布尔值（True/False）。 如果帧读取的是正确的，就是True。
    # 所以最后你可以通过检查他的返回值来查看视频文件是否已经到了结尾
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    # 获得额外的视频信息
    ## 使用函数 cap.get(propId) 来获得视频的一些参数信息, propId 可以是 0 到 18 之间的任何整数。每一个数代表视频的一个属性
    ## 其中的一些值可以使用 cap.set(propId,value) 来修改，value 就是 你想要设置成的新值
    width = cap.get(3)
    height = cap.get(4)
    print(width, height)

    # Display the resulting frame
    cv2.imshow("frame", gray)
    # 0xFF：0xFF是一个位掩码，十六进制常数，二进制值为11111111, 它将左边的24位设置为0,
    # 把返回值限制在在0和255之间。ord(’ ')返回按键对应的整数（ASCII码）
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
