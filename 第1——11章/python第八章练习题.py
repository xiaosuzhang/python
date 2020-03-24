# coding=utf-8
#8.1
# def display_name():
#     print("What do you learn in this chapter?")
#
# display_name()

##8.2

# def favorite_book(title):
#     """Display message about someone's favorite book."""
#     print("One of my favorite books is " + title + ".")
#
# favorite_book("Alice in Wonderland")

##8.3
# def make_shirt(size,message):
#     """Summarize the shirt that's going to be made"""
#     print("I'm going to make a " + size + " T-shirt.")
#     print("这件T恤上印有的字样为：" + message + "\n")
#
# make_shirt("大号","你是大厦。")
# make_shirt(size="xiaohao",message="lichong shi da sha.")


##8.4
# def make_shirt(size='L',message="I love Python"):
#     """Summarize the shirt that's going to be made"""
#     print("I'm going to make a " + size + " T-shirt.")
#     print("这件T恤上印有的字样为：" + message + "\n")
#
# make_shirt()
# make_shirt(size="M")
# make_shirt(size="S",message="你是大厦你怕谁。")

##8.5
# def descripe_city(name,country='China'):
#     """描述城市所属的国家"""
#     print(name.title() + " is in " + country + ".")
#
# descripe_city(name='Beijing')
# descripe_city(name="ShangHai")
# descripe_city(name="NewYork",country="USA")

##8.6
# def city_country(city,country):
#     """次函数用于描述城市和国家之间的对应关系"""
#     relation = city.title() + "," + country.title()
#     return relation
#
# description = city_country(city='shanghai',country='china')
# print(description)
#
# city = city_country('ushuaia', 'argentina')
# print(city)
#
# city = city_country('longyearbyen', 'svalbard')
# print(city)

## 8.7
#
# def make_album(singer,album,number=0):
#     """此函数用于描述歌手与专辑之间的对应关系"""
#     mulic = {
#         "singer" : singer,
#         "album" : album
#     }
#     if number:
#         mulic['number'] = number
#
#     return  mulic
#
# zhuanji_1 = make_album(singer="周杰伦",album="下课后",number=12)
# print(zhuanji_1)
# album = make_album('beethoven', 'ninth symphony')
# print(album)
#
# album = make_album('willie nelson', 'red-headed stranger')
# print(album)

## 8.8
# def make_album(singer,album):
#     """此函数用于描述歌手与专辑之间的对应关系"""
#     mulic = {
#         "singer" : singer,
#         "album" : album
#     }
#
#
#     return  mulic
#
#
# while True:
#     activate = input("如果您想退出该调查，请输入q: ")
#
#     if activate == 'q':
#         break
#     else:
#         artist = input("请输入歌手的姓名：")
#         title = input("请输入该歌手对应专辑的名称: ")
#
#     albums = make_album(singer=artist, album=title)
#     print(albums)

##8.9
# magicians = ['harry houdini', 'david blaine', 'teller']
#
# def show_magicians(name):
#     """打印每个魔术师的名字"""
#     for magician in name:
#         print(magician)
# show_magicians(magicians)


##8.10 8.11
#
# magicians = ['harry houdini', 'david blaine', 'teller']
# rename = []
#
# def make_greate(name,exchange):
#     """修改魔术师的名字"""
#     for magician in name:
#         name = magician + " the Great"
#         exchange.append(name)
#     return exchange
#
#
# def show_magicians(exchanged_name):
#     for names in exchanged_name:
#         print(names)
# rename = make_greate(magicians,rename)
# show_magicians(magicians)
# show_magicians(rename)

##8.12
# def make_sandwich(*toppings):
#     """根据所提供的食材制作sandwich"""
#     print("\nI'll make you a great sandwich:")
#     for item in toppings:
#         print("  ...adding " + item + " to your sandwich.")
#     print("Your sandwich is ready!")
#
# make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
# make_sandwich('turkey', 'apple slices', 'honey mustard')
# make_sandwich('peanut butter', 'strawberry jam')

##8.13

# def build_profile(first_name,last_name,**intorduce):
#     profile = {}
#     profile["fist_name"] = first_name
#     profile["last_name"] = last_name
#     for key,value in intorduce.items():
#         profile[key] = value
#     return  profile
#
# my_profile = build_profile("li","chong",shaxie="chuangshiren")
# print(my_profile)

##8.14

def make_car(zhizaoshang,xinghao,**information):
    cars = {}
    cars["zhizaosahng"] = zhizaoshang
    cars["xinghao"] = xinghao
    for key,value in information.items():
        cars[key] = value
    return cars
car = make_car("subaru","outback",color='blue',two_packages=True)
print(car)