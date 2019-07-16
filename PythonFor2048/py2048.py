#coding:utf-8
#使用python实现2048游戏

import curses
from random import randrange,choice
from collections import defaultdict #collections是Python内建的一个集合模块，提供了许多有用的集合类。
 #defaultdict         使用CTRL+/可以快速注释多行！！！！！！！！
# '''# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
# >>> from collections import defaultdict
# >>> dd = defaultdict(lambda: 'N/A')
# >>> dd['key1'] = 'abc'
# >>> dd['key1'] # key1存在
# 'abc'
# >>> dd['key2'] # key2不存在，返回默认值
# 'N/A'
# 注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
# 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。

#定义用户行为，有‘上，下，左，右，重置，退出’六种行为
actions = ['Up','Down','Left','Right','Restart','Exit']
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
#ord()函数是chr()函数（对于8位的ASCII字符串）或unichr()函数（对于Unicode对象）
# 的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的ASCII数值，或者Unicode数值，如果所给的Unicode字符超出了你的Python定义范围，
# 则会引发一个TypeError的异常。

actions_dict = dict(zip(letter_codes,actions*2))
#zip()函数它是Python的内建函数，(与序列有关的内建函数有：sorted()、reversed()、enumerate()、zip()),
# 其中sorted()和zip()返回一个序列(列表)对象，reversed()、enumerate()返回一个迭代器(类似序列)

#状态机：处理游戏主逻辑的时候我们会用到一种十分常用的技术：状态机，或者更准确的说是有限状态机（FSM）你会发现 2048 游戏很容易就能分解
# 成几种状态的转换。

def main(stdscr):

    def init():
        game_field.reset()
        return 'Game'  #重置棋盘

    def not_game(state):
        # 画出 GameOver 或者 Win 的界面
        game_field.draw(stdscr)
        # 读取用户输入得到action，判断是重启游戏还是结束游戏
        action = get_user_action(stdscr)
        responses = defaultdict(lambda :state) #默认是当前状态，没有行为就会一直在当前界面循环
        responses['Restart'],responses['Exit'] = 'Init','Exit'  #对应不同的行为转换到不同的状态
        return responses[action]  #????????

    def game():
        #画出当前棋盘状态
        game_field.draw(stdscr)
        #读取用户输入得到action
        action =get_user_action(stdscr)
        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        #如果if成功移动了一步:
        if game_field.move(action):
            if game_field.is_win():
                return 'Win'
            if game_field.is_gameover():
                return 'Gameover'
        return 'Game'

    state_actions = {
        'Init':init,
        'Win':lambda :not_game('Win'),
        'Gameover':lambda :not_game('Gameover'),
        'Game':game
    }

    curses.use_default_colors()
    game_field = GameField(win=32)

    state = 'Init'

    #状态机循环开始
    while state != 'Exit':
        state = state_actions[state]()
    curses.wrapper(main)

    #用户输入处理::::阻塞＋循环，直到获得用户有效输入才返回对应行为：
def get_user_action(keyboard):
    char = 'N'
    while char not in actions_dict:
        char = keyboard.getch()  #????????
    return actions_dict[char]

    #矩阵转置和矩阵逆转
def transpose(field):
    return [list(row) for row in zip(*field)]
def invert(field):
    return [row[::-1] for row in field]

    #创建棋盘，初始化棋盘的参数，可以指定棋盘的高和宽以及游戏胜利条件，默认是最经典的 4x4～2048。
class GameField(object):
    def __init__(self,height=4,width=4,win=2048):
        self.height =height
        self.width = width
        self.win_value =2048
        self.score = 0
        self.highscore = 0
        self.reset()
    # 绘制游戏界面
def draw(self,screen):
    help_string1 = '(W)Up (S)Down (A)Left (D)Right'
    help_string2 = '       (R)Restart (Q)Exit'
    gameover_string = '                      GAME OVER'
    win_string = '           YOU WIN!'
    def cast(string):
            screen.addstr(string+'\n')
    #绘制水平分割线
    def draw_hor_separator(self):
        line='+'+('+-------'*self.width+'+')[1:]
        separator =defaultdict(lambda :line)
        if not hasattr(self.draw_hor_separator, "counter"):
            self.draw_hor_separator.counter=0
        cast(separator[self.draw_hor_separator.counter])
        self.draw_hor_separator.counter+=1

    def draw_row(row):
        cast(''.join('|{:^5}'.format(num) if num>0 else '|    ' for num in row)+'|')

    screen.clear()

    cast('SCORE:'+str(self.score))
    if 0!= self.highscore:
        cast('HGHSCORE:'+str(self.highscore))

    for row in self.field:
        draw_hor_separator()
        draw_row()
    draw_hor_separator()

    if self.is_win():
        cast(win_string)
    else:
        if self.is_gameover():
            cast(gameover_string)
        else:
            cast(help_string1)
    cast(help_string2)


    #棋盘操作，随机生成一个2或者4
def spawn(self):
    new_element = 4 if randrange(100) >89 else 2
    (i,j) = choice([(i,j) for i in range(self.width) for j in range(self.height) if self.field[i][j]==0])
    self.field[i][j] = new_element

    #重置棋盘
def reset(self):
    if self.score>self.highscore:
        self.highscore = self.score
    self.score = 0
    self.field = [[0 for i in range(self.width)] for j in range(self.height)]
    self.spawn()
    self.spawn()

    #棋盘走一步，通过对矩阵进行转置与逆转，可以直接从左移得到其他三个方向的移动操作
def move(self,direction):
    def move_row_left(row): #一行向左合并，定义在move中
        def tighten(row): #把零散的非零单元挤到一块
            new_row = [i for i in row if i!=0]
            new_row += [0 for i in range(len(row)-len(new_row))]
            return new_row
        def merge(row): #对邻近元素进行合并
            pair = False
            new_row =[]
            for i in range(len(row)):
                if pair:
                    new_row.append(2*row[i])
                    self.score+=2*row[i]
                    pair = False
                else:
                    if i+1<len(row) and row[i]==row[i+1]:
                        pair = True
                        new_row.append(0)
                    else:
                        new_row.append(row[i])
            assert len(new_row) == len(row)
            return new_row
        #先挤到一块再合并再挤到一块
        return tighten(merge(tighten(row)))
    moves = {}
    moves['Left'] = lambda field:[move_row_left(row) for row in field]
    moves['Right'] = lambda field:invert(moves['Left'](invert(field)))
    moves['Up'] = lambda field:transpose(moves['Left'](transpose(field)))
    moves['Down'] = lambda field:transpose(moves['Right'](transpose(field)))

    if direction in moves:
        if self.move_is_possible(direction):
            self.field = moves[direction](self.field)
            self.spawn
            return True
        else:
            return False

#判断输赢
def is_win(self):
    return any(any(i>=self.win_value for i in row) for row in self.field)
def is_gameover(self):
    return not any(self.move_is_possible for move in actions)

#判断是否移动
def move_is_possible(self,direction):
    def row_is_left_movable(row):
        def change(i):
            if row[i] == 0 and row[i+1]!=0: #可以移动
                return True
            if row[i]!=0 and row[i+1]==row[i]: #可以合并
                return True
            return False
        return any(change(i) for i in range(len(row)-1))

    check = {}
    check['Left'] = lambda field:any(row_is_left_movable(row) for row in field)
    check['Right'] = lambda field:check['Left'](invert(field))
    check['Up'] = lambda field:check['Left'](transpose(field))
    check['Down']=lambda field:check['Right'](transpose(field))

    if direction in check:
        return check[direction](self.field)
    else:
        return False


