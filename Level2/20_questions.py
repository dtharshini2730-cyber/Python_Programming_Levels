"""
Question 20:
Write a program to print the total number of single-digit
prime numbers.
"""

count = 0

for i in range(1, 10):
    if i == 2 or i == 3 or i == 5 or i == 7:
        count = count + 1

print(count)