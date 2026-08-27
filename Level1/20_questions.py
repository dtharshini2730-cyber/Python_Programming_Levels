"""
Problem 20

Question:
Get a three-digit number from user and make
the ten's digit as 0, then print it.

Testcase:
Input: 695
Output: 605

Input: 182
Output: 102
"""
n = int(input())
hundreds = n // 100
ones = n % 10
print(hundreds * 100 + ones)