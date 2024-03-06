import random
import string

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
special_characters = "@#$%^&*"
password_list = []

times = int(input('Enter the number of times passwords to be generated: '))
user = int(input('Enter the length of each password (in numbers): '))

for a in range(times):
    for i in range(0, user):
        number = random.randint(0, 9)
        lett = random.choice(letters)
        char = random.choice(special_characters)
        password_list.append(lett)
        password_list.append(str(number))
        password_list.append(char)

    random.shuffle(password_list)
    password = ''.join(password_list)
    print(password[:user])
    password_list = []
