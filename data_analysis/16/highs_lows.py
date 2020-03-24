#coding=utf-8
# import csv
# from datetime import datetime
# from matplotlib import pyplot as plt
#
# filename = 'sitka_weather_2014.csv'
#
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_now = next(reader)
#
#     dates, highs, lows  = [], [], []
#     for row in reader:
#         current_date = datetime.strptime(row[0],"%Y-%m-%d")
#         dates.append(current_date)
#         high = int(row[1])
#         highs.append(high)
#         low = int(row[3])
#         lows.append(low)
#
#
# fig = plt.figure(dpi=128, figsize=(10, 6))
# plt.plot(dates, highs, c= 'red', alpha = 0.5)
# plt.plot(dates, lows, c = 'blue',alpha = 0.5)
# plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# plt.title("Daily high and low temperatures - 2014", fontsize=24)
# plt.xlabel('',fontsize=16)
# fig.autofmt_xdate()
# plt.ylabel("Temperature(F)",fontsize=16)
# plt.tick_params(axis='both',which='major',labelsize=16)
# plt.ylim(10,120)
#
# plt.show()


import csv
from matplotlib import pyplot as plt
from datetime import datetime



filename = 'death_valley_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, "missing date")

        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates, highs, c = 'red', alpha=0.5)
plt.plot(dates, lows, c='blue',alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue',alpha=0.1)
title = "Daily high and low temptures - 2014\nDeath Valley,CA"
plt.title(title,fontsize=20)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)",fontsize=16)
plt.tick_params(axis='both', which='major',labelsize=16)

plt.show()



