"""
Question 7:
Write a loop program to print the two-digit odd numbers
whose sum of digits is 7.
"""

for i in range(11, 100, 2):
    a = i // 10
    b = i % 10

    if a + b == 7:
        print(i)