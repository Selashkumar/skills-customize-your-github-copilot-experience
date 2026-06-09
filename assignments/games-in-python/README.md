
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a Hangman game in Python that lets players guess letters to reveal a hidden word while tracking remaining attempts.

## 📝 Tasks

### 🛠️ Implement the Hangman game logic

#### Description

Write a Python program that selects a secret word from a predefined list, accepts letter guesses from the player, and displays the current word progress.

#### Requirements
Completed program should:

- Randomly choose a word from a predefined list
- Display the secret word progress using underscores for unguessed letters
- Accept one letter guess at a time
- Track and show incorrect guesses remaining
- Prevent repeated guesses from counting against the player
- Display a win message when the full word is guessed
- Display a lose message when attempts are exhausted

### 🛠️ Improve the user experience

#### Description

Add clear game messages and input handling so the player knows their progress and remaining chances.

#### Requirements
Completed program should:

- Show the current guessed word after each valid guess
- Show the letters guessed so far
- Validate input to accept only a single alphabetic character
- Handle invalid input gracefully with a helpful message
- End the game cleanly after win or loss
