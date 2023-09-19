# 导入time模块
import time

# 定义一个倒计时函数，接受一个整数参数n，表示倒计时的秒数
def countdown(n):
    # 用while循环实现倒计时
    while n > 0:
        # 打印当前的秒数，并用\r回到行首
        print(n, end="\r")
        # 暂停1秒
        time.sleep(1)
        # 将秒数减1
        n -= 1
    # 倒计时结束后，打印Done
    print("Done")

# 调用倒计时函数，传入10作为参数
countdown(10)
