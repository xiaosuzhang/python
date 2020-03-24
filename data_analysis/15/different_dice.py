# coding=utf-8

from die import Die
import  pygal

#创建一个D6和D10
die_1 = Die()
die_2 = Die(10)

results = []

for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result + 1):
    frequence = results.count(value)
    frequencies.append(frequence)

hist = pygal.Bar()

hist.title = "Result of rolling a D6 and a D10 50,000 times."
hist.x_labels = [str(x+1) for x in range(1,max_result)]
hist.x_title = 'Results'
hist.y_title = "Frequency of Result"

hist.add('D6 + D10',frequencies)
hist.render_to_file('different_dice_1_visual.svg')