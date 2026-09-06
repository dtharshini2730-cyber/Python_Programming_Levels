"""
Question 8:
Write a loop program to print the two-digit even numbers
whose sum of digits is 6.
"""

for i in range(10, 100, 2):
    a = i // 10
    b = i % 10

    if a + b == 6:
        print(i)