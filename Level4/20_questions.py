"""
Question 20:
Write a program to print the total number of single-digit
prime numbers.
"""

count = 0

for i in range(2, 10):
    prime = True

    for j in range(2, i):
        if i % j == 0:
            prime = False

    if prime:
        count = count + 1

print(count)