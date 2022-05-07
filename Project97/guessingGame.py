import random

chances = 0

print("Number guessing game")
print("Guess a number (between 1 and 9)")

number = random.randint(1,9)

while chances < 5:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Congratulations YOU WON!!!")
        break

    elif guess < number:
        print("Your guess was too low: Guess a number higher than", guess)

    else:
        print("Your guess was too high: Guess a number higher than", guess)

    chances +=1

    if not chances < 5:
        print("YOU LOSE!!! The number is", number)