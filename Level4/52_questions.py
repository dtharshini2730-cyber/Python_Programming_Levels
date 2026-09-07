"""
Question 52:
Get a main string and a substring. Check whether the substring
is present in the main string and print its position.
"""

s = input("Enter main string: ")
sub = input("Enter substring: ")

print(s.find(sub) + 1)