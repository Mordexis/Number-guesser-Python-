#This is a dice rolling game
import random
#● ┌ ─ ┐ │ └ ┘
#These are the building blocks for the die

die_face = ["┌─────────┐\n│         │\n│    ●    │\n│         │\n└─────────┘", "┌─────────┐\n│ ●       │\n│         │\n│       ● │\n└─────────┘", "┌─────────┐\n│ ●       │\n│    ●    │\n│       ● │\n└─────────┘", "┌─────────┐\n│ ●     ● │\n│         │\n│ ●     ● │\n└─────────┘", "┌─────────┐\n│ ●     ● │\n│    ●    │\n│ ●     ● │\n└─────────┘", "┌─────────┐\n│ ●     ● │\n│ ●     ● │\n│ ●     ● │\n└─────────┘"]
             
#These are all the faces of the dice

Number_of_rolls = int(input("How many times would you like to roll the die"))

total = 0
#This is used to track your total rolled

for x in range (0, Number_of_rolls):
    #for loop used so that you roll the number of times entered
    dice = random.randint(1, 6)
    #used to randomly roll a number between 1 and 6
    face = dice -1
    # used to access the face stored in the list called die_face
    print(die_face[face])
    print(f"You rolled a {dice}")
    #done to show what you rolled
    total += dice

print(f"Your total was {total}")
#done to show what your total was
