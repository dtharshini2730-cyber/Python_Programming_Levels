"""
Question 18:
Write a program to get a number from the user and print
whether the last two digits form a prime number.
"""

n = int(input("Enter number: "))

n = n % 100
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1

if count == 2:
    print("Prime")
else:
    print("Not Prime")