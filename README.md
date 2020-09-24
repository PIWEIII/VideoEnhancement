# 

# 基于Retinex算法实现的低光模糊视频增强技术

# How To Run ?



## 1. 建立目录

首先在计算机的任意位置建立如下所示的目录结构：

VE

​	frames	--存储原始帧

​	frames_enhanced	--存储增强帧

​	result_video	--存储增强视频

## 2.修改代码中的地址

### 2.1 VFtranslator.py

修改VideoToFrames函数中的

```py
os.chdir('你的地址/VE/')
```

修改FramesToVideo函数中的

```py
os.chdir('你的地址/VE/frames_enhanced/')
```



### 2.2 Retinex.py

修改enhancer函数中的

```py
img = '你的地址/VE/frames/image' + str(i) + '.jpg'
```

和

```py
cv2.imwrite('你的地址/VE/frames_enhanced/' + str(i) + '.jpg', result)
```

## 3.Run

运行 run.py

