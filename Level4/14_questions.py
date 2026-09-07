"""
Question 14:
Write a program to print the total number of single-digit
odd numbers.
"""

count = 0

for i in range(1, 10):
    if i % 2 != 0:
        count = count + 1

print(count)