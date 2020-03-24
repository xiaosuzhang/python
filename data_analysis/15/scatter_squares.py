# coding=utf-8
import matplotlib.pyplot as plt

x_valuse = list(range(1,1001))
y_value = [x**2 for x in x_valuse]

#plt.scatter(x_valuse, y_value, c='red', edgecolor='none', s=40)
#颜色映射
plt.scatter(x_valuse, y_value, c=y_value, cmap=plt.cm.Blues, edgecolor='none', s=40)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#设置每个坐标轴的取值范围（分别为x,y的最小值和最大值）
plt.axis([0, 1100, 0, 1100000])

plt.tick_params(axis='both',which='major', labelsize=14)
#plt.show()
#保存图片，第一个参数为图片名，第二个参数指定将图表多余的空白区域剪裁掉
plt.savefig('Square_plot.png', bbox_inches='tight')