"""
Question 34:
Print the total number of palindrome numbers less than 100000.
"""

count = 0

for i in range(1, 100000):
    n = str(i)

    if n == n[::-1]:
        count = count + 1

print(count)