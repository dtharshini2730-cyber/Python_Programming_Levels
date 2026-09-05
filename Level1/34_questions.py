"""
Problem 34

Question:
Get two 3-digit numbers from user.
Print the difference between the one's digit
and hundred's digit of the number whose ten's
digit is bigger than the other number's ten's digit.

Testcase:
Input: 856, 978
Output: 1

Input: 128, 365
Output: 2
"""
a, b = map(int, input().split())
tens_a = (a // 10) % 10
tens_b = (b // 10) % 10
if tens_a > tens_b:
    n = a
else:
    n = b
ones = n % 10
hundreds = n // 100
print(abs(ones - hundreds))