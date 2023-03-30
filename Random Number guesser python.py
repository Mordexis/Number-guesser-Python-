import random
#This is a number guessing game that I'm making for fun
#There's going to be two game modes: one where you guess a random number and one where the computer guesses

def player_guessing():
    Lowerbound=int(input("Enter the lowerbound"))
    Upperbound = int(input("Enter the Upperbound"))
    computer_choice = random.randint(Lowerbound, Upperbound)

    #This function is used to randomly pick a number in a specified range

    user_choice = 0
    while user_choice != computer_choice:

        #A While loop is used to continuously prompt the user for input

        user_choice = int(input("Guess a number"))

        #If and elif statements are used to give the user tips.
        if user_choice > computer_choice:
            print("Too big")

        elif user_choice< computer_choice:
            print("Too small")

        #This is omitted from the while loop as it is only executed after the while loop has been broken

    print(f"Congrats on guessing the number.")

# That is the first function which we use to make the player guess a randomly generated number from the computer

def computer_guessing():
    #This function will have the computer randomly guess a number
    Lowerbound=int(input("Enter the lowerbound"))
    Upperbound = int(input("Enter the Upperbound"))
    computer_guess = random.randint(Lowerbound, Upperbound)
    result = "n"
    #This is similar to the previous function however in this one we have the computer randomly guess a number
    #We use if statements to help guide the computer towards the correct number
    while result != "c" or result != "correct" or result != "y" or result != "yes":
        print(f"Was your number {computer_guess}?")
        result = input("Is this right? Type c if it's correct.\
        H if it's too high.\
        L if it's too low").lower()
        #Backslashes are used to output onto the next line
        #We use .lower() to forcefully make the string input lowercase
        if result == "h" or result == "high":
            Upperbound = computer_guess -1
            #This is done to push the computer towards the right number
            #If it's too high that means it's below the guessed number thus it becomes the Upperbound.
            #The minus one is added as it can still guess the Upperbound and so whilst unlikely it could infinitely loop in theory

        elif result == "l" or result == "low":
            Lowerbound = computer_guess + 1
            #same logic as before is used.

        elif result == "c" or result == "correct" or result == "y" or result == "yes":
            break

        else:
            print("Invalid input")
            #done to ensure that users use the selected choices.

        computer_guess = random.randint(Lowerbound, Upperbound)

    print(f"Great I guessed the number!")



def gameplay():
    #This function will be used to loop and help the user pick between the two game modes.
    print("This is a number guesser game made by Adrian")
    print("There are Currently two game modes\
    1. You guess a random number\
    2. The computer guesses a random number")
    cont_play = ("Would you like to play? Y/N")
    while cont_play != "n" and cont_play != "no":
        cont_play = input("Would you like to play? Y/N")
        if cont_play == "y" or cont_play == "yes":
            game_selecter =input("Press 1 to guess a number\
            Press 2 for the computer to guess").lower()
            if game_selecter == "1":
                player_guessing()

            elif game_selecter == "2":
                computer_guessing()

            else:
                print("Invalid input")

        elif cont_play == "n":
            break

        else:
            print("Invalid input")

    print("Thanks for playing")

gameplay()
