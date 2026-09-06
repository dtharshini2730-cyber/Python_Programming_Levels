"""
Question 15:
Write a program to get a number from the user. If the first digit
is even, print the same number. If the first digit is odd,
subtract 1 from the first digit and print the number.
"""

n = input("Enter number: ")

first = int(n[0])

if first % 2 == 0:
    print(n)
else:
    print(str(first - 1) + n[1:])