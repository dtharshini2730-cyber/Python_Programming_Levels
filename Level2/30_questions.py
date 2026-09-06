"""
Question 30:
Write a program to get two numbers from the user and print
the HCF of those numbers.
"""

a, b = map(int, input("Enter two numbers: ").split())

for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        break