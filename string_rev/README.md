# Rooftop Assessment - Question 5: string_rev

## Overview
This folder contains the solution for **Question 5** of the Rooftop Practical Assessment.  
The goal of this question is to reverse a string without built-in reverse methods.

## How to Run the Scripts

All scripts are written in Python. To run a script:

1. Open terminal in the project folder.
2. Ensure Python is installed:

```bash
python --version

Run the script using
python <folder_name>/<script_name>.py

## Thought process
Implemented a manual stack using a list.

Pushed characters, then popped to get reversed string.

Used the standard if __name__ == "__main__": check to ensure the script runs only when executed directly.

Alternative Methods:

Could use indexing like s[::-1], but forbidden.

Stack approach follows constraints and demonstrates understanding.