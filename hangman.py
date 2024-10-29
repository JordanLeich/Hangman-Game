import random
import time
import colors

# Extensive word categories
categories = {
    "animals": ["dog", "elephant", "giraffe", "lion", "zebra", "crocodile", "dolphin", "kangaroo", "panda", "tiger"],
    "countries": ["canada", "france", "brazil", "japan", "germany", "australia", "mexico", "india", "egypt", "italy"],
    "movies": ["inception", "titanic", "avatar", "gladiator", "matrix", "avengers", "godfather", "jaws", "frozen", "rocky"],
    "fruits": ["apple", "banana", "grape", "mango", "orange", "pear", "peach", "cherry", "kiwi", "pineapple"],
    "colors": ["red", "blue", "green", "yellow", "purple", "orange", "black", "white", "brown", "pink"],
    "sports": ["soccer", "basketball", "baseball", "tennis", "cricket", "hockey", "volleyball", "golf", "boxing", "rugby"],
    "vehicles": ["car", "truck", "motorcycle", "airplane", "helicopter", "bicycle", "boat", "train", "scooter", "submarine"],
    "musical_instruments": ["guitar", "piano", "drums", "violin", "flute", "trumpet", "saxophone", "harmonica", "cello", "clarinet"],
    "planets": ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto"],
    "languages": ["english", "spanish", "french", "german", "chinese", "japanese", "hindi", "arabic", "russian", "portuguese"]
}

# Add a random category for selection
categories["random"] = [word for category in categories.values() for word in category]  # Combine all words

# Hangman visual stages
HANGMAN_PICS = [''' 
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\\  |
      |
     ===''', '''
  +---+
  O   |
 /|\\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\\  |
 / \\  |
     ===''']

# Functions

def validate_guess(guess):
    """Check if the guess is valid (1 alphabet character)."""
    if guess.isalpha() and len(guess) == 1:
        return True
    else:
        print(colors.red + "Invalid input! Please enter a single alphabet letter." + colors.reset)
        return False

def choose_category():
    """Let the player choose a category of words to play."""
    while True:
        print("\nAvailable categories:")
        for category in categories:
            print(f"- {category.capitalize()}")
        category = input("\nChoose a category (or type 'random' for a random selection): ").lower()
        if category in categories:
            return random.choice(categories[category])
        else:
            print(colors.red + "Invalid category. Please try again." + colors.reset)

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

def display_hangman(lives):
    """Display the current state of the hangman based on lives remaining."""
    print(HANGMAN_PICS[6 - lives])

def display_game_status(guessed_word, lives, guessed):
    """Print the current game status including guessed word, lives left, and guessed letters."""
    print(" ".join(guessed_word))
    print(f"Lives left: {lives}")
    print(f"Guessed letters: {', '.join(guessed)}")

def use_hint(guessed_word, word_in_list, lives):
    """Offer a hint at the cost of 1 life."""
    if lives > 1:
        lives -= 1
        for i, letter in enumerate(word_in_list):
            if guessed_word[i] == "_":
                guessed_word[i] = letter
                break
        print(colors.blue + f"Hint used! A letter has been revealed: {' '.join(guessed_word)}" + colors.reset)
    else:
        print(colors.red + "Not enough lives to use a hint!" + colors.reset)
    return lives

def save_score(wins, losses):
    """Save the player's win/loss record to a file."""
    with open("scores.txt", "w") as file:
        file.write(f"Wins: {wins}, Losses: {losses}")

def load_score():
    """Load the player's win/loss record from a file."""
    try:
        with open("scores.txt", "r") as file:
            data = file.read().split(',')
            wins = int(data[0].split(': ')[1])
            losses = int(data[1].split(': ')[1])
    except FileNotFoundError:
        wins, losses = 0, 0
    return wins, losses

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

# Main Game Function
def game():
    wins, losses = load_score()  # Load previous scores
    word = choose_category()
    guessed_word = list("_" * len(word))
    word_in_list = list(word)
    guessed_letters = []

    lives = choose_difficulty()

    while lives > 0:
        display_hangman(lives)
        display_game_status(guessed_word, lives, guessed_letters)

        guess = input("Guess a letter or the full word (or type 'hint' to use a hint, 'exit' to quit): ").lower()

        if guess == "exit":
            print(colors.red + "Thanks for playing! Exiting game..." + colors.reset)
            quit()

        if guess == "hint":
            lives = use_hint(guessed_word, word_in_list, lives)
            continue

        # Check for full word guess
        if len(guess) > 1:
            if guess == word:
                print(colors.green + "You guessed the word correctly!" + colors.reset)
                wins += 1
                print(f"Win Counter: {wins}")
                save_score(wins, losses)
                if restart_game():
                    game()
                else:
                    quit()
            else:
                lives -= 1
                print(colors.red + "Wrong guess! That was not the correct word." + colors.reset)
                if lives == 0:
                    print(colors.red + "Game Over! The correct word was: " + ''.join(word_in_list) + colors.reset)
                    losses += 1
                    save_score(wins, losses)
                    if restart_game():
                        game()
                    else:
                        quit()
            continue  # Skip to next iteration after full word guess

        # Validate single letter guess
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
                wins += 1
                print(f"Win Counter: {wins}")
                save_score(wins, losses)
                if restart_game():
                    game()
                else:
                    quit()
        else:
            lives -= 1
            print(colors.red + "Wrong guess!" + colors.reset)
            if lives == 0:
                print(colors.red + "Game Over! The correct word was: " + ''.join(word_in_list) + colors.reset)
                losses += 1
                save_score(wins, losses)
                if restart_game():
                    game()
                else:
                    quit()

# Start the game
if __name__ == "__main__":
    game()
