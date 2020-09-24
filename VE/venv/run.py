from VFtranslator import *
from Retinex import *
if __name__ == '__main__':
    videoName = 'Test.mp4'
    vtf = VTF()
    #视频分割
    vtf.VideoToFrames(videoName)
    #视频加强
    rtx = Retinex()
    rtx.enhancer()
    #输出视频
    vtf.FramesToVideo('result.mp4')