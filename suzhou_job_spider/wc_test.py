#coding:utf-8
author = 'beiliangshizi'
#date:2017-05-23
#note:this module is used by python2.7


import matplotlib.pyplot as plt
from os import path
import codecs
from scipy.misc import imread
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator

d = path.dirname(__file__)

text = codecs.open(path.join(d, 'output.txt'),'r',encoding='utf-8').read()


# 设置背景图片
back_coloring = imread(path.join(d, "./t.png"))

wc = WordCloud(font_path='./hanyihuochai.ttf',  # 设置字体
               background_color="white",  # 背景颜色
               max_words=2000,  # 词云显示的最大词数
               mask=back_coloring,  # 设置背景图片
               max_font_size=100,  # 字体最大值
               random_state=42,
               )
# 生成词云, 可以用generate输入全部文本(中文不好分词),也可以我们计算好词频后使用generate_from_frequencies函数
wc.generate(text)
# wc.generate_from_frequencies(txt_freq)
# txt_freq例子为[('词a', 100),('词b', 90),('词c', 80)]
# 从背景图片生成颜色值
image_colors = ImageColorGenerator(back_coloring)

plt.figure()
# 以下代码显示图片
plt.imshow(wc)
plt.axis("off")
plt.show()
# 绘制词云

# 保存图片
wc.to_file(path.join(d, "result_pic.png"))
































