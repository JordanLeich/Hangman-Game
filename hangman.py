import random
import time
import colors
import words


def validate_guess(guess):
    """Check if the guess is valid (1 alphabet character)."""
    if guess.isalpha() and len(guess) == 1:
        return True
    else:
        print(colors.red + "Invalid input! Please enter a single alphabet letter." + colors.reset)
        return False


def choose_difficulty():
    """Prompt the player to select a difficulty level and return corresponding lives."""
    difficulties = {"easy": 12, "medium": 9, "hard": 6, "impossible": 3}
    while True:
        difficulty = input("""
Easy = 12 Lives
Medium = 9 Lives
Hard = 6 Lives
Impossible = 3 Lives
Choose a difficulty: """).lower()
        if difficulty in difficulties:
            return difficulties[difficulty]
        else:
            print(colors.red + 'Invalid difficulty. Please try again.' + colors.reset)


def display_game_status(guessed_word, lives, guessed):
    """Print the current game status including guessed word, lives left, and guessed letters."""
    print(" ".join(guessed_word))
    print(f"Lives left: {lives}")
    print(f"Guessed letters: {', '.join(guessed)}")


def restart_game():
    """Ask if the player wants to restart the game."""
    while True:
        question = input('Want to play again (yes or no): ').lower()
        if question in ['yes', 'y']:
            return True
        elif question in ['no', 'n']:
            return False
        else:
            print(colors.red + "Invalid input. Please answer 'yes' or 'no'." + colors.reset)


def game():
    """Main game loop for playing Hangman."""
    word = random.choice(words.words)
    guessed_word = list("_" * len(word))
    word_in_list = list(word)
    guessed_letters = []
    win_count = 0

    lives = choose_difficulty()

    while lives > 0:
        display_game_status(guessed_word, lives, guessed_letters)
        
        guess = input("Guess a letter: ").lower()

        if not validate_guess(guess):
            continue
        
        if guess in guessed_letters:
            print(colors.yellow + "You've already guessed that letter! No lives lost." + colors.reset)
            continue

        guessed_letters.append(guess)

        if guess in word_in_list:
            for i, letter in enumerate(word_in_list):
                if letter == guess:
                    guessed_word[i] = guess
            if guessed_word == word_in_list:
                print(colors.green + "You guessed the word correctly!" + colors.reset)
                win_count += 1
                print(f"Win Counter: {win_count}")
                if restart_game():
                    game()
                else:
                    quit()
        else:
            lives -= 1
            print(colors.red + "Wrong guess!" + colors.reset)
            if lives == 0:
                print(colors.red + "Game Over! The correct word was: " + ''.join(word_in_list) + colors.reset)
                if restart_game():
                    game()
                else:
                    quit()


if __name__ == "__main__":
    game()