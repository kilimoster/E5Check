# 导入pygame库
import pygame
# 导入random库
import random

# 初始化pygame
pygame.init()
# 设置屏幕大小
screen = pygame.display.set_mode((800, 600))
# 设置窗口标题
pygame.display.set_caption('贪吃蛇')
# 设置时钟对象
clock = pygame.time.Clock()

# 定义颜色常量
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 定义蛇的初始位置和方向
snake_x = 400
snake_y = 300
snake_dir = 'right'
# 定义蛇的身体列表
snake_body = [(snake_x, snake_y)]
# 定义蛇的长度
snake_length = 1
# 定义蛇的速度
snake_speed = 10

# 定义食物的初始位置
food_x = random.randint(0, 79) * 10
food_y = random.randint(0, 59) * 10

# 定义游戏是否结束的标志
game_over = False

# 游戏主循环
while not game_over:
    # 处理事件
    for event in pygame.event.get():
        # 如果点击了关闭按钮，退出游戏
        if event.type == pygame.QUIT:
            game_over = True
        # 如果按下了键盘，改变蛇的方向
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != 'down':
                snake_dir = 'up'
            if event.key == pygame.K_DOWN and snake_dir != 'up':
                snake_dir = 'down'
            if event.key == pygame.K_LEFT and snake_dir != 'right':
                snake_dir = 'left'
            if event.key == pygame.K_RIGHT and snake_dir != 'left':
                snake_dir = 'right'

    # 根据蛇的方向移动蛇的位置
    if snake_dir == 'up':
        snake_y -= snake_speed
    if snake_dir == 'down':
        snake_y += snake_speed
    if snake_dir == 'left':
        snake_x -= snake_speed
    if snake_dir == 'right':
        snake_x += snake_speed

    # 判断蛇是否撞到了边界或自己，如果是，游戏结束
    if snake_x < 0 or snake_x > 790 or snake_y < 0 or snake_y > 590 or (snake_x, snake_y) in snake_body:
        game_over = True

    # 将蛇的新位置添加到身体列表中
    snake_body.append((snake_x, snake_y))
    # 如果身体列表的长度大于蛇的长度，删除最旧的位置
    if len(snake_body) > snake_length:
        snake_body.pop(0)

    # 判断蛇是否吃到了食物，如果是，增加蛇的长度和速度，并重新生成食物的位置
    if snake_x == food_x and snake_y == food_y:
        snake_length += 1
        snake_speed += 1
        food_x = random.randint(0, 79) * 10
        food_y = random.randint(0, 59) * 10

    # 填充屏幕背景色
    screen.fill(BLACK)
    # 画出蛇的身体
    for x, y in snake_body:
        pygame.draw.rect(screen, GREEN, (x, y, 10, 10))
    # 画出食物
    pygame.draw.rect(screen, RED, (food_x, food_y, 10, 10))
    # 更新屏幕显示
    pygame.display.flip()
    # 设置帧率
    clock.tick(30)

# 退出pygame
pygame.quit()
