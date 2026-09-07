"""
Question 19:
Write a program to print the sum of all three-digit
odd numbers.
"""

sum = 0

for i in range(100, 1000):
    if i % 2 != 0:
        sum = sum + i

print(sum)