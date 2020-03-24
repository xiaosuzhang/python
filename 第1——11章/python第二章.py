#打印
print("hello Python world!")
#变量,打印函数
message = "Hello Python world!"
print(message)

#重新定义变量，变量值刷新
message = "Hello Python Crash Course World!"
print(message)

#使用变量时避免命名错误
message = "Hello Python Crash Course World!"
#print(mesage)

"""2.3 字符串"""
#使用方法修改字符串的大小写
name = "ada lovalace"
print(name.title())
print(name.upper())
print(name.lower())

#合并（拼接）字符串
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")
a = "Hello, " + full_name.title() + "!"
print(a)

#使用制表符或换行符添加空白
print('python')
print("\tpython")
print("Languagee:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#删除字符串空格——.rstrip()删除字符串末尾空格
favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())

#永久删除空格
favorite_language = "python "
print(favorite_language)
favorite_language = favorite_language.rstrip()
print(favorite_language)

#删除字符串两端或者开头的空格
favorite_language = " python"
print(favorite_language)
favorite_language = favorite_language.lstrip()
print(favorite_language)

favorite_language = " python "
print(favorite_language)
favorite_language = favorite_language.strip()
print(favorite_language)

#数字
age = 23
message = "Happy "+ str(age) + "rd Birthday!"
print(message)