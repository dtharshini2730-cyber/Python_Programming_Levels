"""
Question 10:
Get a three-digit number from the user and print the sum
of all digits.
"""

n = int(input("Enter number: "))

a = n // 100
b = (n // 10) % 10
c = n % 10

print(a + b + c)