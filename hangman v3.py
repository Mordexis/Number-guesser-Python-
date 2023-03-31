words = ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "india", "juliett", "kilo", "lima", "mike", "november", "uniform", "victor", "whiskey", "xray", "yankee", "zulu"]
import random
# Slightly better version of hangman
#changes made:
#Made it accurately display your current progress
#made it tell you if your guess was correct
#removed the duplicate string when you lose
#made it so that the word is shown to you before you start guessing
#made it so that if the length of your guess is greater than one it prints invalid input rather than wrong
#got rid of unnecessary print statements on the branches
#made it so that if you enter the whole word you win.
#added a gameplay function to continously loop through and allow you to replay the game

def hangman():


    word = random.choice(words)

    letters_to_guess = set(word)

    guessed_letters= set()

    correct_guess = set()

    tries = 10



    while tries >0 and len(letters_to_guess)>0:
        
        progress = [letter if letter in correct_guess else "_" for letter in word]
        
        print("Your word is", " ".join(progress))
        print("You have used the following letters:", ", ".join(guessed_letters))
        print(f"You have {tries} tries left")
            

        guess = input("Please guess a letter").lower()





        if guess in guessed_letters and guess.isalpha():
            print("Already guessed")
            print("You have used these letters", ", ".join(guessed_letters))
            print(f"You have {tries} tries left")


        elif guess in letters_to_guess and guess.isalpha():
            letters_to_guess.remove(guess)
            guessed_letters.add(guess)
            correct_guess.add(guess)
            print("Correct!")
            progress = [letter if letter in correct_guess  else "-" for letter in word]
            
        elif guess == word:
            print("You win!")
            break
            
        elif len(guess) != 1:
            print("Invalid input")

        else:
            print("Wrong")
            guessed_letters.add(guess)
            tries -=1
            

    if tries == 0:
        print(f"You lose the word was {word}")

    elif len(letters_to_guess) == 0:
        print("You won!")
        print(f"The word was {word}")

def gameplay():
    print("This is a digital game of hangman made by Adrian")
    play = input("Would you like to play? Y/N").lower()
    
    if play == "y" or play == "yes":
        while play != "n" or play != "no":
            hangman()
            play = input("Would you like to play again? Y/N")
            if play == "n" or play == "no":
                print("Thanks for playing")
                break
            
    elif play == "n" or play == "no":
        print("Please play when you're ready")
        
    else:
        print("Invlaid input")
        while play != "n" and play != "no":
            play = input("Would you like to play? Y/N")
            if play == "y" or play == "yes":
                hangman()
                
            elif play == "n" or play == "no":
                print("Play when you're ready")
gameplay()