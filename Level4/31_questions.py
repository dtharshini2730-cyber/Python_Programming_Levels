"""
Question 31:
Print the number of zeroes encountered between 0 and 1000.
"""

count = 0

for i in range(1, 1001):
    n = str(i)

    for digit in n:
        if digit == '0':
            count = count + 1

print(count)