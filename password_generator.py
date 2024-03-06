import random
import string
letters = 'abcdefghijklmnopqrstuvwxzyABCDEFGHIJKLMNOPQRSTUVWXZY'
special_characters = "@#$%^&*"
password_list = []
user = int(input('Enter the length of password(in numbers): '))
for i in range(0,user):
    number = random.randint(0,9)
    lett = random.choice(letters)
    char = random.choice(special_characters)
    password_list.append(lett)
    password_list.append(str(number))
    password_list.append(char)
    
random.shuffle(password_list)
password = ''.join(password_list)
print(password[:user])
