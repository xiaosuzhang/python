#使用for循环语句遍历整个列表
# anmials = ['panda','dog','cat']
# for anmial in anmials:
#     print('A '+str(anmial)+' would make a great pet')
# print('Any of these animals would make a great pet')

#4.3数到20：使用一个for循环打印数字1~20（含）
# for num in range(1,21):
#     print(num)
#4.4 一百万：创建一个列表，其中包含数字1~1000000，在使用一个for循环将这些数字打印出来
# num = list(range(1,1000001))
# for n in num:
#     print(n)
#4.5:计算1~1000000的总和：创建一个列表，包含数字1~1000000，再使用min()和max()函数核实该列表确实从1开始，到1000000结束的。
# 另外，对这个列表调用函数sum()，看看Python将一百万数字相加需要多长时间
# num = list(range(1,1000001))
# print(max(num))
# print(min(num))
# print(sum(num))
#4.6奇数：通过给函数range()指定第三个参数来创建一个列表，其中包含数字1~20的奇数，在使用一个for循环将折写数字打印出来
# odd_number = list(range(1,20,2))
# print(odd_number)
# for n in odd_number:
#     print(n)
#4.7 3的倍数：创建一个列表，其中包含3~30以内能被3整除的数字，在使用一个for循环将这个列表的数字打印出来
# numbers = list(range(3,30,3))
# print(numbers)
# for n in numbers:
#     print(n)
##4,8 立方：请创建一个列表，其中包含前10个整数的立方，在使用一个for循环将这些立方数都打印出来
# cublic_number = []
# for n in range(1,11):
#     cublic_number.append(n**3)
# print(cublic_number)
# for n in cublic_number:
#     print(n)
##4.9 立方解析：使用列表解析生成一个列表，其中包含前10个整数的立方
# cublic_number = list(value**3 for value in range(1,11))
# print(cublic_number)

##4.10  切片：选择你在本章编写的一个程序，在末尾添加几行代码：已完成如下任务：
#任务1：打印消息"The first three item in the list are:"，再使用切片来打印列表的前三个元素
# list1 = ['lichong','dasha',12311,'ersha',267]
# print("The first three items in the list are:"+str(list1[:3]))
# print("Three items form the middle of the list are:"+str(list1[1:4]))
# print("The last three items in the list are:"+str(list1[-3:]))

##4.11 你喜欢的动物和我喜欢的动物
my_animals = ['panda','dog','cat']
firend_animal = my_animals[:]
my_animals.append('tiger')
firend_animal.append('bird')
print('My favorite animals are: '+ str(my_animals))
for n in my_animals:
    print(n)
print("My  friend's favorite animals are: "+ str(firend_animal))
for n1 in firend_animal:
    print(n1)
