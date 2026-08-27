"""
Problem 30

Question:
Get a four-digit number from user.
If the sum of the ten's digit and hundred's digit
is equal to 10, and one of the digits is more than 7,
then print "Success", otherwise print "Failure".

Testcase:
Input: 4649
Output: Failure

Input: 9286
Output: Success
"""
n = int(input())
a = (n // 100) % 10
b = (n // 10) % 10
if a + b == 10 and (a > 7 or b > 7):
    print("Success")
else:
    print("Failure")