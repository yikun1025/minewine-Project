def log(*args):
    print(*args)

import turtle

turtle.tracer(10000, 0.001)

t = turtle.Turtle()

def setpen(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)

def goto(x, y):
    t.goto(x, y)

def rect_lb(x, y, w, h, color):
    setpen(x, y)
    t.pencolor(color)
    t.fillcolor(color)

    t.begin_fill()
    goto(x, y + h)
    goto(x + w, y + h)
    goto(x + w, y)
    goto(x, y)
    t.end_fill()

def square(x, y, size, color):
    rect_lb(x, y, size, size, color)


import random

def random_line_09(n):
    '''
        start end step 都是数字

        和 7.2 一样, 但是要求支持负数 step
        使用 while 循环
        返回一个 list
        假设 start=1, end=5, step=1 返回数据如下
        [1, 2, 3, 4]
        假设 start=6, end=0, step=-1 返回数据如下
        [6, 5, 4, 3, 2, 1]

        :return: list
        '''

    l = []


    while(n > 0):
        a = random.randrange(0, 10, 9)
        l.append(a)
        n -= 1

    log(l)
    return l


def random_square_09(n, limit=3):
    '''
        返回以下格式的数据
        只包含 0 和 9
        limit 是 9 的个数
        假设 n 为 4, 返回的数据格式如下(这是格式范例, 真实数据是随机的)
        注意, 这只是一个 list, 并不是它显示的样子
        注意, 这是一个 list 不是 str
        [
        [0, 9, 0, 0],
        [0, 0, 9, 0],
        [9, 0, 0, 0],
        [0, 0, 0, 0],
        ]
        :param n: int
        :return: 包含了 n 个『只包含 n 个「随机 0 9」的 list』的 list, 9 的个数是 limit
        '''


    l = []
    for i in range(n):
        cnt = 0
        for j in range(n):
            now = random.randrange(0, 10, 9)

            if cnt < limit:
                l.append(now)
                if now == 9:
                    cnt += 1

            else:
                l.append(0)

    new_list = []

    for i in range(n):
        line_list = []
        for j in range(n):
            line_list.append(l[i * n + j])
        new_list.append(line_list)



    return new_list

def add_square(array):
    n = len(array)
    m = len(array[0])

    new_array = []
    for i in range(n):
        log(array[i])

    log('\n')


    for i in range(n + 2):
        new_list = []

        for j in range(m + 2):
            if i == 0 or i == n + 1:
                new_list.append(0)

            elif j == 0 and i != 0 and i != n + 1:
                new_list.append(0)

            elif j == m + 1 and i != 0 and i != n + 1:
                new_list.append(0)

            elif i != 0 and i != n + 1 and j != 0 and j != m + 1:
                new_list.append(array[i - 1][j - 1])

        new_array.append(new_list)
        log(new_list)


    return new_array

def marked_square(array):

    array = add_square(array)

    n = len(array)
    log('\n')

    for i in range(n - 2):
        i += 1
        m = len(array[i])

        for j in range(m - 2):
            j += 1
            cnt = 0
            #log(i, j)

            if(array[i][j] != 9):
                if array[i - 1][j - 1] == 9:
                    cnt += 1
                if array[i - 1][j] == 9:
                    cnt += 1
                if array[i - 1][j + 1] == 9:
                    cnt += 1
                if array[i][j - 1] == 9:
                    cnt += 1
                if array[i][j + 1] == 9:
                    cnt += 1
                if array[i + 1][j - 1] == 9:
                    cnt += 1
                if array[i + 1][j] == 9:
                    cnt += 1
                if array[i + 1][j + 1] == 9:
                    cnt += 1


                array[i][j] = cnt
            #log(cnt)


    for i in range(len(array)):
        log(array[i])

    return array


def update_square(array):
    array = marked_square(array)
    new_array = []
    log('\n')

    for i in range(len(array) - 2):
        new_list = []
        i += 1
        for j in range(len(array[i]) - 2):
            j += 1
            new_list.append(array[i][j])

        new_array.append(new_list)

    for i in range(len(new_array)):
        log(new_array[i])

    return new_array

random_list = update_square(random_square_09(7, 2))

dict_1 = ['000000010000000',
          '000000110000000',
          '000001010000000',
          '000010010000000',
          '000100010000000',
          '001000010000000',
          '000000010000000',
          '000000010000000',
          '000000010000000',
          '000000010000000',
          '000000010000000',
          '000000010000000',
          '000000010000000',
          '000000010000000',
          '001111111111100']

dict_2 = ['001111111111100',
          '000000000000100',
          '000000000000100',
          '000000000000100',
          '000000000000100',
          '000000000000100',
          '000000000000100',
          '001111111111100',
          '001000000000000',
          '001000000000000',
          '001000000000000',
          '001000000000000',
          '001000000000000',
          '001000000000000',
          '001111111111100']

