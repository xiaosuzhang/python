# coding=utf-8
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS("#336699",base_style=LCS)
chart = pygal.Bar(style=my_style,x_label_rotation=45, show_legend=False)

chart.title = "Python Project"
chart.x_labels = ['system-design-prime', 'django', 'flask']

plot_dicts = [
    {'value': 85703, 'label':"Description of system-design-prime"},
    {'value': 49505, 'label':"Description of flask"},
    {'value': 45002, 'label':"Description of django"},
]

chart.add('',plot_dicts)
chart.render_to_file('bar_descriptions.svg')