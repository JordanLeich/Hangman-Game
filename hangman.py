# Hangman game, Created by: ThomasMatt, Updated by: Jordan Leich. Email me at jordanleich@gmail.com if you wish to
# code together

# Imports
import random
import time
import colors
import words

wincount = 0
lives = 0


def validate(guesses):
    global lives, wincount
    # check guess is 1 char long and guess is in the alphabet
    if guesses.isalpha() and len(guesses) == 1:
        return True
    else:
        return False


def restart():
    question = input('Want to play again (yes or no): ')
    print()

    if question.lower() == 'y' or question.lower() == 'yes':
        game()

    else:
        quit()


def game():
    global lives, wincount
    word = random.choice(words.words)
    guessed = []
    # guessed is a list
    Guessed_Word = list(len(word) * ".")
    Word_In_List = list(word)

    lives = int

    difficulty = input(""" 
Easy = 12 Lives
Medium = 9 Lives
Hard = 6 Lives
Impossible = 3 Lives
Choose a difficulty: """)
    print()

    if difficulty.lower() == 'easy' or difficulty.lower() == 'e':
        lives = 12
    elif difficulty.lower() == 'medium' or difficulty.lower() == 'm':
        lives = 9
    elif difficulty.lower() == 'hard' or difficulty.lower() == 'h':
        lives = 6
    elif difficulty.lower() == 'impossible' or difficulty.lower() == 'i':
        lives = 3

    else:
        print(colors.red + 'difficulty error caught...' + colors.reset)
        game()

    while True:
        if lives == 0:
            print(colors.red + "Game Over!\n" + colors.reset)
            time.sleep(1)
            print(colors.green + "The correct word is", Word_In_List, '\n' + colors.reset)
            time.sleep(1)
            wincount -= 1
            print("Win Counter: ", wincount)
            print()
            time.sleep(1)
            restart()
        # If lives is = 0 then print game over and break out of the loop
        elif Guessed_Word == Word_In_List:
            print(colors.green + "You guessed it!\n" + colors.reset)
            time.sleep(1)
            print(colors.green + "The correct word is", Word_In_List, '\n' + colors.reset)
            time.sleep(1)
            wincount += 1
            print("Win Counter: ", wincount)
            print()
            time.sleep(1)
            restart()
        # check if the guessed word is correct, if it is print well done, if not break out of the loop
        print()
        print(" ".join(Guessed_Word))
        # print guessed word all together with __ for each missing letter
        print("Lives left: ", lives)
        # print the number of lives left over
        guess = input("Guess the letter: ")
        print()
        while not validate(guess):
            print(colors.red + 'Invalid Guess, Try again...\n' + colors.reset)
            guess = input("Guess the letter: ")
            print()

        if guess not in guessed:
            # if the guess input is not in the guessed list
            guessed.append(guess)
            # add letter to the guess list
            if guess not in Word_In_List:
                lives -= 1
            # if it is a new guess and it is not in the list
            else:
                for i in range(0, len(Word_In_List)):
                    if guess == Word_In_List[i]:
                        # [i] counts along the position to check if the guess matches any of the letter
                        Guessed_Word[i] = guess

        else:
            print(colors.red + "You have already guessed that letter! No lives charged!", colors.reset)
            # if that letter has been guessed inform them and don't take a life off them


game()
