import time

def concentration_clock(minutes):
    seconds = minutes * 60
    for remaining_sec in range(seconds, 0, -1):
        mins = remaining_sec // 60
        secs = remaining_sec % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)

    print("专注时间结束！")

concentration_time = int(input("请输入专注时长（分钟）："))
concentration_clock(concentration_time)
