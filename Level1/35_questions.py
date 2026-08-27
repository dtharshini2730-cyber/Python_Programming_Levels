"""
Problem 35

Question:
Get two 3-digit numbers from user.
Add the one's and hundred's digits of both numbers.

Print the sum of all the digits of the number
whose sum of one's and hundred's digits is bigger.

Testcase:
Input: 856, 978
Output: 24

Input: 128, 365
Output: 11
"""
a, b = map(int, input().split())
sum_a = (a % 10) + (a // 100)
sum_b = (b % 10) + (b // 100)
if sum_a > sum_b:
    n = a
else:
    n = b
ones = n % 10
tens = (n // 10) % 10
hundreds = n // 100
print(ones + tens + hundreds)