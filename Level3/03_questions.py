"""
Question 3:
Get a number from user and check whether the sum of digits is 14,
then print the result.
"""

n = int(input("Enter number: "))

sum = 0

while n > 0:
    sum = sum + n % 10
    n = n // 10

if sum == 14:
    print("Sum of Digits is 14")
else:
    print("Sum of Digits is not 14")