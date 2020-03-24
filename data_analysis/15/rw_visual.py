# coding=utf-8

import matplotlib.pyplot as plt

from random_walk import RandomWalk

#创建一个RandomWalk实例，并将其包含的店都绘制出来

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    #设置绘制窗口的尺寸
    plt.figure(dpi=128, figsize=(10,6))

    point_number = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_number, cmap=plt.cm.Blues,s=1)

    #突出起点和终点
    plt.scatter(0,0,c='green',edgecolor='none',s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_walking = input("Make another walk? (y/n): ")
    if keep_walking == 'n':
        break