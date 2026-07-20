import random

# ==============================
# Project Information
# ==============================

GAME_NAME = "Hangman"
VERSION = "1.0"
DEVELOPER = "Pratham Pasi"
LANGUAGE = "Python"

# ==============================
# Hangman Pictures
# ==============================

HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

# ==============================
# Word List
# ==============================

WORDS = [
    "python",
    "computer",
    "developer",
    "keyboard",
    "variable",
    "function",
    "program",
    "internet",
    "software",
    "algorithm"
]


# ==============================
# Functions
# ==============================

def display_hangman(lives):
    """Display the current Hangman stage."""

    print(HANGMAN_PICS[6 - lives])


def display_word(secret_word, guessed_letters):
    """Display the current progress of the secret word."""

    word_guessed = True

    for letter in secret_word:

        if letter in guessed_letters:
            print(letter, end=" ")

        else:
            print("_", end=" ")
            word_guessed = False

    print()

    return word_guessed


def play_game():
    """Play one complete game of Hangman."""

    # Select a random word
    secret_word = random.choice(WORDS)

    # Store guessed letters
    guessed_letters = []

    # Total lives
    lives = 6

    while True:

        # Display Hangman
        display_hangman(lives)

        # Display current word
        word_guessed = display_word(secret_word, guessed_letters)

        # Check if player won
        if word_guessed:
            print("\n🎉 Congratulations! You guessed the word!")
            break

        # Take input
        guess = input("\nGuess a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Duplicate guess check
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        # Store guessed letter
        guessed_letters.append(guess)

        # Wrong guess
        if guess not in secret_word:
            lives -= 1
            print(f"\nWrong guess! Lives left: {lives}")

        # Lose condition
        if lives == 0:
            display_hangman(lives)
            print(f"\n💀 Game Over!")
            print(f"The secret word was: {secret_word}")
            break


def main():
    """Main function."""

    print("=" * 40)
    print(f"{GAME_NAME:^40}")
    print("=" * 40)
    print(f"Developer : {DEVELOPER}")
    print(f"Version   : {VERSION}")
    print("=" * 40)

    while True:

        play_game()

        play_again = input("\nDo you want to play again? (Y/N): ").upper()

        if play_again == "Y":
            print()
            continue

        elif play_again == "N":
            print("\nThanks for playing Hangman!")
            break

        else:
            print("\nInvalid input! Exiting game.")
            break


# ==============================
# Program Starts Here
# ==============================

if __name__ == "__main__":
    main()