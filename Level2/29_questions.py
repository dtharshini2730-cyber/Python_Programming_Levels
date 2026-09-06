"""
Question 29:
Write a program to get three numbers from the user and print
the LCM of those numbers.
"""

a, b, c = map(int, input("Enter three numbers: ").split())

for i in range(1, a * b * c + 1):
    if i % a == 0 and i % b == 0 and i % c == 0:
        print(i)
        break