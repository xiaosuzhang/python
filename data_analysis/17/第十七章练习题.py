# coding=utf-8
"""17-1"""
# import requests
# import pygal
# from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
#
# url = 'https://api.github.com/search/repositories?q=language:Java&sort=stars'
# r = requests.get(url)
# print("Status code: ",r.status_code)
# response_dict = r.json()
# repo_dicts = response_dict['items']
#
# names, plot_dicts = [], []
# for repo_dict in repo_dicts:
#     names.append(repo_dict['name'])
#
#     description = repo_dict['description']
#     if not description:
#         description = 'No description provided'
#     else:
#         plot_dict = {
#             'value': repo_dict['stargazers_count'],
#             'label': description,
#             'xlink': repo_dict['html_url'],
#         }
#
#     plot_dicts.append(plot_dict)
#
# my_style = LS('#333366', base_style=LCS)
# my_style.title_font_size = 24
# my_style.label_font_size = 14
# my_style.major_label_font_size = 18
#
# my_config = pygal.Config()
# my_config.x_label_rotation = 45
# my_config.show_legend = False
# my_config.truncate_label = 15
# my_config.show_y_guides = False
# my_config.width = 1000
#
# chart = pygal.Bar(my_config, style=my_style)
# chart.title = 'Most-Starred Java Projects on GitHub'
# chart.x_labels = names
#
# chart.add('', plot_dicts)
# chart.render_to_file('Java_repos.svg')

import requests

from operator import itemgetter

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#执行API调用并存储响应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print('Status code: ', r.status_code)

#处理有关每篇文章的信息
submission_ids = r.json()

submission_dicts = []

for submission_id in submission_ids[:30]:
    #对于每篇文章，都执行一个API调用
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants',0)
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])


titles, plot_submissions = [], []
for submission_dict in submission_dicts:
    titles.append(submission_dict['title'])

    plot_submission = {
        'value': submission_dict['comments'],
        'xlink': submission_dict['link'],
    }

    plot_submissions.append(plot_submission)



my_style = LS('#333366', base_style=LCS)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
my_config.y_title = 'Number of Comments'

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most Active Discussions on Hacker News'
chart.x_labels = titles

chart.add('', plot_submissions)
chart.render_to_file('hn_submission.svg')
