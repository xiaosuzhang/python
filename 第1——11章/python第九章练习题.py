# coding=utf-8
##9.1 9.2
# class Restaurant():
#     """A class representing a restaurant."""
#
#     def __init__(self, name, cuisine_type):
#         """Initialize the restaurant."""
#         self.name = name.title()
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         """Display a summary of the restaurant."""
#         msg = self.name + " serves wonderful " + self.cuisine_type + "."
#         print("\n" + msg)
#
#     def open_restaurant(self):
#         """Display a message that the restaurant is open."""
#         msg = self.name + " is open. Come on in!"
#         print("\n" + msg)
#
# restaurant = Restaurant('the mean queen', 'pizza')
# print(restaurant.name)
# print(restaurant.cuisine_type)
#
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
#
#
# ludvigs = Restaurant("ludvig's bistro", 'seafood')
# ludvigs.describe_restaurant()
#
# mango_thai = Restaurant('mango thai', 'thai food')
# mango_thai.describe_restaurant()

##9.3
#
# class User():
#     """创建一个描述用户信息的类"""
#
#     def __init__(self,first_name,last_name,username,email,location):
#         """类的初始化"""
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()
#         self.username = username
#         self.email = email
#         self.location = location
#
#     def describe_user(self):
#         """打印用户信息摘要"""
#         print("\n" + self.first_name + " " + self.last_name)
#         print("  Username: " + self.username)
#         print("  Email: " + self.email)
#         print("  Location: " + self.location)
#
#
#
#     def greet_user(self):
#         """向用户发出个性化问候"""
#         print("\nWelcome back, " + self.username + "!")
#
# ueser_1 = User("li","chong","dasha","12333@gdasha.com","Beijing")
# ueser_1.describe_user()
# ueser_1.greet_user()

##9.4

# class Restaurant():
#     """A class representing a restaurant."""
#
#     def __init__(self, name, cuisine_type):
#         """Initialize the restaurant."""
#         self.name = name.title()
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         """Display a summary of the restaurant."""
#         msg = self.name + " serves wonderful " + self.cuisine_type + "."
#         print("\n" + msg)
#
#     def open_restaurant(self):
#         """Display a message that the restaurant is open."""
#         msg = self.name + " is open. Come on in!"
#         print("\n" + msg)
#
#     def set_number_served(self,served):
#         self.number_served = served
#         print("在这家餐厅的就餐人数为：" + str(self.number_served))
#
#     def increment_number_served(self,number):
#         self.number_served += number
#
# restaurant = Restaurant('the mean queen', 'pizza')
#
# restaurant.set_number_served(40)
# print("在这家餐厅的就餐人数为：" + str(restaurant.number_served))
# restaurant.increment_number_served(239)
# print("Number served: " + str(restaurant.number_served))


##9.5
# class User():
#     """创建一个描述用户信息的类"""
#
#     def __init__(self,first_name,last_name,username,email,location):
#         """类的初始化"""
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()
#         self.username = username
#         self.email = email
#         self.location = location
#         self.login_attempts = 0
#
#     def describe_user(self):
#         """打印用户信息摘要"""
#         print("\n" + self.first_name + " " + self.last_name)
#         print("  Username: " + self.username)
#         print("  Email: " + self.email)
#         print("  Location: " + self.location)
#
#     def greet_user(self):
#         """向用户发出个性化问候"""
#         print("\nWelcome back, " + self.username + "!")
#
#     def increment_login_attempts(self):
#         """将登陆次数增加1"""
#         self.login_attempts += 1
#         return self.login_attempts
#
#
#     def reset_login_attempts(self):
#         """重置登陆次数"""
#         self.login_attempts = 0
#         return self.login_attempts
#
# ueser_1 = User("li","chong","dasha","12333@gdasha.com","Beijing")
#
# ueser_1.login_attempts = 12
# login_attempts = ueser_1.increment_login_attempts()
# print("用户登陆次数为：" + str(login_attempts))
#
# login_attempts = ueser_1.reset_login_attempts()
# print("用户登陆次数为：" + str(login_attempts))

