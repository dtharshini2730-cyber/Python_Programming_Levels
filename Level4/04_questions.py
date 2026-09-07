"""
Question 4:
Get a three-digit number from the user and print the digit
in the ten's position.
"""

n = int(input("Enter number: "))

print((n // 10) % 10)