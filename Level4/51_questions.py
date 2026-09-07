"""
Question 51:
Get a string and a character from the user. Find all positions
where the character is present and print them.
"""

s = input("Enter string: ")
ch = input("Enter character: ")

for i in range(len(s)):
    if s[i] == ch:
        print(i + 1, end=" ")