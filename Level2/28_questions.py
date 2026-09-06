"""
Question 28:
Write a program to get two numbers from the user and print
the LCM of those numbers.
"""

a, b = map(int, input("Enter two numbers: ").split())

for i in range(1, a * b + 1):
    if i % a == 0 and i % b == 0:
        print(i)
        break