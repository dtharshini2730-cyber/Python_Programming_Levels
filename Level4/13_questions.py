"""
Question 13:
Get a number from the user and print the sum of all digits.
"""

n = input("Enter number: ")

sum = 0

for i in n:
    sum = sum + int(i)

print(sum)