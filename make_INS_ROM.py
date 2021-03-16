#根据自定义指令集生成微指令rom的内容

file = open('INS_ROM','w+')
file.write("v2.0 raw\n")

#define
LDA = 0x0
MOV = 0x1
ADD = 0x2
LDO = 0x3
STA = 0x4
JMP = 0x5
LDOA = 0x6
RST = 0xf

R1 = 0x0
R2 = 0x1
GPIO1 = 0x2
GPIO2 = 0x3

#寄存器判断
def switch_reg_in(reg):
    if reg == R1:
        return 0x10000
    elif reg == R2:
        return 0x04000
    elif reg == GPIO1:
        return 0x00080
    elif reg == GPIO2:
        return 0x00040
    else:
        return 0x00000
def switch_reg_out(reg):
    if reg == R1:
        return 0x08000
    elif reg == R2:
        return 0x02000
    else:
        return 0x00000
#LDA指令的不同周期对应不同控制码
def LDA_t(t,reg):
    if t == 0x2:
        return 0x01001
    elif t == 0x3:
        return (0x00400 | switch_reg_in(reg))
    else:
        return 0x00000
#MOV
def MOV_t(t,reg):
    if t == 0x2:
        return (0x00001 | switch_reg_in(reg))
    else:
        return 0x00000
#ADD
def ADD_t(t,reg):
    if t == 0x2:
        return 0x00020
    elif t == 0x3:
        return (0x20000 | switch_reg_in(reg))
    else:
        return 0x00000
#LDO
def LDO_t(t,reg):
    if t == 0x2:
        return 0x00201
    elif t == 0x3:
        return (0x00100 | switch_reg_in(reg))
    else:
        return 0x00000
#STA
def STA_t(t,reg):
    if t == 0x2:
        return 0x01001
    elif t == 0x3:
        return (0x00800 | switch_reg_out(reg))
    else:
        return 0x00000
#JMP
def JMP_t(t,reg):
    if t == 0x2:
        return 0x00011
    else:
        return 0x00000
#LDOA
def LDOA_t(t,reg):
    if t == 0x2:
        return 0x01001
    elif t == 0x3:
        return 0x00600
    elif t == 0x4:
        return (0x00100 | switch_reg_in(reg))
    else:
        return 0x00000
count = 0
for bin in range(0xffff):
    if count >= 8:
        file.write("\n")
        count = 0
    t = (bin & 0xf00) >> 8
    ins = (bin & 0x0f0) >> 4
    reg = (bin & 0x00f)
    #判断是否为0、1周期指令
    if t == 0x0:
        file.write("01008\t")
        count+=1
        continue
    elif t == 0x1:
        file.write("00406\t")
        count+=1
        continue
    #判断是否为RESET
    if ins == RST:
        file.write("0\t")
        count+=1
        continue
    #判断指令
    if ins == LDA:
        file.write(hex(LDA_t(t,reg))[2:]+"\t")
        count+=1
        continue
    if ins == MOV:
        file.write(hex(MOV_t(t,reg))[2:]+"\t")
        count+=1
        continue
    if ins == ADD:
        file.write(hex(ADD_t(t,reg))[2:]+"\t")
        count+=1
        continue
    if ins == LDO:
        file.write(hex(LDO_t(t,reg))[2:]+"\t")
        count+=1
        continue
    if ins == STA:
        file.write(hex(STA_t(t,reg))[2:]+"\t")
        count+=1
        continue
    if ins == JMP:
        file.write(hex(JMP_t(t,reg))[2:]+"\t")
        count+=1
        continue
    if ins == LDOA:
        file.write(hex(LDOA_t(t,reg))[2:]+"\t")
        count+=1
        continue
    file.write("0\t")
    count+=1

