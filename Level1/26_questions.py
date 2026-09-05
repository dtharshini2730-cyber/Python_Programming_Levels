"""
Problem 26

Question:
Get a two-digit number from user.
If the sum of the digits is 10 then print
"Success", otherwise print "Failure".

Testcase:
Input: 56
Output: Failure

Input: 37
Output: Success
"""
n = int(input())
a = n // 10
b = n % 10
if a + b == 10:
    print("Success")
else:
    print("Failure")