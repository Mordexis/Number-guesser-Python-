import random
#Improved version of hangman
#Added three levels of difficulty

word1 = ["one", "and", "ant", "art", "fat", "fad", "top", "pot", "pet", "pit", "pig", "hip", "hot", "fart", "tart", "cart", "mast", "tact", "tick", "dues", "sued", "push", "hush", "rush", "husk", "pick", "coat", "cyst", "bats", "stabs", "track", "toast", "alpha", "bravo", "delta", "x-ray", "force", "tusks", "crust", "rusty", "focus", "pushy", "soaps", "ghost", "kills", "skill", "rifts", "first", "fires"]

word2 = ["trusts", "bushes", "golden", "spirits", "lyrics", "music", "gilded", "psycho", "mastered", "custard", "starter", "chanced", "children", "skillet", "skillset", "stylist", "hedges", "forrests", "magasines", "scales", "yachts", "stacks", "flasks", "baskets", "chorus"]

word3 = ["encrusted", "vernacular", "spectacular", "enterprise", "specialist", "direst", "spiralling", "swiftly", "development", "fingerprints", "nonsense", "gorillas", "onomatopoeia", "helicopter", "bazooka", "judiciary", "legislative", "reflection", "entertainment"]


def hangman_easy_mode():
    word = random.choice(word1)
    letters_to_guess = list(word)
    guessed_letters = []
    guessed_words = []
    correct_guesses = []
    tries = 6
    guessed = False
    print("You selected easy mode")
    
    while guessed == False and tries >0:
        progress = [letter if letter in correct_guesses else "_" for letter in letters_to_guess]
        print("Your current progress is", " ".join(progress))
        print("You've guessed the following words:", ", ".join(guessed_words))
        print("You've guessed the following characters:", ", ".join(guessed_letters))
        print(f"You have {tries} tries left")
        
        guess = input("Please guess a letter").lower()
        
        if guess in guessed_words or guess in guessed_letters:
            print(f"You've already guessed {guess}.")
            
        elif len(guess) == 1:
            if guess in letters_to_guess:
                print("Correct!")
                guessed_letters.append(guess)
                correct_guesses.append(guess)
                if set(correct_guesses) == set(letters_to_guess):
                    guessed = True
                    
            else:
                print("Incorrect!")
                guessed_letters.append(guess)
                tries -=1
                
        elif len(guess) == len(word):
            if guess == word:
                print("Amazing!")
                guessed = True
                
                
            else:
                print("Incorrect")
                guessed_words.append(guess)
                tries -= 1
                
        else:
            print("Invalid input")
            
            
        
        if guessed == True:
            print("Congratulations you win!")
            
        elif tries == 0:
            print(f"You lose! The word was {word}")
            
def hangman_medium_mode():
    word = random.choice(word2)
    letters_to_guess = list(word)
    guessed_letters = []
    guessed_words = []
    correct_guesses = []
    tries = 7
    guessed = False
    print("You selected medium mode")
    
    while guessed == False and tries >0:
        progress = [letter if letter in correct_guesses else "_" for letter in letters_to_guess]
        print("Your current progress is", " ".join(progress))
        print("You've guessed the following words:", ", ".join(guessed_words))
        print("You've guessed the following characters:", ", ".join(guessed_letters))
        print(f"You have {tries} tries left")
        
        guess = input("Please guess a letter").lower()
        
        if guess in guessed_words or guess in guessed_letters:
            print(f"You've already guessed {guess}.")
            
        elif len(guess) == 1:
            if guess in letters_to_guess:
                print("Correct!")
                guessed_letters.append(guess)
                correct_guesses.append(guess)
                if set(correct_guesses) == set(letters_to_guess):
                    guessed = True
                    
            else:
                print("Incorrect!")
                guessed_letters.append(guess)
                tries -=1
                
        elif len(guess) == len(word):
            if guess == word:
                print("Amazing!")
                guessed = True
                
                
            else:
                print("Incorrect")
                guessed_words.append(guess)
                tries -= 1
                
        else:
            print("Invalid input")
            
            
        
        if guessed == True:
            print("Congratulations you win!")
            
        elif tries == 0:
            print(f"You lose! The word was {word}")
            

def hangman_hard_mode():
    word = random.choice(word3)
    letters_to_guess = list(word)
    guessed_letters = []
    guessed_words = []
    correct_guesses = []
    tries = 8
    guessed = False
    
    print("You selected hard mode")
    
    while guessed == False and tries >0:
        progress = [letter if letter in correct_guesses else "_" for letter in letters_to_guess]
        print("Your current progress is", " ".join(progress))
        print("You've guessed the following words:", ", ".join(guessed_words))
        print("You've guessed the following characters:", ", ".join(guessed_letters))
        print(f"You have {tries} tries left")
        
        guess = input("Please guess a letter").lower()
        
        if guess in guessed_words or guess in guessed_letters:
            print(f"You've already guessed {guess}.")
            
        elif len(guess) == 1:
            if guess in letters_to_guess:
                print("Correct!")
                guessed_letters.append(guess)
                correct_guesses.append(guess)
                if set(correct_guesses) == set(letters_to_guess):
                    guessed = True
                    
            else:
                print("Incorrect!")
                guessed_letters.append(guess)
                tries -=1
                
        elif len(guess) == len(word):
            if guess == word:
                print("Amazing!")
                guessed = True
                
                
            else:
                print("Incorrect")
                guessed_words.append(guess)
                tries -= 1
                
        else:
            print("Invalid input")
            
            
        
        if guessed == True:
            print("Congratulations you win!")
            
        elif tries == 0:
            print(f"You lose! The word was {word}")
            
            


def gameplay():
    keep_play = "yes"
    while keep_play != "n" and keep_play != "no":
        keep_play = input("Would you like to play? Y/N").lower()
        
        if keep_play == "y" or keep_play == "yes":
            while keep_play == "y" or keep_play == "yes":
                level_selector = input("Please select your level of difficulty. \n 1. Easy \n 2. Medium \n 3. Hard").lower()
            
                if level_selector == "1" or level_selector == "e" or level_selector == "easy":
                    hangman_easy_mode()
                    break
                
                elif level_selector == "2" or level_selector == "m" or level_selector == "medium":
                    hangman_medium_mode()
                    break
                
                elif level_selector == "3" or level_selector == "h" or level_selector == "hard":
                    hangman_hard_mode()
                    break
                
                else:
                    print("Invalid input!")
                

            
            
            if keep_play == "n" or keep_play == "no":
                print("Thanks for playing")
                break
            
        else:
            print("Inalid input")
            

            
            
    if keep_play == "n" or keep_play == "no":
        print("Play when you're ready")
            
gameplay()
            
            