dict_3 = ['001111111111100',
          '000000000000100',
          '000000000000100',
          '000000000000100',
          '000000000000100',
          '000000000000100',
          '000000000000100',
          '001111111111100',
          '000000000000100',
          '000000000000100',
          '000000000000100',
          '000000000000100',
          '000000000000100',
          '000000000000100',
          '001111111111100']

dict_4 = ['00100000000100',
          '00100000000100',
          '00100000000100',
          '00100000000100',
          '00100000000100',
          '00100000000100',
          '00100000000100',
          '00111111111100',
          '00000000000100',
          '00000000000100',
          '00000000000100',
          '00000000000100',
          '00000000000100',
          '00000000000100',
          '00000000000100']

dict_5 = ['00111111111100',
          '00100000000000',
          '00100000000000',
          '00100000000000',
          '00100000000000',
          '00100000000000',
          '00100000000000',
          '00111111111100',
          '00000000000100',
          '00000000000100',
          '00000000000100',
          '00000000000100',
          '00000000000100',
          '00000000000100',
          '00111111111100']


dict_6 = ['00111111111100',
          '00100000000000',
          '00100000000000',
          '00100000000000',
          '00100000000000',
          '00100000000000',
          '00100000000000',
          '00111111111100',
          '00100000000100',
          '00100000000100',
          '00100000000100',
          '00100000000100',
          '00100000000100',
          '00100000000100',
          '00111111111100']

dict_7 = ['01111111111000',
          '00000000001000',
          '00000000001000',
          '00000000001000',
          '00000000001000',
          '00000000001000',
          '00000000001000',
          '00000000001000',
          '00000000001000',
          '00000000001000',
          '00000000001000',
          '00000000001000',
          '00000000001000',
          '00000000001000',
          '00000000001000']

dict_8 = ['001111111111000',
          '001000000001000',
          '001000000001000',
          '001000000001000',
          '001000000001000',
          '001000000001000',
          '001000000001000',
          '001111111111000',
          '001000000001000',
          '001000000001000',
          '001000000001000',
          '001000000001000',
          '001000000001000',
          '001000000001000',
          '001111111111000']

dict_9 = ['000000000000000',
          '000000001110000',
          '000000111000000',
          '000001100000000',
          '000011100000000',
          '001111111111000',
          '001111111111000',
          '011111111111100',
          '011111111111100',
          '011111111111000',
          '001111111111000',
          '000111111110000',
          '000111111100000',
          '000000000000000',
          '000000000000000']


def draw_pixel(x, y, pixel, size = 3):
    '''
    pixel 是一个 像素值
    像素值是只有一个字符的 str
    如果是 '0' 则画一个白色否则画黑色

	以坐标 x y 为矩形左上角顶点画一个边长为 size 的正方形

    :return: None
    '''

    t.hideturtle()
    if pixel == '0':
        color = 'white'
    else:
        color = 'black'
        square(x, y, size, color)

def draw_line(x, y, pixels, size = 3):
    '''
    pixels 是一个包含了像素值的 list

	以坐标 x y 为左上角顶点画一排边长为 size 的正方形

    :return: None
    '''

    for i in range(len(pixels)):
        s = str(pixels[i])
        new_x = x + i * size
        draw_pixel(new_x, y, s, size)

def draw_block(x, y, block, size = 3):
    '''
    block 是一个包含了 pixels list 的 list
	(也就是一个像素方阵)

	以坐标 x y 为左上角顶点画一个边长为 size 的正方形方阵

    :return: None
    '''

    for i in range(len(block)):
        new_y = -size * i + y
        draw_line(x, new_y, block[i], size)

def draw_mine_map(x, y, map, size = 2.1):
    col = len(map)
    for i in range(col):
        array_col = map[i]
        new_y = y - i * 22 * size

        for j in range(len(array_col)):
            new_x = j * 22 * size + x

            if array_col[j] == 0:
                square(new_x - 7, new_y - 31, 38, '#CBC7C7')

            if array_col[j] == 1:
                draw_block(new_x, new_y, dict_1, size)

            if array_col[j] == 2:
                draw_block(new_x, new_y, dict_2, size)

            if array_col[j] == 3:
                draw_block(new_x, new_y, dict_3, size)

            if array_col[j] == 4:
                draw_block(new_x, new_y, dict_4, size)

            if array_col[j] == 5:
                draw_block(new_x, new_y, dict_5, size)

            if array_col[j] == 6:
                draw_block(new_x, new_y, dict_6, size)

            if array_col[j] == 7:
                draw_block(new_x, new_y, dict_7, size)

            if array_col[j] == 8:
                draw_block(new_x, new_y, dict_8, size)

            if array_col[j] == 9:
                draw_block(new_x, new_y, dict_9, size)

