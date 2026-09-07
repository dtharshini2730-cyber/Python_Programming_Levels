"""
Question 22:
Write a program to print the total number of three-digit
prime numbers.
"""

count = 0

for i in range(100, 1000):
    prime = True

    for j in range(2, i):
        if i % j == 0:
            prime = False
            break

    if prime:
        count = count + 1

print(count)