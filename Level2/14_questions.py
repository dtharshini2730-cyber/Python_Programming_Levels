"""
Question 14:
Write a program to get a number from the user and interchange
the first and last digits, then print the result.
"""

n = input("Enter number: ")

result = n[-1] + n[1:-1] + n[0]

print(result)