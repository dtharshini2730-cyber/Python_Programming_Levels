"""
Question 12:
Write a program to get a number from the user and print
the sum of all digits.
"""

n = int(input("Enter number: "))

sum = 0

while n > 0:
    sum = sum + n % 10
    n = n // 10

print(sum)