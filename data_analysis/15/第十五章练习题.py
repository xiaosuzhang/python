# coding=utf-8
"""15-1、15-2"""

# import matplotlib.pyplot as plt
#
# x_value = list(range(1,5001))
# y_value = [x**3 for x in x_value]
# plt.scatter(x_value, y_value, c=y_value,cmap=plt.cm.Reds,edgecolors='none', s=40)
# plt.title("Cubes", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Cube of Value",fontsize=14)
# plt.tick_params(axis='both', which='major', labelsize=14)
# plt.axis([0,5100,0,5100**3])
# plt.show()


"""15-3"""

# import matplotlib.pyplot as plt
#
# from random_walk import RandomWalk
#
# while True:
#
#     rw = RandomWalk(5000)
#     rw.fill_walk()
#
#     plt.figure(dpi=128, figsize=(10, 6))
#
#     plt.plot(rw.x_values, rw.y_values, linewidth=1, zorder=1)
#
#     plt.scatter(0, 0, c='green', edgecolors='none', s=100)
#     plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
#
#     plt.axes().get_xaxis().set_visible(False)
#     plt.axes().get_yaxis().set_visible(False)
#     plt.show()
#
#     keep_walking = input("Make another walk?(y/n): ")
#     if keep_walking == 'n':
#         break


"""15-6"""

# coding=utf-8
#
# from die import Die
# import  pygal
#
# #创建一个D6和D10
# die_1 = Die()
# die_2 = Die(10)
#
# results = []
#
# for roll_num in range(50000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)
#
# frequencies = []
# max_result = die_1.num_sides + die_2.num_sides
#
# for value in range(2, max_result + 1):
#     frequence = results.count(value)
#     frequencies.append(frequence)
#
# hist = pygal.Bar()
#
# hist.title = "Result of rolling a D6 and a D10 50,000 times."
# hist.x_labels = [str(x+1) for x in range(1,max_result)]
# hist.x_title = 'Results'
# hist.y_title = "Frequency of Result"
#
# hist.add('D6 + D10',frequencies)
# hist.render_to_file('different_dice_1_visual.svg')

"""15-7"""
#
# from die import Die
# import pygal
#
# die_1 = Die(8)
# die_2 = Die(8)
#
# results = []
# for roll_num in range(1000000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)
#
# frequencies = []
# max_results = die_1.num_sides + die_2.num_sides
#
# for value in range(2, max_results + 1):
#     frequency = results.count(value)
#     frequencies.append(frequency)
#
# hist = pygal.Bar()
# hist.title = "Results of rolling two D8 dice 1,000,000 times."
# hist.x_labels = [str(x) for x in range(2,max_results+1)]
# hist.x_title = "Result"
# hist.y_title = "Frequency of Result"
#
# hist.add("D8 + D8", frequencies)
# hist.render_to_file("15-7.svg")


"""15-8"""
# from die import Die
# import pygal
#
# die_1 = Die()
# die_2 = Die()
# die_3 = Die()
#
# results = []
# for rull_num in range(10000):
#     result = die_1.roll() + die_2.roll() + die_3.roll()
#     results.append(result)
#
# frequencies = []
# max_results = die_1.num_sides + die_2.num_sides + die_3.num_sides
#
# for value in range(3,max_results + 1):
#     frequency = results.count(value)
#     frequencies.append(frequency)
#
# hist = pygal.Bar()
# hist.title = "Results of rolling three D6 dice 1,000,000 times."
# hist.x_labels = [str(x) for x in range(3,max_results + 1)]
# hist.x_title = "Results"
# hist.y_title = "Frequency of Result"
#
# hist.add("D6 + D6 + D6", frequencies)
# hist.render_to_file("15-8_results.svg")


"""15-9"""
from die import Die
import pygal

die_1 = Die()
die_2 = Die()

results = []
for rull_num in range(100000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

frequencies = []
max_results = die_1.num_sides * die_2.num_sides
for value in range(1,max_results + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Results of multiplying two D6 dice. (1,000,000 rolls)"

hist.x_labels = [str(x) for x in range(1,max_results+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 * D6', frequencies)
hist.render_to_file('dice_visual.svg')

