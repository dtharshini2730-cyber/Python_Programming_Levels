"""
Question 16:
Write a program to get a number from the user and print
whether that number is prime or not.
"""

n = int(input("Enter number: "))

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1

if count == 2:
    print("Prime")
else:
    print("Not Prime")