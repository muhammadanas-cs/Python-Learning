# 🎲 Number Guessing Game – Python Project

## 💡 Project Overview

This is a fun, beginner-friendly command-line Python game where the computer picks a secret random number between 1 and 100, and the player tries to guess it in as few attempts as possible.

## 🎯 Aim

The aim of this project is to build an interactive guessing game in Python to practice using the `random` module, infinite loops (`while True`), conditional statements, and user input handling.

## ⚙️ Features

1. **Random Number Generation:** Automatically picks a hidden number between `1` and `100`.
2. **Smart Hints:** Tells the player whether their guess is `"Too low!"` or `"Too high!"`.
3. **Attempt Counter:** Tracks and displays the total number of tries taken to guess the right number.
4. **Loop Control:** Keeps the game running smoothly until the player wins and exits via `break`.

## 🛠️ Technologies Used

* **Language:** Python 3
* **Built-in Module:** `random`
* **Environment:** VS Code / Any Python IDE

## 🔑 Key Concepts Used

* **`random` Module (`random.randint()`):** Generates a random integer within a specified range (`1` to `100`).
* **While Loop (`while True`):** Creates a continuous game loop until the correct guess is made.
* **Break Statement (`break`):** Exits the loop immediately once the player guesses correctly.
* **Conditional Statements (`if-elif-else`):** Compares the player's guess with the target number to provide hints.
* **Type Casting (`int()`):** Converts string user input into an integer for numerical comparison.
* **Counter Variable (`tries += 1`):** Increments the attempt count on every valid guess.
* **Formatted Strings (`f-string`):** Cleanly displays the final score and attempts count.

## 📚 What I Learned

* How to import and use Python's built-in `random` module.
* How to control infinite loops using the `break` statement.
* How to track state across loop iterations using a counter variable.
* How to format dynamic output messages using Python `f-strings`.

## 🚀 How to Run

1. Make sure you have **Python 3** installed on your system.
2. Save the code as `guess_game.py` (or download it from the repository).
3. Open a terminal in the project folder and run:

   ```bash
   python guess_game.py
   ```