"""
Problem 27

Question:
Get a three-digit number from user.
If the sum of the digits is 10 then print
"Success", otherwise print "Failure".

Testcase:
Input: 956
Output: Failure

Input: 127
Output: Success
"""
n = int(input())
a = n // 100
b = (n // 10) % 10
c = n % 10
if a + b + c == 10:
    print("Success")
else:
    print("Failure")