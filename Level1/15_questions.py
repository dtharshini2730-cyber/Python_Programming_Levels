"""
Problem 15

Question:
Get a four-digit number from user and only reverse
the first two digits of the number, then print
the number.

Testcase:
Input: 9561
Output: 9516

Input: 3859
Output: 3895
"""
n = int(input())
ones = n % 10
tens = (n // 10) % 10
hundreds = (n // 100) % 10
thousands = n // 1000
print(thousands * 1000 + hundreds * 100 + ones * 10 + tens)