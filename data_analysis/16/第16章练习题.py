# coding=utf-8
"""16-2"""
# import csv
# from matplotlib import pyplot as plt
# from datetime import datetime
#
# def read_weather(filename,dates,highs,lows):
#
#     with open(filename) as f:
#         reader = csv.reader(f)
#         header = next(reader)
#
#         for row in reader:
#             try:
#                 current_date = datetime.strptime(row[0],"%Y-%m-%d")
#                 high = int(row[1])
#                 low = int(row[3])
#             except ValueError:
#                 print(current_date,"missing data")
#             else:
#                 dates.append(current_date)
#                 highs.append(high)
#                 lows.append(low)
#
# dates_1, highs_1, lows_1 = [], [], []
# read_weather('sitka_weather_2014.csv',dates_1,highs_1,lows_1)
# fig = plt.figure(dpi=128,figsize=(10,6))
# plt.plot(dates_1, highs_1, c='red', alpha=0.6)
# plt.plot(dates_1, lows_1, c='blue', alpha=0.6)
# plt.fill_between(dates_1, highs_1, lows_1, facecolor='blue', alpha=0.15)
#
# dates_2, highs_2, lows_2 = [], [], []
# read_weather('death_valley_2014.csv',dates_2,highs_2,lows_2)
# plt.plot(dates_2, highs_2, c='red', alpha=0.6)
# plt.plot(dates_2, lows_2, c='blue', alpha=0.6)
# plt.fill_between(dates_2, highs_2, lows_2, facecolor='blue', alpha=0.15)
#
# title = "Daily high and low temperatures - 2014"
# title += "\nSitka, AK and Death Valley, CA"
# plt.title(title,fontsize=20)
# plt.xlabel('',fontsize=16)
# fig.autofmt_xdate()
# plt.ylabel("Temperature(F)",fontsize=16)
# plt.tick_params(axis='both', which='major',labelsize=16)
# plt.ylim(10,120)
#
# plt.show()


"""16-3"""

# import csv
# from datetime import datetime
# from matplotlib import pyplot as plt
#
# filename = 'sitka_rainfall_2015.csv'
#
# with open(filename) as f:
#     reader = csv.reader(f)
#     header = next(reader)
#
#     dates, rainfalls = [], []
#     for row in reader:
#         try:
#             current_date = datetime.strptime(row[0], "%Y-%m-%d")
#             rainfall = float(row[19])
#         except ValueError:
#             print(current_date,'Missing data')
#         else:
#             dates.append(current_date)
#             rainfalls.append(rainfall)
#
# fig = plt.figure(dpi=128,figsize=(10,6))
# plt.plot(dates, rainfalls, c='blue', alpha=0.5)
# plt.fill_between(dates, rainfalls, facecolor='blue', alpha=0.2)
# title = "Daily rainfall amounts - 2015\nSitka, AK"
# plt.title(title,fontsize=20)
# plt.xlabel("",fontsize=14)
# fig.autofmt_xdate()
# plt.ylabel("RainFall",fontsize=14)
# plt.tick_params(axis='both',which='major',labelsize=14)
# plt.show()

"""16-6"""

import json


filename = 'global_gdp.json'
from country_codes import get_country_code
from pygal_maps_world.maps import World
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

with open(filename) as f:
    gdp_data = json.load(f)

cc_gdp = {}
for gdp_dict in gdp_data:
    if gdp_dict["Year"] == 2014:
        country = gdp_dict['Country Name']
        gdp = int(float(gdp_dict['Value']))
        code = get_country_code(country)
        if code:
            cc_gdp[code] = gdp

cc_gdp_1, cc_gdp_2, cc_gdp_3 = {}, {}, {}

for cc,gdp in cc_gdp.items():
    if gdp < 5000000000:
        cc_gdp_1[cc] = round(gdp / 1000000000)
    elif gdp < 50000000000:
        cc_gdp_2[cc] = round(gdp / 1000000000)
    else:
        cc_gdp_3[cc] = round(gdp / 1000000000)

wm_style = RS('#336699', base_style=LCS)
wm = World(wm_style = wm_style)
wm.title ='Global GDP in 2014, by Country (in billions USD)'
wm.add("0-5bn",cc_gdp_1)
wm.add("5bn-50bn",cc_gdp_2)
wm.add(">50bn",cc_gdp_3)

wm.render_to_file('global_gdp.svg')