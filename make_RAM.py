#根据汇编代码生成ram的内容

ASM = [
    # 'LDA R1 f0',
    # 'LDA R2 f1',
    # 'LDA GPIO1 f2',
    # 'LDA GPIO2 f3',
    # 'NOP',
    # 'NOP',
    # 'NOP',
    # 'NOP',
    # 'NOP',
    # 'NOP',
    # 'MOV R1 11',
    # 'MOV R2 22',
    # 'NOP',
    # 'NOP',
    # 'NOP',
    # 'NOP',
    # 'NOP',
    # 'ADD GPIO1',
    # 'LDO GPIO2 03',
    # 'STA R1 ff',
    'MOV R1 10',
    'STA R1 fe',    #内存地址fe存放点阵的列数
    'LDO R1 0',     #数据ROM的00地址存放帧总数
    'STA R1 ff',    #内存地址ff存放读取到的帧总数
    'MOV R1 0',
    'MOV R2 1',
    'STA R1 fd',    #loop_start #内存地址fd存放每一帧的列计数
    'LDA GPIO2 fd', #将内存fd地址的值（列计数），存入GPIO2
    'LDOA GPIO1 fd',#将内存地址fd的值作为地址，读取ROM数据（列数据），存入GPIO1
    'ADD R1',       #列计数++
    'STA R1 fd',    #loop_start #内存地址fd存放每一帧的列计数
    'LDA GPIO2 fd', #将内存fd地址的值（列计数），存入GPIO2
    'LDOA GPIO1 fd',#将内存地址fd的值作为地址，读取ROM数据（列数据），存入GPIO1
    'ADD R1',       #列计数++
    'STA R1 fd',    #loop_start #内存地址fd存放每一帧的列计数
    'LDA GPIO2 fd', #将内存fd地址的值（列计数），存入GPIO2
    'LDOA GPIO1 fd',#将内存地址fd的值作为地址，读取ROM数据（列数据），存入GPIO1
    'ADD R1',       #列计数++
    'STA R1 fd',    #loop_start #内存地址fd存放每一帧的列计数
    'LDA GPIO2 fd', #将内存fd地址的值（列计数），存入GPIO2
    'LDOA GPIO1 fd',#将内存地址fd的值作为地址，读取ROM数据（列数据），存入GPIO1
    'ADD R1',       #列计数++
    'STA R1 fd',    #loop_start #内存地址fd存放每一帧的列计数
    'LDA GPIO2 fd', #将内存fd地址的值（列计数），存入GPIO2
    'LDOA GPIO1 fd',#将内存地址fd的值作为地址，读取ROM数据（列数据），存入GPIO1
    'ADD R1',       #列计数++
    'STA R1 fd',    #loop_start #内存地址fd存放每一帧的列计数
    'LDA GPIO2 fd', #将内存fd地址的值（列计数），存入GPIO2
    'LDOA GPIO1 fd',#将内存地址fd的值作为地址，读取ROM数据（列数据），存入GPIO1
    'ADD R1',       #列计数++
    'STA R1 fd',    #loop_start #内存地址fd存放每一帧的列计数
    'LDA GPIO2 fd', #将内存fd地址的值（列计数），存入GPIO2
    'LDOA GPIO1 fd',#将内存地址fd的值作为地址，读取ROM数据（列数据），存入GPIO1
    'ADD R1',       #列计数++
    'STA R1 fd',    #loop_start #内存地址fd存放每一帧的列计数
    'LDA GPIO2 fd', #将内存fd地址的值（列计数），存入GPIO2
    'LDOA GPIO1 fd',#将内存地址fd的值作为地址，读取ROM数据（列数据），存入GPIO1
    'ADD R1',       #列计数++
    'STA R1 fd',    #loop_start #内存地址fd存放每一帧的列计数
    'LDA GPIO2 fd', #将内存fd地址的值（列计数），存入GPIO2
    'LDOA GPIO1 fd',#将内存地址fd的值作为地址，读取ROM数据（列数据），存入GPIO1
    'ADD R1',       #列计数++
    'STA R1 fd',    #loop_start #内存地址fd存放每一帧的列计数
    'LDA GPIO2 fd', #将内存fd地址的值（列计数），存入GPIO2
    'LDOA GPIO1 fd',#将内存地址fd的值作为地址，读取ROM数据（列数据），存入GPIO1
    'ADD R1',       #列计数++
    'STA R1 fd',    #loop_start #内存地址fd存放每一帧的列计数
    'LDA GPIO2 fd', #将内存fd地址的值（列计数），存入GPIO2
    'LDOA GPIO1 fd',#将内存地址fd的值作为地址，读取ROM数据（列数据），存入GPIO1
    'ADD R1',       #列计数++
    'STA R1 fd',    #loop_start #内存地址fd存放每一帧的列计数
    'LDA GPIO2 fd', #将内存fd地址的值（列计数），存入GPIO2
    'LDOA GPIO1 fd',#将内存地址fd的值作为地址，读取ROM数据（列数据），存入GPIO1
    'ADD R1',       #列计数++
    'STA R1 fd',    #loop_start #内存地址fd存放每一帧的列计数
    'LDA GPIO2 fd', #将内存fd地址的值（列计数），存入GPIO2
    'LDOA GPIO1 fd',#将内存地址fd的值作为地址，读取ROM数据（列数据），存入GPIO1
    'ADD R1',       #列计数++
    'STA R1 fd',    #loop_start #内存地址fd存放每一帧的列计数
    'LDA GPIO2 fd', #将内存fd地址的值（列计数），存入GPIO2
    'LDOA GPIO1 fd',#将内存地址fd的值作为地址，读取ROM数据（列数据），存入GPIO1
    'ADD R1',       #列计数++
    'STA R1 fd',    #loop_start #内存地址fd存放每一帧的列计数
    'LDA GPIO2 fd', #将内存fd地址的值（列计数），存入GPIO2
    'LDOA GPIO1 fd',#将内存地址fd的值作为地址，读取ROM数据（列数据），存入GPIO1
    'ADD R1',       #列计数++
    'STA R1 fd',    #loop_start #内存地址fd存放每一帧的列计数
    'LDA GPIO2 fd', #将内存fd地址的值（列计数），存入GPIO2
    'LDOA GPIO1 fd',#将内存地址fd的值作为地址，读取ROM数据（列数据），存入GPIO1
    'ADD R1',       #列计数++
    'NOP',
    'NOP',
    'NOP',          #强行视觉暂留
    'JMP NULL 06',  #跳转到loop_start
]

