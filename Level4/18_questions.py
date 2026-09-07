"""
Question 18:
Write a program to print the sum of all two-digit
odd numbers.
"""

sum = 0

for i in range(10, 100):
    if i % 2 != 0:
        sum = sum + i

print(sum)