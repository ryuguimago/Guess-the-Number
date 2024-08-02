#Guess the Number Game
import random
# generate random number between 1 and 20
def number_gen(a,b):
    number = random.randint(a,b)
    return number

#lets the user decide the range
def user_input():
    # todo: handle edge cases and error messages 
    print("please enter the numbers for the range you want to play")
    a = int(input("please enter the low number: "))
    b = int(input("please enter the high number: "))
    return a,b 

#the actual guessing
def guessing(a,b):
    number = number_gen(a,b)
    guess = 0
    while guess != number:
        try:
            guess = int(input("what is your guess?"))
            if guess in range(a,b+1):
                if guess < number:
                    print("you need to guess higher")
                elif guess == number:
                    print("Congratulations, you found the number") # todo: count tries for user experiance 
                    break
                else:
                    print("you need to guess lower")
            else:
                print(f"your guess has to be between {a} and {b}")
        except ValueError:
            print("your guess has to be a whole number")


# main function
def main():
    print("Hello, this is a number guessing game")
    
    while True:  # Loop to ensure valid input
        play = input("Do you want to play?\ny/n \n").strip().lower()  # Handle case insensitivity and extra spaces
        
        if play == "y":
            
            while True:
                a,b = user_input()
                print(f"Guess the number between {a} and {b}")
                guessing(a,b)
                play = input("Do you want to play again?\ny/n \n").strip().lower()
                if play != "y":
                    break
            break  # Exit the loop after the user decides not to play again
        elif play == "n":
            print("c u next time")
            break  # Exit the loop if the user does not want to play
        else:
            print("Please enter a valid response ('y' or 'n')")

if __name__ == "__main__":
    main()