#RAM中的数据
DATA = {
    # 0xf0:0x1234,
    # 0xf1:0x2345,
    # 0xf2:0x3456,
    # 0xf3:0x4567,
}

file = open('RAM','w+')
file.write("v2.0 raw\n")

#define
ins_dict = {
    'NOP':0xf,
    'LDA':0x0,
    'MOV':0x1,
    'ADD':0x2,
    'LDO':0x3,
    'STA':0x4,
    'JMP':0x5,
    'LDOA':0x6,
}

reg_dict = {
    'R1':0x0,
    'R2':0x1,
    'GPIO1':0x2,
    'GPIO2':0x3,
    'NULL':0x0,#表示该指令与寄存器无关，故ins2的十六进制数可以为任何值
}

line_count = 0x0000 #ram中的每一行计数
count = 0           #存档格式计数


for line in ASM:
    if count >= 8:
        file.write("\n")
        count = 0
    ele = line.split(' ')
    #三目语句
    if len(ele) > 2:
        make_ins = (ins_dict[ele[0]] << 12) | (reg_dict[ele[1]] << 8) |  int(ele[2],16) 
        file.write(hex(make_ins)[2:]+"\t")
        count+=1
        line_count+=1
        continue
    #双目语句
    elif len(ele) > 1:
        make_ins = (ins_dict[ele[0]] << 12) | (reg_dict[ele[1]] << 8)
        file.write(hex(make_ins)[2:]+"\t")
        count+=1
        line_count+=1
        continue
    #单目语句
    else:
        make_ins = (ins_dict[ele[0]] << 12) | 0x0fff
        file.write(hex(make_ins)[2:]+"\t")
        count+=1
        line_count+=1
        continue
    count+=1
    line_count+=1

while(line_count != 0x10000):
    if count >= 8:
        file.write("\n")
        count = 0
    #判断是否为数据部分
    if line_count in DATA.keys():
        file.write(hex(DATA[line_count])[2:]+"\t")
        count+=1
        line_count+=1
        continue
    else:
        file.write("ffff\t")
        count+=1
        line_count+=1
        continue



# for bin in range(0xffff):
#     if count >= 8:
#         file.write("\n")
#         count = 0
#     t = (bin & 0xf00) >> 8
#     ins = (bin & 0x0f0) >> 4
#     reg = (bin & 0x00f)
#     #判断是否为RESET
#     if ins == 0xf and reg == 0xf:
#         file.write("0\t")
#         count+=1
#         continue
#     #判断是否为0、1周期指令
#     if t == 0x0:
#         file.write("01008\t")
#         count+=1
#         continue
#     elif t == 0x1:
#         file.write("00406\t")
#         count+=1
#         continue
#     #判断指令
    
#     if ins == LDA:
#         file.write(hex(LDA_t(t,reg))[2:]+"\t")
#         count+=1
#         continue
#     if ins == MOV:
#         file.write(hex(MOV_t(t,reg))[2:]+"\t")
#         count+=1
#         continue
#     file.write("0\t")
#     count+=1

