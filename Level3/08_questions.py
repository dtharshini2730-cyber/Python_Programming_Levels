"""
Question 8:
Get a number from user and check whether its digits are
in ascending order.
"""

n = input("Enter number: ")

if list(n) == sorted(n):
    print("Yes")
else:
    print("No")