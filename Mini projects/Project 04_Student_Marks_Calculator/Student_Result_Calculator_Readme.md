# 🎓 Student Result & Grade Calculator – Python Project

## 💡 Project Overview

This is a beginner-friendly, command-line Python application that collects subject names and marks from a user, validates all inputs, calculates the total marks, overall percentage, and final grade, and prints a neatly formatted Result Card.

## 🎯 Aim

The aim of this project is to build a reliable Student Result Card generator in Python to practice working with lists, input validation (`try-except`), nested loops, built-in math functions, and string alignment formatting.

## ⚙️ Features

1. **Dynamic Subject Entry:** Allows the user to enter any number of subjects (minimum 1).
2. **Robust Input Validation:** Ensures the subject count is a positive integer and marks fall strictly between `0` and `100`, catching non-numeric inputs gracefully without crashing.
3. **Automatic Calculations:** Computes total marks out of `n * 100` and calculates the overall percentage.
4. **Grade Assignment:** Automatically assigns grades (`A+`, `A`, `B`, `C`, `D`, or `F`) based on the calculated percentage.
5. **Formatted Result Card:** Displays subject-wise marks, total score, percentage, and final grade in a clean, aligned terminal layout.

## 🛠️ Technologies Used

* **Language:** Python 3
* **Environment:** VS Code / Any Python IDE

## 🔑 Key Concepts Used

* **Lists (`subjects`, `marks`):** Stores subject names and corresponding scores dynamically using `.append()`.
* **Exception Handling (`try-except ValueError`):** Prevents crashes when a user enters letters or symbols instead of numbers.
* **Nested Loops (`for` and `while True`):** Iterates through each subject while repeatedly prompting until valid marks are entered.
* **Range Comparison (`0 <= score <= 100`):** Validates that entered marks stay within valid bounds.
* **Built-in Functions (`sum()`, `range()`):** Calculates the sum of all marks and controls iteration.
* **Conditional Statements (`if-elif-else`):** Determines the student's final grade based on percentage thresholds.
* **String Alignment & Formatting (`f-strings`):** Uses `:<20` for left-aligning subject names and `:>.2f` for right-aligning scores to two decimal places.

## 📚 What I Learned

* How to store and sync parallel data across two Python lists.
* How to write crash-proof user inputs using `while True` combined with `try-except`.
* How to align text columns cleanly in the terminal using `f-string` format specifiers.
* How to structure real-world grading logic using `if-elif-else` statements.

## 🚀 How to Run

1. Make sure you have **Python 3** installed on your system.
2. Save the code as `result_calculator.py` (or download it from the repository).
3. Open a terminal in the project folder and run:

   ```bash
   python result_calculator.py
   ```