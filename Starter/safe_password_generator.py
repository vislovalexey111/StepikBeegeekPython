from random import choice

passwords = []
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
invalid_characters = 'il1Lo0O'
requirements = ''

def is_valid(string):
    if string.isnumeric() and int(string) > 0:
        return True

    return False

def generate_password(length, characters):
    password = ''

    for _ in range(length):
        password += choice(characters)

    return password

inp = input('How many passwords do you need: ')

while not is_valid(inp):
    inp = input("ERROR: try again to enter number of passwords: ")

passwords_count = int(inp)

inp = input('How long each password must be: ')

while not is_valid(inp):
    inp = input("ERROR: try again to enter length of each password: ")

password_length = int(inp)

if input("Do you need numbers? (y/any): ") == 'y':
    requirements += digits

if input("Do you need capital letters? (y/any): ") == 'y':
    requirements += uppercase_letters

if input("Do you need normal letters? (y/any): ") == 'y':
    requirements += lowercase_letters

if input("Do you need punctuation symbols? (y/any): ") == 'y':
    requirements += punctuation

if input("Exclude strange symbols? (y/any): ") == 'y':
    for bad_char in invalid_characters:
        requirements.replace(bad_char, '')

for _ in range(passwords_count):
    passwords.append(generate_password(password_length, requirements))

print(*passwords)