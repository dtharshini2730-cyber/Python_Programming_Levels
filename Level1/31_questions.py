"""
Problem 31

Question:
Get a three-digit number from user.
If the sum of the digits is less than 10,
then print the sum.

Otherwise add the digits of the sum and continue
until the result is a single digit.

Testcase:
Input: 123
Output: 6

Input: 149
Output: 5

Input: 991
Output: 1
"""
n = int(input())
a = n // 100
b = (n // 10) % 10
c = n % 10
s = a + b + c
while s >= 10:
    s = s // 10 + s % 10
print(s)