##9.6
# class Restaurant():
#     """A class representing a restaurant."""
#
#     def __init__(self, name, cuisine_type):
#         """Initialize the restaurant."""
#         self.name = name.title()
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         """Display a summary of the restaurant."""
#         msg = self.name + " serves wonderful " + self.cuisine_type + "."
#         print("\n" + msg)
#
#     def open_restaurant(self):
#         """Display a message that the restaurant is open."""
#         msg = self.name + " is open. Come on in!"
#         print("\n" + msg)
#
#     def set_number_served(self,served):
#         self.number_served = served
#         print("在这家餐厅的就餐人数为：" + str(self.number_served))
#
#     def increment_number_served(self,number):
#         self.number_served += number
#
#
# class IceCreamStand(Restaurant):
#
#     def __init__(self, name, cuisine_type='ice_cream'):
#         super().__init__(name, cuisine_type)
#         self.flavors = []
#
#     def show_incream(self):
#         print("\nWe have the following flavors available:")
#         for flavor in self.flavors:
#             print("- " + flavor.title())
#
# big_one = IceCreamStand('The Big One')
# big_one.flavors = ['vanilla', 'chocolate', 'black cherry']
# big_one.show_incream()

##9.7
#
# class User():
#     """创建一个描述用户信息的类"""
#
#     def __init__(self,first_name,last_name,username,email,location):
#         """类的初始化"""
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()
#         self.username = username
#         self.email = email
#         self.location = location
#         self.login_attempts = 0
#
#     def describe_user(self):
#         """打印用户信息摘要"""
#         print("\n" + self.first_name + " " + self.last_name)
#         print("  Username: " + self.username)
#         print("  Email: " + self.email)
#         print("  Location: " + self.location)
#
#     def greet_user(self):
#         """向用户发出个性化问候"""
#         print("\nWelcome back, " + self.username + "!")
#
#     def increment_login_attempts(self):
#         """将登陆次数增加1"""
#         self.login_attempts += 1
#         return self.login_attempts
#
#
#     def reset_login_attempts(self):
#         """重置登陆次数"""
#         self.login_attempts = 0
#         return self.login_attempts
#
# class Admin(User):
#
#     def __init__(self,username,first_name='li',last_name='chong',email='',location='Beijing'):
#         super().__init__(first_name,last_name,username,email,location)
#         self.privileges = []
#
#     def show_privileges(self):
#         print("用户：" + self.username.title() + " 拥有的权限如下：")
#         for privilege in self.privileges:
#             print("  -" + privilege)
#
# user_1 = Admin("dasha")
# user_1.privileges = ["can add post",'can delete post']
# user_1.show_privileges()


##9.8

# class User():
#     """创建一个描述用户信息的类"""
#
#     def __init__(self,first_name,last_name,username,email,location):
#         """类的初始化"""
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()
#         self.username = username
#         self.email = email
#         self.location = location
#         self.login_attempts = 0
#
#     def describe_user(self):
#         """打印用户信息摘要"""
#         print("\n" + self.first_name + " " + self.last_name)
#         print("  Username: " + self.username)
#         print("  Email: " + self.email)
#         print("  Location: " + self.location)
#
#     def greet_user(self):
#         """向用户发出个性化问候"""
#         print("\nWelcome back, " + self.username + "!")
#
#     def increment_login_attempts(self):
#         """将登陆次数增加1"""
#         self.login_attempts += 1
#         return self.login_attempts
#
#
#     def reset_login_attempts(self):
#         """重置登陆次数"""
#         self.login_attempts = 0
#         return self.login_attempts
#
# class Privileges():
#
#     def __init__(self,privileges=[]):
#         self.privilages = privileges
#
#
#     def show_privileges(self):
#         for privilege in self.privilages:
#             print(" --" + privilege)


# class Admin(User):
#
#     def __init__(self,username,first_name='li',last_name='chong',email='',location='Beijing'):
#         super().__init__(first_name,last_name,username,email,location)
#         self.privileges = Privileges()
#
#
# amdin_1 = Admin("dasha")
# print("用户：" + amdin_1.username.title() + " 拥有的权限如下：")
# amdin_1.privileges.privilages = ["can add post",'can delete post']
# amdin_1.privileges.show_privileges()


##9.9

# class Car():
#     """A simple attempt to represent a car"""
#
#     def __init__(self,manufacturer,model,year):
#         """Initialize attributes to describe a car"""
#         self.manufacturer = manufacturer
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = str(self.year) + " " + self.manufacturer + " " + self.model
#         return long_name.title()
#
#     def read_odmeter(self):
#         """Print a statement showing the car's mileage"""
#         print("This ca has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self,mileage):
#         """
#         Set the odometer reading to the given value.
#         Reject the change if it attempts to roll the odometer back.
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self,miles):
#         """Add the given amount of the odometer reading."""
#         self.odometer_reading += miles
#
# class Bateery():
#     """A simple attempt to model a battery for an electric car."""
#     def __init__(self,battery_size = 70):
#         """Initialize the battery's attributes."""
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         """Print a statement about the range this battery provides."""
#         print("This car has a " + str(self.battery_size) + " -KWh battery.")
#
#     def get_range(self):
#         """Print a statement about the range this battery provides."""
#
#         if self.battery_size == 70:
#             range = 240
#         elif self.battery_size == 85:
#             range = 270
#
#         message = "This car can go approximately " + str(range)
#         message += " miles on a full charge."
#         print(message)
#
#     def upgrade_battery(self):
#         """"""
#         if self.battery_size != 85:
#             self.battery_size = 85
#
#
# class ElectricCar(Car):
#
#     """Models aspects of a car, specific to electric vehicles."""
#
#     def __init__(self,make,model,year):
#         super().__init__(make,model,year)
#         self.battery = Bateery()
#
# print("Make an electric car, and check the battery:")
# my_tesla = ElectricCar('tesla', 'model s', 2016)
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
#
# print("\nUpgrade the battery, and check it again:")
# my_tesla.battery.upgrade_battery()
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

##9.10
# import restaurant
# res = restaurant.Restaurant('the mean queen', 'pizza')
# res.describe_restaurant()
#
# from restaurant import Restaurant
# res_1 = Restaurant('the mean queen', 'pizza')
# res_1.open_restaurant()

##9.11

# from admin import Admin,Privileges
#
# admin_1 = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
#
# admin_1.privileges.privileges =[
#     'can reset passwords',
#     'can moderate discussions',
#     'can suspend accounts',
# ]
# admin_1.privileges.show_privileges()

##9.12

# from admin import Admin,Privileges
#
# admin_1 = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
# admin_1.describe_user()
# admin_1.privileges.privileges =[
#     'can reset passwords',
#     'can moderate discussions',
#     'can suspend accounts',
# ]
# print("\nThe admin " + admin_1.username + " has these privileges: ")
# admin_1.privileges.show_privileges()


##9.13

# from collections import OrderedDict
#
# glossary = OrderedDict()
# glossary['boolean expression'] = 'An expression that evaluates to True or False.'
# glossary['string'] = "A series of characters."
# glossary['comment'] = 'A note in a program that the Python interpreter ignores.'
# glossary['list'] = 'A collection of items in a particular order.'
# glossary['loop'] = 'Work through a collection of items, one at a time.'
# glossary['dictionary'] =  "A collection of key-value pairs."
# glossary['key'] = 'The first item in a key-value pair in a dictionary.'
# glossary['value'] =  'An item associated with a key in a dictionary.'
# glossary['conditional test'] =  'A comparison between two values.'
# glossary['float'] = 'A numerical value with a decimal component.'
#
# for word,definition in glossary.items():
#     print("\n" + word.title() + ": " + definition)

##9.19
from random import randint
# x = randint(1,6)
# print(x)

class Die():

    def __init__(self,sides = 6):
        self.sides = sides

    def roll_die(self):
        return randint(1,self.sides)

d6 = Die()
results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die:")
print(results)

# Make a 10-sided die, and show the results of 10 rolls.
d10 = Die(sides=10)

results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 rolls of a 10-sided die:")
print(results)

# Make a 20-sided die, and show the results of 10 rolls.
d20 = Die(sides=20)

results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("\n10 rolls of a 20-sided die:")
print(results)