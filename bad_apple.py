#使用opencv提取badapple视频截图
import cv2

file = open('DATA_ROM','w+')
file.write("v2.0 raw\n")

vid = cv2.VideoCapture("BADAPPLE.flv")

origin_hz = 60              #原始视频帧率
tar_hz = 30                 #期望截取每秒帧数
step = origin_hz // tar_hz  #截取步长
size = (16,16)              #缩小到16x16

test_count = 0
step_count = 0
ret = True
data = 0x0
while ret:
    ret,img = vid.read()
    if step_count >= step:
        step_count = 0
        continue
    if step_count != 0:
        step_count += 1
        continue
    img16x16 = cv2.resize(img, size, interpolation = cv2.INTER_AREA)
    for W in range(16):
        for H in range(16):
            pixel = img16x16[H,W]
            if pixel[0] < 10 and pixel[1] < 10 and pixel[2] < 10:
                data = (data << 1) | 0x1
            else:
                data = (data << 1) | 0x0
        file.write(hex(data)[2:]+"\t")
        data = 0x0
        if W == 7 or W == 15:
            file.write("\n")

    step_count += 1
    # test_count += 1
    # if test_count > 200:
    #     break