# Rooftop Assessment - Question 7: fizzBuzz

## Overview
This folder contains the solution for **Question 7** of the Rooftop Practical Assessment.  
The goal of this question is to print numbers 1–100, replacing multiples of 3/5 with "Fizz"/"Buzz".

## How to Run the Scripts

All scripts are written in Python. To run a script:

1. Open terminal in the project folder.
2. Ensure Python is installed:

```bash
python --version

Run the script using
python <folder_name>/<script_name>.py

## Thought process
Used modulo % to check divisibility.

Checked 3 & 5 first, then 3, then 5.

Used the standard if __name__ == "__main__": check to ensure the script runs only when executed directly.

Alternative Methods:

Could use lists or join, but simple loops are sufficient and readable.