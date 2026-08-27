"""
Problem 28

Question:
Get a three-digit number from user.
If the sum of the one's digit and hundred's digit
is less than 10, then print "Success",
otherwise print "Failure".

Testcase:
Input: 569
Output: Failure

Input: 316
Output: Success
"""
"""
Problem 28

Get a three-digit number from user.
If the sum of the one's digit and hundred's digit
is less than 10, print "Success",
otherwise print "Failure".
"""

n = int(input())
a = n // 100
b = n % 10
if a + b < 10:
    print("Success")
else:
    print("Failure")