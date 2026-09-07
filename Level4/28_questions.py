"""
Question 28:
Print the smallest four-digit prime number.
"""

for i in range(1000, 10000):
    prime = True

    for j in range(2, i):
        if i % j == 0:
            prime = False
            break

    if prime:
        print(i)
        break