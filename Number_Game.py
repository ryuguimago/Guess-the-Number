#Guess the Number Game
import random
# generate random number between 1 and 20
def number_gen():
    number = random.randint(1,20)
    return number

#lets the user decide the range
def user_input():
    
#the actual guessing
def guessing():
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
                    break
                else:
                    print("you need to guess lower")
            else:
                print("your guess has to be between 1 and 20")
        except ValueError:
            print("your guess has to be a whole number")


# main function
def main():
    print("Hello, this is a number guessing game")
    
    while True:  # Loop to ensure valid input
        play = input("Do you want to play?\ny/n \n").strip().lower()  # Handle case insensitivity and extra spaces
        
        if play == "y":
            while True:
                print("Guess the number between 1 and 20")
                guessing()
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
