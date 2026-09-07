"""
Question 47:
Add two integer arrays of up to 50 digits and store
the result in a 51-digit array.
"""

a = list(map(int, input("Enter first array: ").split()))
b = list(map(int, input("Enter second array: ").split()))

c = []

for i in range(len(a)):
    c.append(a[i] + b[i])

print(c)