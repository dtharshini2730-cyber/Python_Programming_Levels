"""
Question 48:
Adjust the carry in an integer array. Convert a two-digit
number into a single digit and add the carry to the previous position.
"""

a = list(map(int, input("Enter array: ").split()))

for i in range(len(a) - 1, 0, -1):
    if a[i] >= 10:
        carry = a[i] // 10
        a[i] = a[i] % 10
        a[i - 1] = a[i - 1] + carry

print(*a)