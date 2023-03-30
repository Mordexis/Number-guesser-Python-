words = ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "india", "juliett", "kilo", "lima", "mike", "november", "uniform", "victor", "whiskey", "x-ray", "yankee", "zulu"]
import random
# Very poor version of hangman


def hangman():


    word = random.choice(words)

    letters_to_guess = set(word)

    guessed_letters= set()

    correct_guess = set()

    tries = 10



    while tries >0 and len(letters_to_guess)>0:

        guess = input("Please guess a letter").lower()


        progress = [letter if letter in correct_guess  else "- " for letter in word]



        if guess in guessed_letters:
            print("Already guessed")
            print(f"You have used these letters, {guessed_letters}")
            print(f"Your current progress is {progress}")
            print(f"You have {tries} tries left")


        elif guess in letters_to_guess:
            letters_to_guess.remove(guess)
            guessed_letters.add(guess)

            correct_guess.add(guess)
            print(f"You have used these letters, {guessed_letters}")
            print(f"Your current progress is {progress}")
            print(f"You have {tries} tries left")


        else:
            print("Wrong")
            tries -=1
            print(f"You have used these letters, {guessed_letters}")
            print(f"Your current progress is {progress}")
            print(f"You have {tries} tries left")
            guessed_letters.add(guess)


    if tries == 0:
        print(f"You lose the word was {word}")
        print(f"The word was {word}")

    elif len(letters_to_guess) == 0:
        print("You won!")
        print(f"The word was {word}")

hangman()


