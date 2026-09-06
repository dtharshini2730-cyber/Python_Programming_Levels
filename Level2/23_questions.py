"""
Question 23:
Write a program to get a number from the user and print
the total number of single-digit perfect square numbers
in the number.
"""

n = input("Enter number: ")

count = 0

for i in n:
    if i == '1' or i == '4' or i == '9':
        count = count + 1

print(count)