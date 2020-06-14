# Hangman game, Created by: ThomasMatt, Updated by: Jordan Leich. Email me at jordanleich@gmail.com if you wish to
# code together

# Imports
import random
import time


def validate(guesses):
    # check guess is 1 char long and guess is in the alphabet
    if guesses.isalpha() and len(guesses) == 1:
        return True
    else:
        return False


# Word list
words = ["jazz", "apple", "character", "rhythm", "piano", "butterfly", "car", "pajama", "kayak", "zigzag", "zombie",
         "oxygen", "able", "baby", "lock", "ornament", "quality", "liquid", "suggestion", "weather", "twist"]

word = random.choice(words)
# word stored as a variable
guessed = []
# guessed is a list
Guessed_Word = list(len(word) * "_")

Word_In_List = list(word)
lives = 12

while True:
    if lives == 0:
        print("Game Over!")
        print()
        time.sleep(2)
        print("The correct word was", Word_In_List)
        print()
        time.sleep(4)
        break
    # If lives is = 0 then print game over and break out of the loop
    elif Guessed_Word == Word_In_List:
        print("You guessed it!")
        print()
        time.sleep(2)
        print("The correct word is", Word_In_List)
        print()
        time.sleep(4)
        break
    # check if the guessed word is correct, if it is print well done, if not break out of the loop
    print(" ".join(Guessed_Word))
    # print guessed word all together with __ for each missing letter
    print("Lives left: %d" % lives)
    # print the number of lives left over
    guess = input("Guess: ")
    print()
    while not validate(guess):
        guess = input("Guess: ")
        print()

    if guess not in guessed:
        # if the guess input is not in the guessed list
        guessed.append(guess)
        # add letter to the guess list
        if guess not in Word_In_List:
            lives = lives - 1
        # if it is a new guess and it is not in the list
        else:
            for i in range(0, len(Word_In_List)):
                if guess == Word_In_List[i]:
                    # [i] counts along the position to check if the guess matches any of the letter
                    Guessed_Word[i] = guess

    else:
        print("You have already guessed that letter! No lives charged!")
        print()
        # if that letter has been guessed inform them and don't take a life off them
