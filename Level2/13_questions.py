"""
Question 13:
Write a program to get a number from the user and print
the reverse of that number.
"""

n = int(input("Enter number: "))

rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10

print(rev)