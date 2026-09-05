"""
Problem 29

Question:
Get a four-digit number from user.
If the sum of the ten's digit and hundred's digit
is greater than 10, then print "Success",
otherwise print "Failure".

Testcase:
Input: 7529
Output: Failure

Input: 9386
Output: Success
"""
n = int(input())
a = (n // 100) % 10
b = (n // 10) % 10
if a + b > 10:
    print("Success")
else:
    print("Failure")