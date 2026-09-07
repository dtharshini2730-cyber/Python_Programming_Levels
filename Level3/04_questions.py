"""
Question 4:
Get a number from user and check whether it is prime or not,
then print the result.
"""

n = int(input("Enter number: "))

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1

if count == 2:
    print("Number is Prime")
else:
    print("Number is not Prime")