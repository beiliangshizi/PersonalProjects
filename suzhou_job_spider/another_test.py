#coding=utf-8
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import sys
from snownlp import SnowNLP
hktk='今天我寒夜里看雪飘过 怀著冷却了的心窝飘远方 风雨里追赶 雾里分不清影踪 天空海阔你与我 可会变(谁没在变) 多少次迎著冷眼与嘲笑 从没有放弃过心中的理想 一刹那恍惚 若有所失的感觉 不知不觉已变淡 心里爱(谁明白我) 原谅我这一生不羁放纵爱自由 也会怕有一天会跌倒 被弃了理想谁人都可以 那会怕有一天只你共我 今天我寒夜里看雪飘过 怀著冷却了的心窝飘远方 风雨里追赶 雾里分不清影踪 天空海阔你与我 可会变(谁没在变) 原谅我这一生不羁放纵爱自由 也会怕有一天会跌倒 被弃了理想谁人都可以 那会怕有一天只你共我 仍然自由自我 永远高唱我歌 走遍千里 原谅我这一生不羁放纵爱自由 也会怕有一天会跌倒 被弃了理想谁人都可以 那会怕有一天只你共我 被弃了理想谁人都可以 那会怕有一天只你共我 原谅我这一生不羁放纵爱自由 也会怕有一天会跌倒 被弃了理想谁人都可以 那会怕有一天只你共我'
hktk1=hktk.replace(' ','，')
#print hktk1
hktk=hktk1.decode('utf-8')
song=SnowNLP(hktk)

key=' '.join(song.keywords(30))
my_wordcloud = WordCloud().generate(key)

plt.imshow(my_wordcloud)

plt.axis('off')
plt.show()