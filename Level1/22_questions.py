"""
Problem 22

Question:
Get a number from user and subtract 5 from that
number if the number's ten's position digit is odd,
then print the result.

Do not use "if".

Testcase:
Input: 685
Output: 685

Input: 89172
Output: 89167
"""
n = int(input())
tens = (n // 10) % 10
print(n - 5 * (tens % 2))