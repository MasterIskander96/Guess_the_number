import random

rand = random.randint(1,100)

retr = input("Your name:")
if retr == "Iskander5102i":
    print("Hello,game creator!")
    print(f"Secret number: {rand}")
else:
    print(f"Good luck in the game {retr}!")

tries = 0

while True:
    if tries >= 5:
        print(f"You have used up all your attempts.Secret number:{rand}.")
        break

    number = int(input("Try to guess the number:"))

    tries += 1

    if number > 100:
        print("Error! Enter any number from 1 to 100.")

    elif number > rand:
        print("Too lower!Try again!↻")

    elif number < rand:
        print("Too high!Try again!↻")

    elif number == rand:
        print("Congratulations! You guessed it!🥳🥳🥳")
        break

    else:
        print("Ошибка!Напишите любое число от 1 до 100")