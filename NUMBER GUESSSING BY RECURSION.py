import random
easy_number_of_attempts=10
medium_number_of_attempts=7
hard_number_of_attempts=5
def set_difficulty(level):
    if level=="easy":
        return easy_number_of_attempts
    elif level=="medium":
        return medium_number_of_attempts
    elif level=="hard":
        return hard_number_of_attempts
    else:
        return

def check_num(guessed_num,answer,attempts):
    if guessed_num<answer:
        print("your guess is too low")
        return attempts-1
    elif guessed_num>answer:
        print("Your guess is too high")
        return attempts-1
    else:
        print(f"Your guess is correct....The answer was {answer}")
        return attempts

def game():
    print("let me think of a number between 1 to 50:")
    answer=random.randint(1,50)
    level = input("Choose difficulty (easy / medium / hard): ").lower()
    attempts = set_difficulty(level)
    if attempts is None:
        print("Invalid level! Please choose again.\n")
        game()
        return
    guessed_num=0
    while guessed_num!=answer:
        print(f"You have {attempts} remaining to guess the number")
        guessed_num=int(input("Guess a number: "))
        attempts=check_num(guessed_num,answer,attempts)
        if attempts==0:
            print("You lose the Game!")
            print("play again!")
            return
        elif guessed_num!=answer:
            print("Guess again")

game()









