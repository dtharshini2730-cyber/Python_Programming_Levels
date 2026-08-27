"""
Problem 13

Question:
Get a two-digit number from user and print
the reverse of the number.

Testcase:
Input: 56
Output: 65

Input: 59
Output: 95
"""
n = int(input())
ones = n % 10
tens = n // 10

print(ones * 10 + tens)