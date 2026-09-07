"""
Question 5:
Get a number from user and count the number of zeros in that number.
"""

n = input("Enter number: ")

count = 0

for i in n:
    if i == '0':
        count = count + 1

print(count)