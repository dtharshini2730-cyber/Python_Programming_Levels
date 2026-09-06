"""
Question 27:
Write a program to print the total count of numbers less than
100000 whose sum of digits is 14.
"""

count = 0

for i in range(100000):
    n = i
    sum = 0

    while n > 0:
        sum = sum + n % 10
        n = n // 10

    if sum == 14:
        count = count + 1

print(count)