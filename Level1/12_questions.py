"""
Problem 12

Question:
Get a three-digit number from user and print
the sum of the digits.

Testcase:
Input: 562
Output: 13

Input: 469
Output: 19
"""

n = int(input())
ones = n % 10
tens = (n // 10) % 10
hundreds = n // 100
print(ones + tens + hundreds)