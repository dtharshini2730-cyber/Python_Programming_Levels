"""
Question 27:
Print the largest three-digit prime number.
"""

for i in range(999, 99, -1):
    prime = True

    for j in range(2, i):
        if i % j == 0:
            prime = False
            break

    if prime:
        print(i)
        break