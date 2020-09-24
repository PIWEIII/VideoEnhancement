import numpy as np
import cv2
import sys
import time
#基于Retinex算法实现的图像增强效果
class Retinex():
    def replaceZeroes(self,data):
        # np.nonzero函数是numpy中用于得到数组array中非零元素的位置（数组索引）的函数
        min_nonzero = min(data[np.nonzero(data)])
        data[data == 0] = min_nonzero
        return data

    def MSR(self,img,scales):
        weight = 1/3.0
        scales_size = len(scales)
        h,w = img.shape[:2]
        log_R = np.zeros((h,w),dtype=np.float32)

        for i in range(scales_size):
            img = Retinex().replaceZeroes(img)
            L_blur = cv2.GaussianBlur(img,(scales[i], scales[i]), 0)
            L_blur = Retinex().replaceZeroes(L_blur)
            dst_Img = cv2.log(img/255.0)
            dst_Lblur = cv2.log(L_blur/255.0)
            dst_Ixl = cv2.multiply(dst_Img,dst_Lblur)
            log_R += weight * cv2.subtract(dst_Img,dst_Ixl)
        dst_R = cv2.normalize(log_R,None,0,255,cv2.NORM_MINMAX)
        log_uint8 = cv2.convertScaleAbs(dst_R)
        return log_uint8

    def enhancer(self):
        scales = [15, 101, 301]  # [3,5,9]  #看不出效果有什么差别
        print('enhancing the images...')
        for i in range(1, 132):
            img = 'C:/Users/Desktop/Desktop/VE/frames/image' + str(i) + '.jpg'
            src_img = cv2.imread(img)
            b_gray, g_gray, r_gray = cv2.split(src_img)
            #分别对本张图片的R,G,B三个通道进行MSR计算
            b_gray = Retinex().MSR(b_gray, scales)
            g_gray = Retinex().MSR(g_gray, scales)
            r_gray = Retinex().MSR(r_gray, scales)
            result = cv2.merge([b_gray, g_gray, r_gray])
            #窗口显示图片（暂不需要）
            # cv2.imshow('img',src_img)
            # cv2.imshow('MSR_result',result)
            cv2.imwrite('C:/Users/Desktop/Desktop/VE/frames_enhanced/' + str(i) + '.jpg', result)
            #‘0’删除窗口
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            s1 = "\r[%s%s]%d%%" % ("*" * i, " " * (100 - i), i)
            sys.stdout.write(s1)
            sys.stdout.flush()
            time.sleep(0.3)
        print('images enhancement has done')
