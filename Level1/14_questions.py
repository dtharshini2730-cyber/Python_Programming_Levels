"""
Problem 14

Question:
Get a three-digit number from user and print
the reverse of the number.

Testcase:
Input: 561
Output: 165

Input: 859
Output: 958
"""
n = int(input())
ones = n % 10
tens = (n // 10) % 10
hundreds = n // 100
print(ones * 100 + tens * 10 + hundreds)