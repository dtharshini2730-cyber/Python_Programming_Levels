"""
Problem 18

Question:
Get a two-digit number from user and make
the ten's digit 1, then print it.

Testcase:
Input: 95
Output: 15

Input: 82
Output: 12
"""
n = int(input())
print(10 + (n % 10))