#访问列表元素
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[-1])
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

#修改列表元素
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

#在列表中添加元素——在列表的末尾添加元素
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

#在列表中添加元素——在列表中插入元素
motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)

#从列表中删除元素——使用del删除元素
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

#使用pop删除列表末尾的元素
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
popped_motorycle = motorcycles.pop()
print(popped_motorycle)
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + "!")
first_owned = motorcycles.pop(0)
print("The last motorcycle I owned was a " + first_owned.title() + "!")

#根据值删除元素
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.remove('honda')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki','ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print('\nA ' + too_expensive.title() +" is too expensive for me")

#使用sort()对列表进行永久性排序
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
car = ['bmw','audi','toyota','subaru']
car.sort(reverse=True)
print(car)

#使用sorted()函数对列表进行临时性排序

cars = ['bmw','audi','toyota','subaru']
print("Here is original list:")
print(cars)
print("\nHere is the second list:")
print(sorted(cars))
print("\nHere is the original list again：")
print(cars)

#倒着打印列表
cars = ['bmw','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)

#确定列表的长度
cars = ['bmw','audi','toyota','subaru']
print(len(cars))