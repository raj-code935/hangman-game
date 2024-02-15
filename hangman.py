#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

# List of secret words (fruit names)
SECRET_WORDS = ["apple", "banana", "orange", "mango", "grape", "kiwi", "pear"]

def select_word(secret_words):
    """Selects a random word from the list of secret words."""
    return random.choice(secret_words)

def display_word(word, guessed_letters):
    """Displays the word with guessed letters revealed."""
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()

def play_hangman():
    """Main function to play the Hangman game."""
    word = select_word(SECRET_WORDS)
    guessed_letters = []
    chances = len(word) + 2  # Add 2 additional chances
    print("Welcome to Hangman! Try to guess the fruit name.")

    while chances > 0:
        print("\nChances left:", chances)
        print("Word:", display_word(word, guessed_letters))

        if display_word(word, guessed_letters).replace(" ", "") == word:
            print("Congratulations! You guessed the word:", word)
            break

        guess = input("Guess a letter: ").lower()
        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You've already guessed that letter.")
            elif guess in word:
                print("Correct guess!")
                guessed_letters.append(guess)
            else:
                print("Incorrect guess.")
                chances -= 1
        else:
            print("Please enter a valid single letter.")

    if chances == 0:
        print("Sorry, you've run out of chances. The word was:", word)

# Start the game
play_hangman()


# In[ ]:




