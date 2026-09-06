"""
Question 22:
Write a program to get a number from the user and print
the total number of two-digit odd numbers in the number.
"""

n = input("Enter number: ")

count = 0

for i in range(len(n) - 1):
    x = int(n[i:i+2])

    if x >= 10 and x % 2 != 0:
        count = count + 1

print(count)