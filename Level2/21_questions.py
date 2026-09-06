"""
Question 21:
Write a program to get a number from the user and print
the total number of digits that are odd.
"""

n = input("Enter number: ")

count = 0

for i in n:
    if int(i) % 2 != 0:
        count = count + 1

print(count)