"""
Problem 24

Question:
Get a three-digit number from user and subtract 5
from that number if one's digit and hundred's digit
are the same, then print the result.

Do not use "if".

Testcase:
Input: 595
Output: 590

Input: 372
Output: 372
"""
n = int(input())
ones = n % 10
hundreds = n // 100
print(n - 5 * (ones == hundreds))