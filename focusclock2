# 导入所需的模块
import time
import tkinter as tk
import winsound

# 定义专注时钟类
class FocusClock:
    # 初始化方法，设置窗口属性和变量
    def __init__(self):
        # 创建主窗口
        self.window = tk.Tk()
        # 设置窗口标题
        self.window.title("专注时钟")
        # 设置窗口大小和位置
        self.window.geometry("300x200+400+200")
        # 设置窗口不可调整大小
        self.window.resizable(False, False)
        # 创建标签控件，用于显示时间
        self.time_label = tk.Label(self.window, text="", font=("Arial", 32))
        # 将标签控件放置在窗口中央
        self.time_label.pack(expand=True)
        # 创建标签控件，用于显示日期和星期
        self.date_label = tk.Label(self.window, text="", font=("Arial", 16))
        # 将标签控件放置在窗口底部
        self.date_label.pack(side=tk.BOTTOM)
        # 定义专注时间（分钟）
        self.focus_time = 25
        # 定义休息时间（分钟）
        self.break_time = 5
        # 定义倒计时时间（秒）
        self.countdown_time = self.focus_time * 60
        # 定义状态变量，用于判断当前是专注状态还是休息状态
        self.state = "focus"
        # 调用更新时间的方法
        self.update_time()
        # 进入主循环，等待用户事件
        self.window.mainloop()

    # 定义更新时间的方法，用于显示当前的时间、日期和星期，并进行倒计时和提醒
    def update_time(self):
        # 获取当前的时间对象
        now = time.localtime()
        # 格式化当前的时间字符串，如 12:34:56
        time_str = time.strftime("%H:%M:%S", now)
        # 格式化当前的日期和星期字符串，如 2023-08-23 星期三
        date_str = time.strftime("%Y-%m-%d %A", now)
        # 将时间字符串显示在标签控件上
        self.time_label["text"] = time_str
        # 将日期和星期字符串显示在标签控件上
        self.date_label["text"] = date_str
        # 判断当前是否是专注状态
        if self.state == "focus":
            # 将窗口背景色设置为绿色，表示专注状态
            self.window["bg"] = "green"
            # 判断倒计时时间是否为零
            if self.countdown_time == 0:
                # 播放提示音，表示专注时间结束，需要休息一下
                winsound.Beep(1000, 1000)
                # 将状态变量设置为休息状态
                self.state = "break"
                # 将倒计时时间设置为休息时间乘以60秒
                self.countdown_time = self.break_time * 60
            else:
                # 将倒计时时间减一秒
                self.countdown_time -= 1
                # 计算倒计时时间的分钟和秒数，如 24:59
                minutes, seconds = divmod(self.countdown_time, 60)
                # 在时间字符串后面添加倒计时时间，如 12:34:56 (24:59)
                time_str += " ({:02d}:{:02d})".format(minutes, seconds)
                # 将更新后的时间字符串显示在标签控件上
                self.time_label["text"] = time_str

        else: # 当前是休息状态
            # 将窗口背景色设置为红色，表示休息状态
            self.window["bg"] = "red"
            # 判断倒计时时间是否为零
            if self.countdown_time == 0:
                # 播放提示音，表示休息时间结束，需要继续专注
                winsound.Beep(2000, 1000)
                # 将状态变量设置为专注状态
                self.state = "focus"
                # 将倒计时时间设置为专注时间乘以60秒
                self.countdown_time = self.focus_time * 60
            else:
                # 将倒计时时间减一秒
                self.countdown_time -= 1
                # 计算倒计时时间的分钟和秒数，如 04:59
                minutes, seconds = divmod(self.countdown_time, 60)
                # 在时间字符串后面添加倒计时时间，如 12:34:56 (04:59)
                time_str += " ({:02d}:{:02d})".format(minutes, seconds)
                # 将更新后的时间字符串显示在标签控件上
                self.time_label["text"] = time_str

        # 1000毫秒后再次调用本方法，实现循环更新
        self.window.after(1000, self.update_time)

# 创建专注时钟对象
fc = FocusClock()
