"""
Question 17:
Write a program to get a number from the user, print whether
that number is prime, and check whether the sum of its digits
is equal to 14.
"""

n = int(input("Enter number: "))

count = 0
sum = 0
temp = n

for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1

while temp > 0:
    sum = sum + temp % 10
    temp = temp // 10

if count == 2 and sum == 14:
    print("Prime & Sum of Digits is 14")
elif count != 2 and sum == 14:
    print("Not Prime but sum of digits is 14")
elif count == 2:
    print("Prime, but sum of Digits is not 14")
else:
    print("Not Prime and sum of Digits is not 14")