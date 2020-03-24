# coding=utf-8

# alien_color = 'red'
#
# if alien_color == 'green':
#     print('You got five points')
# elif alien_color == 'yellow':
#     print('You got ten points')
# else:
#     print('You got 20 points')

# use_names = ['admin','dasha','tong','kexin','na']
#
# use_name = 'admin'
# if use_names == []:
#     print("We need to find some users!")
# elif use_name in use_names:
#     print("Hello admin, would you like to see a status report?")
# else:
#     print("Hello Eric, thank you for logging in again")


current_names = ['ADMIN','dasha','tong','kexin','na']
new_users = ['Admin','dasha','James','Messii','Koby']

for name in new_users:
    if name in current_names or name.upper() in current_names:
        print("You should input another use name")
    else:
        print("The use name is not used")
