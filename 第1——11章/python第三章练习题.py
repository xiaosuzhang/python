"""习题3-1"""
#将一些朋友的姓名存储在一个列表中，并将其命名为names。一次访问该列表中的每个元素，从而将每个朋友的姓名打印出来

names = ['dasha','ersha','lichong','angle','shazi']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[-1])

"""习题3-2"""
#继续使用3-1中的列表，但不打印每个朋友的姓名，而为每人打印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的名字
names = ['dasha','ersha','lichong','angle','shazi']
message= names[0] + " ! How are you ?"
print(message)
message= names[1] + " ! How are you ?"
print(message)
message= names[2] + " ! How are you ?"
print(message)
message= names[3] + " ! How are you ?"
print(message)
message= names[-1] + " ! How are you ?"
print(message)

"""习题3-3"""
#自己的列表：想想你喜欢的通勤方式，如：骑摩托车或开汽车，并创建一个包含多种通勤方式的列表。根据该列表打印一些类有关这些
# 通勤方式的宣言。
transportation = ['motorcycle','bicycle',"car"]
message = "I would like to own a Honda " + transportation[0]
print(message)
message = "I would like to own a Gaint " + transportation[1]
print(message)
message = "I would like to own a Porsche " + transportation[2]
print(message)

"""习题3-4"""
#嘉宾名单：如果你可以邀请任何一个人共进晚餐，你会邀请哪些人？请创建一个列表，其中包含至少3个你想邀请的人：
# 然后使用这个列表打印消息，邀请这些人来与你共进晚餐
dinner_list = ['Monkey·D·Luffy','Roronoa Zoro','Nami','Usopp']
print("Can you have dinner with me, " + dinner_list[0])
print("Can you have dinner with me, " + dinner_list[1])
print("Can you have dinner with me, " + dinner_list[2])
print("Can you have dinner with me, " + dinner_list[3])

"""习题3-5"""
#修改嘉宾名单：得知某位嘉宾无法赴约，因此你需要邀请另外一名嘉宾
print("\nI am sorry to hear that, " + dinner_list[3] + " cannot have dinner with me!")
dinner_list[3] = 'Nico Robin'
print("\nCan you have dinner with me, " + dinner_list[0]+ "?")
print("Can you have dinner with me, " + dinner_list[1]+ "?")
print("Can you have dinner with me, " + dinner_list[2]+ "?")
print("Can you have dinner with me, " + dinner_list[3] + "?")

"""习题3-6"""
#添加嘉宾
print("\nHello everyone, I have a larger dining table")
dinner_list.insert(0,'Tony-Tony Chopper')
dinner_list.insert(3,'Franky')
dinner_list.append("Brook")
print("\nCan you have dinner with me, " + dinner_list[0]+ "?")
print("Can you have dinner with me, " + dinner_list[1]+ "?")
print("Can you have dinner with me, " + dinner_list[2]+ "?")
print("Can you have dinner with me, " + dinner_list[3] + "?")
print("Can you have dinner with me, " + dinner_list[4]+ "?")
print("Can you have dinner with me, " + dinner_list[5]+ "?")
print("Can you have dinner with me, " + dinner_list[6]+ "?")

"""习题3-7"""
#缩减名单：你刚得知新购买的餐桌无法及时送到，因此只能邀请两位嘉宾。
print("\nSorry, there are only two places left")
name = dinner_list.pop()
print("Sorry "+ name +", I cannot invite you to have dinner with me")
name = dinner_list.pop()
print("Sorry "+ name +", I cannot invite you to have dinner with me")
name = dinner_list.pop()
print("Sorry "+ name +", I cannot invite you to have dinner with me")
name = dinner_list.pop()
print("Sorry "+ name +", I cannot invite you to have dinner with me")
name = dinner_list.pop()
print("Sorry "+ name +", I cannot invite you to have dinner with me")
print("\nCan you have dinner with me, " + dinner_list[0] + "?")
print("Can you have dinner with me, " + dinner_list[1] + "?")
del dinner_list[0]
print(dinner_list)
del dinner_list[0]
print(dinner_list)

"""习题3-8"""
#放眼世界，想出至少5个你渴望旅游的地方
places = ['yunna','chengdu','chongqing','xinjiang','lasa']
print(places)
#使用sorted()按字母顺序打印这个列表，同时不要修改它
print(sorted(places))
print(places)
#使用sorted()按与字母相反的顺序打印这个列表，同时不要修改它
print(sorted(places,reverse=True))
print(places)
#使用reverse()修改列表元素的排列顺序
places.reverse()
print(places)
places.reverse()
print(places)
#使用sort()修改该列表
places.sort()
print(places)
places.sort(reverse=True)
print(places)

"""习题3-10"""
#尝试使用各个函数，使用本章介绍的每个函数处理列表
list = ['Monkey·D·Luffy','Roronoa Zoro','Nami','Usopp','Tony-Tony Chopper','Franky']
#1、访问
print(list)
list_1 = list[4]
print(list_1)
#2、修改
list[5] = 'Brook'
print(list)
#3、添加
list.append("Charlotte LinLin")  #末尾添加
print(list)
list.insert(2,'Sanji')  #根据索引添加
print(list)
# 4、删除
del list[3] #根据索引删除元素，删除就没了呀
print(list)
name = list.pop()  #默认删除最后一个元素，可以将删除的元素给别人
print(name)
print(list)
list.remove('Sanji') #根据元素的值将元素删除
print(list)
#5、排序
list_1 = list
list.sort()  #根据首字母进行排序，永久性修改了位置
print(list)
list.sort(reverse=True)
print(list)

print(sorted(list_1)) #根据首字母排序，但是不改变原来列表中元素的位置
print(list_1)

list_1.reverse() #根据列表元素的位置进行反转，也是永久性修改了原列表的位置
print(list_1)
list_1.reverse()
print(list_1)
#6、计算列表的长度
print(len(list_1))
