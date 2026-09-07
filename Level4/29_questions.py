"""
Question 29:
Print the largest four-digit prime number.
"""

for i in range(9999, 999, -1):
    prime = True

    for j in range(2, i):
        if i % j == 0:
            prime = False
            break

    if prime:
        print(i)
        break