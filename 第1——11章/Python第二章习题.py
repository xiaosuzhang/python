""" 习题2-1"""
#将一条消息存储到变量中，再将其打印出来
message = "I am aron man"
print(message)

"""习题2-2"""
#将一条消息存储到变量中，将其打印出来；再将变量的值修改为一条新消息，并将其打印出来
message = "I want to do something"
print(message)
message = "I love you 3000 times "
print(message)

"""习题2-3"""
#个性化消息：将用户的姓名存储到一个变量中，并向该用户显示一条消息
name = "Eric"
print("Hello " + name +", would you like to learn some Python tooday?")

"""习题2-4"""
#将一个人的姓名存储到一个变量中，再以小写、大写和首字母大写的方式显示这个人名
name = "eric"
print(name)
print(name.title())
print(name.upper())
name = name.upper()
print(name.lower())

"""习题2-5"""
#找一句你钦佩的名人所说的名言，将这个名人的姓名和他的名言打印出来。
print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')

"""习题2-6"""
#重复练习2-5，但将名人的姓名存储在变量famous_person中，在创建要显示的消息，并将其存储在变量message中，
# 然后打印这条消息
famouse_person = "Albert Einstein"
massage = famouse_person + ' once said, "A preson who never made a mistake never tried anything new."'
print(massage)

"""习题2-7"""
#删除人名中的空白：存储一个人名，并在其开头和末尾包含一些空白符。务必至少使用字符组合"\t"和"\n"各一次
name = "\tAlbert\nEinstein\t"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

name_1 = "\n\tTom\t\t\na"
print(name_1)
a = name_1.strip()
print(a)
b = name_1.lstrip()
print(b)
c = name_1.rstrip()
print(c)

"""习题2-8"""
#数字8。编写4个表达式，它们分别使用加、减、乘、除运算，但结果都是数字8.
print(3+5)
print(9-1)
print(4*2)
print(8/1)

"""习题2-9"""
#最喜欢的数字：将你最喜欢的数字存储到一个变量中，再使用这个变量创建一条消息，指出你最喜欢的数字，然后将这条消息打印出来
favorite_number = 8
message = "My favorite number is " + str(favorite_number)
print(message)


