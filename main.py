import pygame,time,sys
from pygame.locals import *
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



Board = []
Role = 2
resultFlag = 0
isRun =0
mouse_cursor = pygame.image.load("images/black_piece.png")  #加载鼠标图片

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

    if flag:
        resultFlag = value #获取五子连珠的棋子颜色
        print("白子胜利！" if value ==1 else "黑子胜利")


def main():
    global Board,resultFlag,isRun,screen,info,bg0,bg3,bg4

    initBoard(27,27)# 初始化棋盘
    pygame.init()     # 初始化游戏环境
    screen = pygame.display.set_mode((780, 620), RESIZABLE, 32)  # 创建游戏窗口 # 第一个参数是元组：窗口的长和宽

    pygame.display.set_caption("五子棋1.0———by风清扬")                # 添加游戏标题
    info = pygame.image.load("images/info.jpg")  #
    bg0= pygame.image.load("images/bg0.jpeg")          #加载背景图片
    bg3 = pygame.image.load("images/bg3.jpg")
    bg4 = pygame.image.load("images/bg4.jpeg")  #
    background= pygame.image.load("images/bg.png")  # 加载背景图片
    whitePiece = pygame.image.load("images/white_piece.png") #加载白棋图片
    blackPiece= pygame.image.load("images/black_piece.png") #加载黑棋图片
    blackWin = pygame.image.load("images/black_win.jpg")  # 加载黑棋胜利图片
    whiteWin = pygame.image.load("images/white_win.jpg")  # 加载黑棋胜利图片


    happy_effect.play(-1)

    while True:

        while isRun==0:                         #欢迎界面
            screen.blit(bg0, (0, 0))
            screen.blit(bg3, (618, 0))
            screen.blit(bg4, (623, 305))
            pygame.display.update()  # 更新视图
            eventHander()

        while isRun > 0:                        #开始后界面
            happy_effect.stop()


            screen.blit(background, (0, 0))
            screen.blit(bg3, (618, 0))
            screen.blit(bg4, (623, 305))

            for temp in Board:
                x, y = pygame.mouse.get_pos()
                x -= mouse_cursor.get_width() / 2
                y -= mouse_cursor.get_height() / 2

                for point in temp:
                    if point.value == 1:  # 白棋
                        screen.blit(whitePiece, (point.x - 18, point.y - 18))
                    elif point.value == 2:  # 黑棋
                        screen.blit(blackPiece, (point.x - 18, point.y - 18))

            if x >= 580 and x <= 770 and y >= 0 and y <= 620:
                pass
            else:
                screen.blit(mouse_cursor, (x, y))

            if resultFlag > 0:
                Board = []  # 清空棋盘
                initBoard(27, 27)  #  初始化棋盘
                if resultFlag == 1:
                    screen.blit(whiteWin, (200, 150))
                else:
                    screen.blit(blackWin, (200, 150))

            pygame.display.update()  # 更新视图

            if resultFlag > 0:

                pygame.mixer.music.stop()
                win_effect.play()
                time.sleep(4)
                resultFlag = 0
                pygame.mixer.music.play(-1)

            eventHander()
        else:
            eventHander()
            while isRun == -1:             #####游戏规则界面
                screen.blit(info, (0, 0))
                screen.blit(bg3, (618, 0))
                screen.blit(bg4, (623, 305))
                pygame.display.update()  # 更新视图
                eventHander()

if __name__ == '__main__':
   main()        #调用主函数绘制窗口


