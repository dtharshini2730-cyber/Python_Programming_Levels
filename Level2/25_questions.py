"""
Question 25:
Write a program to get a number from the user and print
the total number of single-digit prime numbers in the number.
"""

n = input("Enter number: ")

count = 0

for i in n:
    if i == '2' or i == '3' or i == '5' or i == '7':
        count = count + 1

print(count)