# 五子棋项目说明

## 1.1、概述

​				学习了一个学期的python，掌握了基本的语法和数据结构，了解了python制作小游戏的基本过程。因在本次期末考核内容中，我选择尝试制作一个自己感兴趣的游戏——五子棋。由于时间和能力有限，本次制作仅实现了最基本的功能：双人对战、查看游戏规则、游戏开始与暂停、播放背景音乐和音效。



## 1.2、游戏截图

![欢迎界面](https://user-images.githubusercontent.com/79883276/122643377-12e55c00-d142-11eb-991a-0fa3202716db.png)
![输赢判断界面](https://user-images.githubusercontent.com/79883276/122643382-1973d380-d142-11eb-8db2-007e9ae1abdd.png)
![游戏规则界面](https://user-images.githubusercontent.com/79883276/122643384-1b3d9700-d142-11eb-9706-eb877f66f847.png)
![游戏界面](https://user-images.githubusercontent.com/79883276/122643386-1d075a80-d142-11eb-8ed6-16cf07baf7f1.png)

## 2、主要功能的代码解析

####  2.1.1、导入包

```python
import pygame,time,sys
from pygame.locals import *
```

#### 2.1.2、设置全局变量

```python
Board = []  #棋盘
Role = 2	#游戏角色——黑或白 1:白、2:黑
resultFlag = 0	#判断输赢情况 1:白赢、2:黑赢
isRun =0	#判断游戏运行情况：-1:查看游戏规则界面、0:欢迎界面、1或2:游戏开始后界面、-2:暂停
```

#### 2.1.3、设置鼠标图片

```python
mouse_cursor = pygame.image.load("images/black_piece.png")  #加载鼠标图片
在每次下完棋子后，加载对方棋子的图片
```

#### 2.1.4、加载背景音乐和音乐

```python
pygame.mixer.init()
#混音器初始化

sound_effect = pygame.mixer.Sound("m.mp3")
win_effect = pygame.mixer.Sound("win.mp3")
pause_effect=pygame.mixer.Sound("pause.mp3")
info_effect=pygame.mixer.Sound("info.mp3")
exit_effect=pygame.mixer.Sound("exit.mp3")
happy_effect=pygame.mixer.Sound("happy.mp3")
bo_effect=pygame.mixer.Sound("bo.mp3")

pygame.mixer.music.load("bgm.mp3")#背景音乐
```

#### 2.2.1、游戏简单功能实现

```python

def exit():   #退出游戏
    print("Exit")
    exit_effect.play()
    time.sleep(1)
    pygame.quit()
    sys.exit()

def checkRole():    #查看游戏规则
    print("CheckRole")
    info_effect.play()
    global screen,info,bg0,bg3,bg4,isRun
    isRun=-1

def start():        #开始游戏
    print("Start")
    bo_effect.play()
    pygame.mixer.music.play()
    global isRun
    isRun=1

def pause():    #暂停/继续
    global isRun,pa
    if(isRun>0):
        print("pause")
    else:
        print("continue")
    pause_effect.play()
    isRun=isRun*(-2)

```

棋盘初始化

```python
class Point():
    def __init__(self,x,y,value):
        self.x,self.y,self.value = x,y,value


def initBoard(x,y):     #棋盘初始化
    print("初始化棋盘")
    for i in range(15): #总共15行
        rowlist = []
        for j in range(15):
            pointX,pointY= x+ j*40,y+ i*40  #每一行有15列
            p = Point(pointX,pointY,0)  #记录每一行与列的交点的坐标
            rowlist.append(p)
        Board.append(rowlist)#记录每一行的15个列的坐标
```

#### 2.2.2、游戏复杂功能实现

事件监视器

```python
def eventHander():              #事件监视器
    global mouse_cursor,Role,isRun

    for event in pygame.event.get():

        if event.type == QUIT:
           exit()
        if event.type == MOUSEBUTTONDOWN:

            x,y = pygame.mouse.get_pos()
            i=j=0
            if x>=638 and x<=730 and y>=229 and y<=255: #退出
                exit()
            if x >= 656 and x <= 759 and y >= 162 and y <= 181:  # 查看规则
                checkRole()
            if x >= 660 and x <= 748 and y >= 45 and y <= 68:  # 开始游戏
                start()
            if x >= 642 and x <= 728 and y >= 106 and y <= 130:  # 暂停游戏
                pause()

            if isRun>0:
                for temp in Board:
                    for point in temp:
                        if x >= point.x - 10 and x <= point.x + 10 and y >= point.y - 10 and y <= point.y + 10:
                            sound_effect.play()
                            if point.value == 0 and Role == 1:  # 若棋盘位置为空；棋子为白棋
                                point.value = 1  # 鼠标点击时，棋子为白棋
                                Judge(i, j, 1)
                                Role = 2  # 切换角色
                                mouse_cursor = pygame.image.load("images/black_piece.png")  # 切换鼠标图片（黑白棋子）
                            elif point.value == 0 and Role == 2:  # 若棋盘位置为空；棋子为黑棋
                                point.value = 2  # 鼠标点击时，棋子为黑棋
                                Judge(i, j, 2)
                                Role = 1  # 切换角色
                                mouse_cursor = pygame.image.load("images/white_piece.png")
                            break
                        j += 1
                    i += 1
                    j = 0


```

游戏判定功能

```python
def Judge(i,j,value):
    global resultFlag
    flag = False
    for x in  range(j - 4, j + 5):
        if x >= 0 and x + 4 < 15 :
            if Board[i][x].value == value and \
                Board[i][x + 1].value == value and \
                Board[i][x + 2].value == value and \
                Board[i][x + 3].value == value and \
                Board[i][x + 4].value == value :
                flag = True
                break
                pass
    for x in range(i - 4, i + 5):
        if x >= 0 and x + 4 < 15:
            if Board[x][j].value == value and \
                    Board[x + 1][j].value == value and \
                    Board[x + 2][j].value == value and \
                    Board[x + 3][j].value == value and \
                    Board[x + 4][j].value == value:
                flag = True
                break
                pass


    for x, y in zip(range(j + 4, j - 5, -1), range(i - 4, i + 5)):
        if x >= 0 and x + 4 < 15 and y + 4 >= 0 and y < 15:
            if Board[y][x].value == value and \
                    Board[y - 1][x + 1].value == value and \
                    Board[y - 2][x + 2].value == value and \
                    Board[y - 3][x + 3].value == value and \
                    Board[y - 4][x + 4].value == value:
                flag = True


    for x, y in zip(range(j - 4, j + 5), range(i - 4, i + 5)):
        if x >= 0 and x + 4 < 15 and y >= 0 and y + 4 < 15:
            if Board[y][x].value == value and \
                    Board[y + 1][x + 1].value == value and \
                    Board[y + 2][x + 2].value == value and \
                    Board[y + 3][x + 3].value == value and \
                    Board[y + 4][x + 4].value == value:
                flag = True

    if flag:               #如果条件成立，证明五子连珠
        resultFlag = value #获取成立的棋子颜色
        print("白子胜利！" if value ==1 else "黑子胜利")
```

### 3、其他说明

####  3.1游戏已经上传开源上传至github,以及我的个人网站：https://sheepsong.cn

#### 3.2 制作这个简单的游戏让我感受到了python的魅力，也让我更喜欢自己设计一些小玩意，希望在接下来的两年中，我能做出更加复杂有趣的东西吧！






