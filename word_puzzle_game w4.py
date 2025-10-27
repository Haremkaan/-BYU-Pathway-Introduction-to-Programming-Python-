# W04 Project: Word Puzzle Game
# Description: This program is an interactive word guessing game similar to Wordle.
# The user tries to guess the secret word and receives hints after each guess.
# Extra Feature: The secret word is randomly chosen from a list, so each game is different.

import random

print("Welcome to the word guessing game!")
print("Try to guess the secret word. Hints will guide you.")
print()

# Randomly choose a secret word from a list
word_list = ["mosiah", "temple", "moroni", "nephi", "helaman", "alma"]
secret_word = random.choice(word_list)

guess = ""
guess_count = 0

# Show the initial hint
print("Your hint is: " + " ".join(["_"] * len(secret_word)))

while guess != secret_word:
    guess = input("\nWhat is your guess? ").lower()
    guess_count += 1

    if guess == secret_word:
        break

    if len(guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word.")
        continue

    # Generate hint
    hint = []
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hint.append(guess[i].upper())
        elif guess[i] in secret_word:
            hint.append(guess[i].lower())
        else:
            hint.append("_")
    print("Your hint is: " + " ".join(hint))

print("\nCongratulations! You guessed it!")
print(f"It took you {guess_count} guesses.")
