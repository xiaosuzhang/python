# coding=utf-8

##7.1
# car = input("What kind of car would you like? ")
# print("Let me see if i can find you a " + car)

##7.2
# number_of_people = input("How many people are in your dinner party tonight? ")
# number_of_people = int(number_of_people)
#
# if number_of_people > 8:
#     print("I'm sorry, you'll have to wait for a table.")
# else:
#     print("Your table is already")

##7.3
# number = input("Please give me a number: ")
# number = int(number)
# if number % 10 == 0:
#     print(str(number) + " is a multiple of 10.")
# else:
#     print(str(number) + " is not a multiple of 10.")

##7.4
# prompt = "\nWhat topping would you like on your pizza?"
# prompt += "\nEnter 'quit' when you are finished: "

# prompt_1 = input(prompt)
# while prompt_1 != 'quit':
#     print("We'll add " + prompt_1 + ' in your pizza')
#     prompt_1 = input(prompt)


# while True:
#     if input(prompt) != 'quit':
#         print("We'll add " + prompt + ' in your pizza')
#     else:
#         break

##7.5

# prompt = "How old are you?"
# prompt += "\nEnter 'quit' when you are finished. "
#
# while True:
#     age = input(prompt)
#     if age == 'quit':
#         break
#
#     age = int(age)
#     if age < 3:
#         print("The ticket is free")
#     elif age < 12:
#         print("The ticket is 10 dollars")
#     else:
#         print("The ticket is 15 dollars")

## 7.8
# sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
# finished_sandwiches = []
# while sandwich_orders:
#     sandwiches = sandwich_orders.pop()
#     print("I'm working on your " + sandwiches + " sandwich.")
#     finished_sandwiches.append(sandwiches)
# print("\n")
# for sandwiches in finished_sandwiches:
#     print("I made your " + sandwiches + " sandwich.")


##7.9
# sandwich_orders = [
#     'pastrami', 'veggie', 'grilled cheese', 'pastrami',
#     'turkey', 'roast beef', 'pastrami']
# finished_sandwiches = []
#
# print("I'm sorry, we're all out of pastrami today.")
#
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
#
# print(sandwich_orders)
#
# while sandwich_orders:
#     sandwich = sandwich_orders.pop()
#     print("I'm working on your " + sandwich + " sandwich.")
#     finished_sandwiches.append(sandwich)
#
# print("\n")
# for sandwiches in finished_sandwiches:
#     print("I made your " + sandwiches + " sandwich.")

##7.10
response = {}
activate = True
while activate:
    name = input("\n Can you give me youe name? ")
    place = input("If you could visit one place in the world, where would it be? ")
    response[name] = place
    repeat = input('\n Would you like to let another person respond?(yes/no) ')
    if repeat == 'no':
        activate = False
print("\n ---Poll result----")
for name,place in response.items():
    print(name + " would like to visit " + place + "." +'\n')