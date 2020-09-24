import cv2
import numpy as np
import os
class VTF():
    def VideoToFrames(self,videoName):
        print('Dividing video...')
        os.chdir('C:/Users/Desktop/Desktop/VE')
        # 读取视频，并逐帧分解成图片
        cap = cv2.VideoCapture(videoName)  # 打开视频
        isOpened = cap.isOpened()  # 是否打开？
        print(isOpened)

        # 获取视频相关信息：每一帧的宽高应一致
        fps = cap.get(cv2.CAP_PROP_FPS)  # 帧率，每秒有多少张图片
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 宽
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 高
        print(fps, width, height)  # 输出信息

        i = 0
        while (isOpened):
            # 读取视频的前60秒图像 共 60*int(fps)张
            if i == int(fps) * 60:
                break
            else:
                i = i + 1
            (flag, frame) = cap.read()  # 读取每一张flag frame
            filename = './frames/image' + str(i) + '.jpg'
            # 将读取的图片写入文件夹中
            if (flag) == True:
                cv2.imwrite(filename, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
        print('video divided!')


    def FramesToVideo(self,resultName):
        print('frames is under processing...')
        os.chdir('C:/Users/Desktop/Desktop/VE/frames_enhanced/')
        ##读取零散图片(上面分解的图片)，并将其合成视频
        img = cv2.imread('1.jpg')
        imginfo = img.shape
        size = (imginfo[1], imginfo[0])  # 与默认不同，opencv使用 height在前，width在后，所有需要自己重新排序
        print(size)

        # 创建写入对象，包括 新建视频名称，每秒钟多少帧图片(10张) ,size大小
        # 一般人眼最低分辨率为19帧/秒
        # 下方函数的参数分别是：输出文件名，每秒帧数、size大小
        videoWrite = cv2.VideoWriter('C:/Users/Desktop/Desktop/VE/result_video/'+resultName, -1, 22, size)
        # 60s的视频一般是1440帧左右
        for i in range(1, 132):
            filename = str(i) + '.jpg'
            img = cv2.imread(filename, 1)  # 1 表示彩图，0表示灰度图
            # 直接写入图片对应的数据
            videoWrite.write(img)
        videoWrite.release()  # 关闭写入对象
        print('video have made')
