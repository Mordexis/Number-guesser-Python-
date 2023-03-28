import random
def rps():
    wins = 0
    losses = 0
    ties = 0
    first_to = int(input("What would you like to play up to?"))
    while wins < first_to and losses < first_to:
        user_choice = input("Pick between rock, paper and scissors.")
        computer_choice = random.choice(["rock", "paper", "scissors"])

        leg_moves = {"rock": {"rock": "tie", "paper": "lose", "scissors": "win"},
        "paper": {"rock": "win", "paper": "tie", "scissors": "lose"},
        "scissors": {"rock": "lose", "paper": "win", "scissors": "tie"}
        }

        if user_choice.lower() in leg_moves:
            result = leg_moves[user_choice.lower()][computer_choice]
            if result == "win":
                wins += 1
                print(f"You used {user_choice}. The computer used {computer_choice}.")
                print("You won this round.")

            elif result == "lose":
                losses += 1
                print(f"You used {user_choice}. The computer used {computer_choice}.")
                print("You lost this round.")

            elif result == "tie":
                print(f"You used {user_choice}. The computer used {computer_choice}.")
                ties += 1
                print("It's a tie!")

        else:
            print("Invalid input")

        if wins == first_to:
            print("Congrats you win!")
            print(f"You had {wins} wins, {losses} losses and {ties} ties.")
            break

        elif losses == first_to:
            print("You lose!")
            print(f"You had {wins} wins, {losses} losses and {ties} ties.")
            break


def gameplay():
    print("This is an online rock paper scissors game made by Adrian")
    cont_play = input("Would you like to play? Y/N").lower()
    while cont_play != "n" and cont_play != "no":
        rps()
        cont_play = input("Would you like to play? Y/N").lower()

        if cont_play == "n" or cont_play == "no":
            print("Thanks for playing")
            break

    if cont_play == "n" or cont_play == "no":
        print("Play when you're ready")


gameplay()