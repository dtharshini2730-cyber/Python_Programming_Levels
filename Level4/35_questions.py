"""
Question 35:
Get two numbers from the user and find their LCM.
"""

a, b = map(int, input("Enter two numbers: ").split())

for i in range(1, a * b + 1):
    if i % a == 0 and i % b == 0:
        print(i)
        break