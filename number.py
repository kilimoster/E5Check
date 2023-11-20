# 导入random模块
import random

# 定义一个猜数字的游戏函数
def guess_number():
    # 生成一个1到100之间的随机整数
    answer = random.randint(1, 100)
    # 初始化猜测次数为0
    count = 0
    # 循环直到猜对或放弃
    while True:
        # 提示用户输入一个数字
        guess = input("请输入一个1到100之间的数字，或者输入q退出：")
        # 如果用户输入q，退出游戏
        if guess == "q":
            print("游戏结束，谢谢参与！")
            break
        # 尝试把用户输入转换为整数
        try:
            guess = int(guess)
        # 如果用户输入不是整数，提示错误并继续循环
        except ValueError:
            print("请输入一个有效的数字！")
            continue
        # 如果用户输入不在1到100之间，提示错误并继续循环
        if guess < 1 or guess > 100:
            print("请输入一个1到100之间的数字！")
            continue
        # 增加猜测次数
        count += 1
        # 如果用户猜对了，恭喜用户并退出游戏
        if guess == answer:
            print(f"恭喜你，你猜对了！你一共猜了{count}次。")
            break
        # 如果用户猜小了，提示用户并继续循环
        elif guess < answer:
            print("你猜小了，再试一次！")
        # 如果用户猜大了，提示用户并继续循环
        else:
            print("你猜大了，再试一次！")

# 调用游戏函数
guess_number()
