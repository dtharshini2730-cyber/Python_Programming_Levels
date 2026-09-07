"""
Question 17:
Write a program to print the sum of all single-digit
odd numbers.
"""

sum = 0

for i in range(1, 10):
    if i % 2 != 0:
        sum = sum + i

print(sum)