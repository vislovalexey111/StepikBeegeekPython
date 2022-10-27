from random import randint

def is_valid(num):
    if num.isnumeric() and 1 <= int(num) <= 100:
        return True

    return False

print('Welcom to the game "Guess A Magic Number"!')

magic_number = randint(1, 100)
attempts = 0

while True:
    num = input("\nEnter a number: ")
    attempts += 1

    while not is_valid(num):
        num = input("\nMay be you actually will enter integer between 1 and 100: ")
        attempts += 1

    n = int(num)

    if n == magic_number:
        print("\nYou've got the right number!")
        print("Total attempts:", attempts)

        break
    elif n < magic_number:
        print("Your number is less then Magic Number! Try again!")
    else:
        print("Your number is greater then Magic Number! Try again!")

print('\n', '*' * 3, "Thank you for playing!", '*' * 3)