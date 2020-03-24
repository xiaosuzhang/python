# coding=utf-8
import json
import pygal_maps_world.maps
from pygal.style import RotateStyle
from country_codes import get_country_code

#将数据加载到一个列表中

filename = 'population_data.json'

with open(filename) as f:
    pop_data = json.load(f)

#创建一个包含人口数量的字典
cc_population = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_population[code] = population


#根据人口数量将所有的国家分成三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pp in cc_population.items():
    if pp < 10000000:
        cc_pops_1[cc] = pp
    elif pp < 1000000000:
        cc_pops_2[cc] = pp
    else:
        cc_pops_3[cc] = pp



wm_style = RotateStyle('#336699')
wm = pygal_maps_world.maps.World(style=wm_style)
wm.title = "World Population in 2010, by country"
wm.add('0-10m',cc_pops_1)
wm.add('10m-10bn',cc_pops_2)
wm.add(">10bn",cc_pops_3)

wm.render_to_file('world_population.svg')