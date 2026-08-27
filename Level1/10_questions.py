"""
Problem 10

Question:
Get a three-digit number from user and print
the ten's digit.

Testcase:
Input: 456
Output: 5

Input: 569
Output: 6
"""
n = int(input())
print((n // 10) % 10)