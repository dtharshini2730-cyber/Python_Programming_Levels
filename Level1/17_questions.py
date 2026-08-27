"""
Problem 17

Question:
Get a two-digit number from user and make
the one's digit as 0, then print it.

Testcase:
Input: 95
Output: 90

Input: 18
Output: 10
"""
n = int(input())
print(n // 10 * 10)