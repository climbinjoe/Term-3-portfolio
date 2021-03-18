# Hangman Game
# Joseph Simper
# 10/20
# The classic game of Hangman.  The computer picks a random word
# and the player wrong to guess it, one letter at a time.  If the player
# can't guess the word in time, the little stick figure gets hanged.

#imports
import random

HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 |    +
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |    +
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\\
 |    +
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\\
 |    +
 |   |
 |   |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\\
 |    +
 |   | |
 |   | |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\\
 |    +
 |   | |
 |   | |
 |  ~-
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\\
 |    +
 |   | |
 |   | |
 |  ~- -~
 |
----------
""")

MAX_WRONG = len(HANGMAN) - 1
WORDS = ("OVERUSED", "CLAM", "GUAM", "TAFFETA", "PYTHON")
word=random.choice(WORDS)
#assignment
#10 python related terms
#be sure to define terms in comments
wrong = 0
used = []
so_far = "_"*len(word)

print("Welcome to Hangman.  Good luck!")

while wrong < MAX_WRONG and so_far != word:

    print(HANGMAN[wrong])
    print(so_far)


    guess = input("\n\neNTER YOUR GUESS:")
    guess = guess.upper()
    print(guess)

    while guess in used:
        print("You've already guessed the letter",guess)
        guess = input("Enter your guess:")
        guess = guess.upper()

    used.append(guess)
    
    if guess in word:
        print("\nYes,",guess,"is in word!")

        #create a new so_far to include guess in the
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new+=guess
            else:
                new+=so_far[i]
        so_far = new

    else:
        print("\nSorry,",guess,"isn't in word.")
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nYou failed!")
else:
    print("\nYou guessed it!")

print("\nThe word was",word)

input("\n\nPress the enter key to exit.")














