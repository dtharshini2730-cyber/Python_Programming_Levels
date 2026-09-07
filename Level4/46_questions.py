"""
Question 46:
Get a number string up to 50 digits and convert it
into an integer array.
"""

s = input("Enter number: ")

a = []

for i in s:
    a.append(int(i))

print(a)