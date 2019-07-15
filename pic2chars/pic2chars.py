#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:beiliangshizi - huangjunjie3@jd.com
# datetime:2019/6/21 10:02

from PIL import Image    # PIL 是Python 图像处理库pillow
import argparse             # argparse是Python接受输入参数的库

# 命令行输入参数处理
parser = argparse.ArgumentParser()
parser.add_argument('file')                   # 输入文件
parser.add_argument('-o', '--output')   # 输出文件
# 输出字符画宽，默认值为80
parser.add_argument('--width', type = int, default = 80)
# 输出字符画高，默认值为80
parser.add_argument('--height', type = int, default = 80)

# 获取参数
args = parser.parse_args()
IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

# 我们的字符画所使用的字符集，一共有 70 个字符
ascii_char = list("$@B%8&amp;WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~&lt;>i!lI;:,\"^`'. ")


# 将256灰度映射到列表的70个字符上
def get_char(r,g,b,alpha = 256):

    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1)/length

    return ascii_char[int(gray/unit)]




if __name__ == '__main__':

    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)
    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'
    print(txt)

    # 字符画输出到文件
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)
