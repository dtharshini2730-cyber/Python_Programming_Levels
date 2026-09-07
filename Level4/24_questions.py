"""
Question 24:
Write a program to print the sum of all two-digit
prime numbers.
"""

sum = 0

for i in range(10, 100):
    prime = True

    for j in range(2, i):
        if i % j == 0:
            prime = False
            break

    if prime:
        sum = sum + i

print(sum)