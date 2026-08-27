"""
Problem 16

Question:
Get a four-digit number from user and only reverse
the last two digits of the number, then print
the number.

Testcase:
Input: 9561
Output: 5961

Input: 3859
Output: 8359
"""
n = int(input())
thousands =  n // 1000
hundreds = (n // 100) % 10
tens = (n // 10) % 10
ones = n % 10
print(hundreds * 1000 + thousands * 100 + tens * 10 + ones)