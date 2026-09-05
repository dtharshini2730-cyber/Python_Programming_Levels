"""
Problem 33

Question:
Get two 2-digit numbers from user.
Print the sum of digits of the biggest number.

Testcase:
Input: 56, 78
Output: 15

Input: 14, 65
Output: 11
"""
a, b = map(int, input().split())
if a > b:
    big = a
else:
    big = b
print(big // 10 + big % 10)