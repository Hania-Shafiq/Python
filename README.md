# Python Projects Collection

This repository contains a collection of small projects written in Python. Each project demonstrates fundamental programming concepts and provides practical applications. The projects included in this collection are:

## Projects

1. **Calculator**: A simple command-line calculator that can perform basic arithmetic operations such as addition, subtraction, multiplication, and division.

2. **Rock-Paper-Scissors Game**: A fun command-line game where the user can play against the computer in the classic rock-paper-scissors game.

3. **To-Do List**: A command-line application to manage tasks efficiently. Users can add, view, and remove tasks from their to-do list.

4. **Contact Book**: A simple application for storing and managing contacts. Users can add, search, and delete contacts easily.

5. **Password Generator**: A tool to generate strong, random passwords with various customization options for length and character types.
6. **Arithmetic Sequence Problem**:

### Problem Statement
Given the digits 0 to 9, find all increasing arithmetic sequences of five positive 2-digit integers that can be formed using each digit exactly once. For example, the sequence **09, 27, 45, 63, 81** is one such sequence, with a total sum of **225**. The task is to calculate the total of the sums of all valid arithmetic sequences.

### Implementation

The solution involves defining several functions:

1. **`get_digits(number)`**: 
   - Takes a number as input and returns its digits as a list of characters. This includes adding a leading zero for single-digit numbers.

2. **`uses_all_digits_once(seq)`**:
   - Checks if a given sequence of integers uses each digit from 0 to 9 exactly once. It ensures that the sequence contains exactly 10 unique digits, including '0'.

3. **`find_sequences()`**:
   - Main function that generates potential arithmetic sequences of five integers.
   - It iterates through all possible starting integers and common differences to form sequences.
   - For each sequence, it checks if the sequence uses all digits exactly once and calculates its sum if valid.
   - Prints each valid sequence along with its sum and keeps a running total of all sums.
 
