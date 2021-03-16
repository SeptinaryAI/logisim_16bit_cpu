import cv2

file = open('TEST','w+')
file.write("v2.0 raw\n")

img16x16 = cv2.imread('test.jpg')

data = 0x0
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