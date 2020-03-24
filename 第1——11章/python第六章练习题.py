# coding=utf-8
# person = {'first_name':'li','last_name':'chong','city':'Beijing','age':'28'}
# print(person['first_name'])
# print(person['last_name'])
# print(person['city'])
# print(person['age'])


# # 6.2 Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary.
# # Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and
# # their favorite number. For even more fun, poll a few friends and get some actual data for your program.
# favorite_numbers = {
#     'mandy': 42,
#     'micah': 23,
#     'gus': 7,
#     'hank': 1000000,
#     'maggie': 0,
#     }
# print("mandy's favorite number is "+ str(favorite_numbers['mandy']))
# print("micah's favorite number is "+ str(favorite_numbers['micah']))
# print("gus's favorite number is "+ str(favorite_numbers['gus']))
# print("hank's favorite number is "+ str(favorite_numbers['hank']))
# print("maggie's favorite number is "+ str(favorite_numbers['maggie']))

# 6.3 A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a
# glossary. Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys
# in your glossary, and store their meanings as values. Print each word and its meaning as neatly formatted output.
# You might print the word followed by a colon and then its meaning, or print the word on one line and then print its
# meaning indented on a second line. Use the newline character ('\n') to insert a blank line between each word-meaning
# pair in your output.

glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    }

print('String: ' + glossary['string'] + '\n')
print('Comment: ' + glossary['comment'] + '\n')
print('List: ' + glossary['list'] + '\n')
print('Loop: ' + glossary['loop'] + '\n')
print('Dictionary: ' + glossary['dictionary'] )

#6.4

# glossary = {
#     'string': 'A series of characters.',
#     'comment': 'A note in a program that the Python interpreter ignores.',
#     'list': 'A collection of items in a particular order.',
#     'loop': 'Work through a collection of items, one at a time.',
#     'dictionary': "A collection of key-value pairs.",
#     }
#
# for key, value in glossary.items():
#     print('The Key is ' + key +', and the value is '+ value)

#6.5
# rivers = {
#     'nile': 'egypt',
#     'mississippi': 'united states',
#     'fraser': 'canada',
#     'kuskokwim': 'alaska',
#     'yangtze': 'china',
#     }
#
# for river,country in rivers.items():
#     print('\n' + "The " + river.title() + " runs through " + country.title())
#
# for river in rivers.keys():
#     print('- ' + river.title())
#
# for country in rivers.values():
#     print('- ' + country.title())


#6.6

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }
#
# coders = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']
#
#
# for coder in coders:
#     if coder in favorite_languages.keys():
#         print("Thank you for taking the poll, " + coder.title())
#     else:
#         print(coder.title() +  ", what's your favorite programming language?")

# 6.7
# peoples = []
# person = {
#     'first_name': 'eric',
#     'last_name': 'matthes',
#     'age': 43,
#     'city': 'sitka',
#     }
# peoples.append(person)
#
# person = {
#     'first_name': 'ever',
#     'last_name': 'matthes',
#     'age': 5,
#     'city': 'sitka',
#     }
# peoples.append(person)
#
# person = {
#     'first_name': 'willie',
#     'last_name': 'matthes',
#     'age': 8,
#     'city': 'sitka',
#     }
# peoples.append(person)
#
# for people in peoples:
#     name = people['first_name'].title() + ' ' + people['last_name'].title()
#     age = people['age']
#     city = people['city']
#     print(name +' is ' + str(age) + ' years old, and lives in ' + city)

#6.8
# pets = []
# pet = {
#     'animal type' : 'dog',
#     'owner' : 'guido'
# }
# pets.append(pet)
# pet = {
#     'animal type' : 'cat',
#     'owner' : 'dasha'
# }
# pets.append(pet)
# pet = {
#     'animal type' : 'tigger',
#     'owner' : 'lichong'
# }
# pets.append(pet)
#
# for pet in pets:
#     name = pet['animal type']
#     owners = pet['owner']
#     print(owners + " has a " +name + '.')

#6.9
# favoriates_places = {
#     'dasha':['shanghai','lijiang','qingdao'],
#     'lichong':['guangzhou','dali','qingdao'],
#     'xiaofeng':['pingyao','shenyang','dalian']
# }
#
# for name,place in favoriates_places.items():
#     print(name.title() + ' likes the: ')
#     for p in place:
#         print('\t'+p)

#6.10

# favorite_numbers = {
#     'mandy': [42, 17],
#     'micah': [42, 39, 56],
#     'gus': [7, 12],
#     }
# for name,number in favorite_numbers.items():
#     print(name.title() + 'favorite number is ')
#     for n in number:
#         print('- ' + str(n))

#6.11
# cities = {
#     'santiago': {
#         'country': 'chile',
#         'population': 6158080,
#         'nearby mountains': 'andes',
#         },
#     'talkeetna': {
#         'country': 'alaska',
#         'population': 876,
#         'nearby mountains': 'alaska range',
#         },
#     'kathmandu': {
#         'country': 'nepal',
#         'population': 1003285,
#         'nearby mountains': 'himilaya',
#         }
#     }
# for city,description in cities.items():
#     country = description['country']
#     population = description['population']
#     nearby_mountains = description['nearby mountains']
#     print('The ' + city.title() + ' is belong to ' + country.title() + '.')
#     print('It has a population of about ' + str(population) + '.')
#     print('The ' + nearby_mountains + ' are nearby.' +'\n')

