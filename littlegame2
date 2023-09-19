// 导入Swing库
import javax.swing.*;
// 导入事件监听器接口
import java.awt.event.*;
// 导入颜色类
import java.awt.Color;
// 导入随机数类
import java.util.Random;
// 导入列表类
import java.util.ArrayList;

// 定义一个继承自JPanel的贪吃蛇面板类
public class SnakePanel extends JPanel implements ActionListener {
    // 定义颜色常量
    public static final Color BLACK = new Color(0, 0, 0);
    public static final Color WHITE = new Color(255, 255, 255);
    public static final Color RED = new Color(255, 0, 0);
    public static final Color GREEN = new Color(0, 255, 0);
    public static final Color BLUE = new Color(0, 0, 255);

    // 定义蛇的初始位置和方向
    private int snakeX = 400;
    private int snakeY = 300;
    private String snakeDir = "right";
    // 定义蛇的身体列表
    private ArrayList<Integer> snakeBodyX = new ArrayList<>();
    private ArrayList<Integer> snakeBodyY = new ArrayList<>();
    // 定义蛇的长度
    private int snakeLength = 1;
    // 定义蛇的速度
    private int snakeSpeed = 10;

    // 定义食物的初始位置
    private int foodX;
    private int foodY;

    // 定义随机数对象
    private Random random = new Random();

    // 定义计时器对象
    private Timer timer;

    // 定义游戏是否结束的标志
    private boolean gameOver = false;

    // 贪吃蛇面板类的构造方法
    public SnakePanel() {
        // 设置面板大小
        this.setSize(800, 600);
        // 设置面板背景色
        this.setBackground(BLACK);
        // 设置面板可见
        this.setVisible(true);
        // 设置面板可获取焦点
        this.setFocusable(true);
        // 添加键盘监听器，改变蛇的方向
        this.addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                switch (e.getKeyCode()) {
                    case KeyEvent.VK_UP:
                        if (!snakeDir.equals("down")) {
                            snakeDir = "up";
                        }
                        break;
                    case KeyEvent.VK_DOWN:
                        if (!snakeDir.equals("up")) {
                            snakeDir = "down";
                        }
                        break;
                    case KeyEvent.VK_LEFT:
                        if (!snakeDir.equals("right")) {
                            snakeDir = "left";
                        }
                        break;
                    case KeyEvent.VK_RIGHT:
                        if (!snakeDir.equals("left")) {
                            snakeDir = "right";
                        }
                        break;
                }
            }
        });
        // 初始化食物位置
        generateFood();
        // 创建计时器对象，每30毫秒触发一次动作事件
        timer = new Timer(30, this);
        // 启动计时器
        timer.start();
    }

    // 重写绘制组件方法，画出蛇和食物
    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        // 设置画笔颜色为绿色，画出蛇的身体
        g.setColor(GREEN);
        for (int i = 0; i < snakeLength; i++) {
            g.fillRect(snakeBodyX.get(i), snakeBodyY.get(i), 10, 10);
        }
        // 设置画笔颜色为红色，画出食物
        g.setColor(RED);
        g.fillRect(foodX, foodY, 10, 10);
    }

    // 重写动作事件处理方法，更新蛇和食物的位置和状态
    @Override
    public void actionPerformed(ActionEvent e) {
        // 根据蛇的方向移动蛇的位置
        switch (snakeDir) {
            case "up":
                snakeY -= snakeSpeed;
                break;
            case "down":
                snakeY += snakeSpeed;
                break;
            case "left":
                snakeX -= snakeSpeed;
                break;
            case "right":
                snakeX += snakeSpeed;
                break;
        }
        // 判断蛇是否撞到了边界或自己，如果是，游戏结束
        if (snakeX < 0 || snakeX > 790 || snakeY < 0 || snakeY > 590 || isHitSelf()) {
            gameOver = true;
            timer.stop();
            JOptionPane.showMessageDialog(this, "游戏结束！");
            System.exit(0);
        }
        // 将蛇的新位置添加到身体列表中
        snakeBodyX.add(snakeX);
        snakeBodyY.add(snakeY);
        // 如果身体列表的长度大于蛇的长度，删除最旧的位置
        if (snakeBodyX.size() > snakeLength) {
            snakeBodyX.remove(0);
            snakeBodyY.remove(0);
        }
        // 判断蛇是否吃到了食物，如果是，增加蛇的长度和速度，并重新生成食物的位置
        if (snakeX == foodX && snakeY == foodY) {
            snakeLength++;
            snakeSpeed++;
            generateFood();
        }
        // 重新绘制组件
        repaint();
    }

    // 定义一个生成食物位置的方法，保证食物不会出现在蛇身上
    public void generateFood() {
        do {
            foodX = random.nextInt(80) * 10;
            foodY = random.nextInt(60) * 10;
        } while (isOnSnake(foodX, foodY));
    }

    // 定义一个判断坐标是否在蛇身上的方法，返回布尔值
    public boolean isOnSnake(int x, int y) {
        for (int i = 0; i < snakeLength; i++) {
            if (x == snakeBodyX.get(i) && y == snakeBodyY.get(i)) {
                return true;
            }
        }
        return false;
    }

    // 定义一个判断蛇是否撞到自己的方法，返回布尔值
    public boolean isHitSelf() {
        for (int i = 0; i < snakeLength - 1; i++) {
            if (snakeX == snakeBodyX.get(i) && snakeY == snakeBodyY.get(i)) {
                return true;
            }
        }
        return false;
    }
}

// 定义一个继承自JFrame的贪吃蛇窗口类
public class SnakeFrame extends JFrame {
    // 贪吃蛇窗口类的构造方法
    public SnakeFrame() {
        // 设置窗口标题
        this.setTitle("贪吃蛇");
        // 设置窗口大小
        this.setSize(800, 600);
        // 设置窗口居中显示
        this.setLocationRelativeTo(null);
        // 设置窗口关闭时退出程序
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // 设置窗口不可调整大小
        this.setResizable(false);
        // 创建并添加贪吃蛇面板对象
        SnakePanel panel = new SnakePanel();
        this.add(panel);
        // 设置窗口可见
        this.setVisible(true);
    }

    // 主方法，创建贪吃蛇窗口对象
    public static void main(String[] args) {
        new SnakeFrame();
    }
}
