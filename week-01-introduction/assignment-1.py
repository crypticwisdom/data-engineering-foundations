"""
Docstring for assignments.intro


Assignment:
Python Basics Assignment
Objective

Practice:

- Creating a Python file
- Using comments
- Printing output
- Receiving user input
- Running a Python script

Instructions:
Create a Python file named: intro.py

At the top of the file, add a comment that includes:
- Your full name
- Today’s date
- A short sentence about what the program does

Example:

# Name: John Doe
# Date: 20-01-2026
# This program collects user details and prints them


Write a program that: Prints a welcome message

Asks the user for:
- Their name
- Their age
- Their favorite programming language
- Prints all the information back to the user in a clear sentence


Example output (format can vary):
Welcome to my first Python program!
What is your name?
How old are you? 26
What is your favorite programming language? Python

Hello George!
You are X years old and your favorite programming language is Python.

Rules:
Use print() for output
Use input() to receive user input
Add at least 3 comments in your code
The program must run without errors

Send the intro.py file

"""



# Name: George Okechukwu
# Date: 22-01-2026
# This program collects user details and prints them

# welcome message
print('welcome to my first python program!')

'''
I created variables to store needed information
'''
# Asking for information

name = input("what is your name?")
age = input("How old are you?")
favourite_language = input("What is your favourite programming language?")
    
# Printing all information back to the user in a clear sentence

print('Hello', name ,'!')
print('you are', age ,'years old')
print('your favourite programming language is',favourite_language)