def draw_block_map(x, y, map,size = 2):
    col = len(map)

    for i in range(col):
        new_y = y - i * 23 * size
        for j in range(len(map[i])):
            new_x = x + j * 23 * size
            square(new_x, new_y, size * 22, '#B5AFAF')
            rect_lb(new_x, new_y, 2, size * 21, 'black')
            rect_lb(new_x, new_y, size * 21 , 2, 'black')

def click(*args):
    print('click')
    print(args)

    x, y = args
    map = random_list

    n = len(map)
    mine_point = []
    dict_1_point = []
    dict_2_point = []
    dict_3_point = []
    dict_4_point = []
    dict_5_point = []
    dict_6_point = []
    dict_7_point = []
    dict_8_point = []
    dict_0_point = []

    for i in range(n):
        new_y = 100 - 46 * i
        m = len(map[i])
        for j in range(m):
            new_x = -150 + 46 * j

            if map[i][j] == 9:
                mine_point.append((new_x, new_y))

            if map[i][j] == 1:
                dict_1_point.append((new_x, new_y))

            if map[i][j] == 2:
                dict_2_point.append((new_x, new_y))

            if map[i][j] == 3:
                dict_3_point.append((new_x, new_y))

            if map[i][j] == 4:
                dict_4_point.append((new_x, new_y))

            if map[i][j] == 5:
                dict_5_point.append((new_x, new_y))

            if map[i][j] == 6:
                dict_6_point.append((new_x, new_y))

            if map[i][j] == 7:
                dict_7_point.append((new_x, new_y))

            if map[i][j] == 8:
                dict_8_point.append((new_x, new_y))

            if map[i][j] == 0:
                dict_0_point.append((new_x, new_y))


    for i in range(len(dict_1_point)):
        new_x, new_y = dict_1_point[i]

        if new_x + 2 <= x <= new_x + 44 and new_y + 2 <= y <= new_y + 44:
            draw_block(new_x + 10, new_y + 36, dict_1, size = 2.1)

    for i in range(len(dict_2_point)):
        new_x, new_y = dict_2_point[i]

        if new_x + 2 <= x <= new_x + 44 and new_y + 2 <= y <= new_y + 44:
            draw_block(new_x + 10, new_y + 36, dict_2, size = 2.1)

    for i in range(len(dict_3_point)):
        new_x, new_y = dict_3_point[i]

        if new_x + 2 <= x <= new_x + 44 and new_y + 2 <= y <= new_y + 44:
            draw_block(new_x + 10, new_y + 36, dict_3, size = 2.1)

    for i in range(len(dict_4_point)):
        new_x, new_y = dict_4_point[i]

        if new_x + 2 <= x <= new_x + 44 and new_y + 2 <= y <= new_y + 44:
            draw_block(new_x + 10, new_y + 36, dict_4, size = 2.1)

    for i in range(len(dict_5_point)):
        new_x, new_y = dict_5_point[i]

        if new_x + 2 <= x <= new_x + 44 and new_y + 2 <= y <= new_y + 44:
            draw_block(new_x + 10, new_y + 36, dict_5, size = 2.1)

    for i in range(len(dict_6_point)):
        new_x, new_y = dict_6_point[i]

        if new_x + 2 <= x <= new_x + 44 and new_y + 2 <= y <= new_y + 44:
            draw_block(new_x + 10, new_y + 36, dict_6, size = 2.1)

    for i in range(len(dict_7_point)):
        new_x, new_y = dict_7_point[i]

        if new_x + 2 <= x <= new_x + 44 and new_y + 2 <= y <= new_y + 44:
            draw_block(new_x + 10, new_y + 36, dict_7, size = 2.1)

    for i in range(len(dict_8_point)):
        new_x, new_y = dict_8_point[i]

        if new_x + 2 <= x <= new_x + 44 and new_y + 2 <= y <= new_y + 44:
            draw_block(new_x + 10, new_y + 36, dict_8, size = 2.1)

    for i in range(len(dict_0_point)):
        new_x, new_y = dict_0_point[i]

        if new_x + 2 <= x <= new_x + 44 and new_y + 2 <= y <= new_y + 44:
            square(new_x + 3, new_y + 2, 42, '#CBC7C7')

    for i in range(len(mine_point)):
        new_x, new_y = mine_point[i]

        if new_x + 2 <= x <= new_x + 44 and new_y + 2 <= y <= new_y + 44:
            draw_mine_map(-140, 136, map)





    print(mine_point)
    #print(new_x, new_y)


def main():
    draw_block_map(-150, 100, random_list)
    turtle.onscreenclick(click)
    turtle.update()


# draw_char(char_8)

turtle.listen()

main()

# onscreenclick 是配置一个函数, 你点击屏幕的时候调用


turtle.update()
turtle.done()
