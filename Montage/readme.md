### Montage ###
    description: 实战2. Python实现蒙太奇马赛克拼图，运行时下载的图集太大了，删除了大部分，运行如果发现用于生成效果的图片不够，
    可以运行爬虫脚本自行爬取。

- 依赖：
    + Python运行环境: Python3；
    + 安装pillow库，pip install pillow；
    + 安装argparse库，pip install argparse；
- 运行：
    + 抓取图片素材：python spider_pictures.py 
    + 选择合适的目标图片，确认图片路径；
    + python mosaic.py -i ttt.jpg -d trump/ -o output/ -r 100

    
- 运行效果：
    + 目标图：
        ![image](https://github.com/beiliangshizi/Python_In_Action/blob/master/Montage/ttt.jpg)
    + 效果图：
        ![image](https://github.com/beiliangshizi/Python_In_Action/blob/master/Montage/a.jpg)
        ![image](https://github.com/beiliangshizi/Python_In_Action/blob/master/Montage/b.jpg)