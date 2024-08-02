#Guess the Number Game
import random
# generate random number between 1 and 100
def number_gen():
    number = random.randint(1,20)
    return number

print("Hello, this is a number guessing game")
print("guess the number between 1 and 20")
number = number_gen()
guess = 0
while guess != number:
    try:
        guess = int(input("what is your guess?"))
        if guess in range(1,21):
            if guess < number:
                print("you need to guess higher")
            elif guess == number:
                print("Congratulations, you found the number")
                exit()
            else:
                print("you need to guess lower")
        else:
            print("your guess has to be between 1 and 20")
    except ValueError:
        print("your guess has to be a whole number")