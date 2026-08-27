"""
Problem 11

Question:
Get a two-digit number from user and print
the sum of the digits.

Testcase:
Input: 56
Output: 11

Input: 69
Output: 15
"""
n = int(input())
ones = n % 10
tens = (n // 10)
print (ones + tens)