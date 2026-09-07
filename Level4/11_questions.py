"""
Question 11:
Get a four-digit number from the user and print the sum
of all digits.
"""

n = int(input("Enter number: "))

a = n // 1000
b = (n // 100) % 10
c = (n // 10) % 10
d = n % 10

print(a + b + c + d)