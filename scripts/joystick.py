import hid

# 修改为你的手柄 VID/PID
VID = 0x054C   # PlayStation example
PID = 0x05C4

h = hid.device()
h.open(VID, PID)

print("连接成功，开始读取数据...")

while True:
    data = h.read(64)  # 读取 64 字节 HID 报文
    if data:
        print(data)