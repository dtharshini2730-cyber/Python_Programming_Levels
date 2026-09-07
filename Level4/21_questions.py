"""
Question 21:
Write a program to print the total number of two-digit
prime numbers.
"""

count = 0

for i in range(10, 100):
    prime = True

    for j in range(2, i):
        if i % j == 0:
            prime = False
            break

    if prime:
        count = count + 1

print(count)