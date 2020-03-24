# coding=utf-8

##10.1  10.2
# filenames = "learning_python.txt"

# with open(filenames) as file_object:
#     lines = file_object.read()
#     print(lines.strip())

# with open(filenames) as file:
#     for line in file:
#         print(line.strip())

# with open(filenames) as filename:
#     lines = filename.readlines()
#
# for line in lines:
#     line = line.replace('Python','C')
#     print(line.strip())

##10.3
# use_name = input("请输入您的用户名：")
# with open('guest.txt','a') as names:
#     names.write(use_name)

##10.4

# while True:
#
#     activate = input("如果您想退出该程序请输入q：")
#     if activate == 'q':
#         break
#     else:
#         use_name = input("请输入您的用户名：")
#         print("您好：" + use_name)
#         with open('guest_book.txt','a') as guest_book:
#             guest_book.write(use_name + '\n')

##10.5

# while True:
#
#     activate = input("如果您想退出该程序请输入q：")
#     if activate == 'q':
#         print("感谢您参与此调查！")
#         break
#     else:
#         use_name = input("请输入您喜欢编程的原因：")
#         with open('reason.txt','a') as guest_book:
#             guest_book.write(use_name + '\n')
#
#
# filename = 'programming_poll.txt'
#
# responses = []
# while True:
#     response = input("\nWhy do you like programming? ")
#     responses.append(response)
#
#     continue_poll = input("Would you like to let someone else respond? (y/n) ")
#     if continue_poll != 'y':
#         break
#
# with open(filename, 'a') as f:
#     for response in responses:
#         f.write(response + "\n")

##10.6  10.7
# while True:
#   try:
#       num_1 = input("请输入第一个数字：")
#       num_1 = int(num_1)
#       num_2 = input("请输入第二个数字：")
#       num_2 = int(num_2)
#   except ValueError:
#       print("Sorry, I really needed a number.")
#
#   else:
#      num = num_1 + num_2
#      print(num)

##10.8 10.9

# def read_fdilename(filename):
#     """"读取文件并显示"""
#     try:
#         with open(filename) as file:
#             file = file.read().rstrip()
#             print(file)
#     except FileNotFoundError:
#         #print("对不起，您访问的文件不存在")
#         pass
#
#
# cats_filename = 'cats.txt'
# dogs_filename = 'dogs.txt'
# read_fdilename(cats_filename)
# read_fdilename(dogs_filename)

##10.10

# filename = "THE_GOLDEN_BIRD.txt"
# with open(filename,'r',encoding='UTF-8') as f_obj:
#     file = f_obj.read()
#
# print(file.lower().count('the'))

##10.11
# import json
#
# filename = 'number.json'
# number = input("请输入您喜欢的数字：")

# with open(filename,'w') as file:
#     json.dump(number,file)

# with open(filename) as file:
#     number = json.load(file)
#
# print("我知道您最喜欢的数字是：" + number)

##10.12

# import json
#
# filename = "number.json"
# try:
#     with open(filename) as f_obj:
#         number = json.load(f_obj)
#
# except FileNotFoundError:
#     number = input("请输入您最喜欢的数字：")
#     with open(filename,'w') as f_obj:
#         json.dump(number,f_obj)
# else:
#     print("我知道您最喜欢的数字是：" + number)

##10.13

import json

def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = "username.json"
    try:
        with open(filename) as f_obj:
            usename = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return usename

def get_new_username(name):
    """提示用户输入用户名"""
    #username = input("What is your name? ")
    username = name
    filename = 'username.json'
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)

    return username

# def greet_user():
#     """问候用户，并指出其名字"""
#     username = get_stored_username()
#     if username:
#         correct = input("Are you " + username + "? (y/n) ")
#         if correct == 'y':
#             print("Welcome back, " + username + "!")
#         else:
#             username = get_new_username()
#             print("We'll remember you when you come back, " + username + "!")
#     else:
#         username = get_new_username()
#         print("We'll remember you when you come back " + username + "!")
# greet_user()

def greet_use():
    """验证用户名是否在文件中"""
    input_use = input("请输入您的用户名：")
    username = get_stored_username()
    if input_use in username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username(input_use)
        print("We'll remember you when you come back " + username + "!")

greet_use()
