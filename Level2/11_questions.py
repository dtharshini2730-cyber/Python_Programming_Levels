"""
Question 11:
Write a program to get a number from the user and print the total number of digits in that number.
"""

n = int(input("Enter number: "))

count = 0

while n > 0:
    count = count + 1
    n = n // 10

print(count)