"""
Question 32:
Print the total number of prime numbers below 1,000,000
whose sum of digits is equal to 14.
"""

count = 0

for i in range(2, 1000000):
    sum = 0
    n = i

    while n > 0:
        sum = sum + n % 10
        n = n // 10

    if sum == 14:
        prime = True

        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                prime = False
                break

        if prime:
            count = count + 1

print(count)