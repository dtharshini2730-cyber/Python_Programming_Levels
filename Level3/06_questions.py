"""
Question 6:
Get a number from user and reverse that number.
"""

n = int(input("Enter number: "))

reverse = 0

while n > 0:
    reverse = reverse * 10 + n % 10
    n = n // 10

print(reverse)