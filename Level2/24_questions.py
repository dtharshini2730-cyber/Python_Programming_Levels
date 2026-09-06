"""
Question 24:
Write a program to get a number from the user and print
the total number of two-digit perfect square numbers
in the number.
"""

n = input("Enter number: ")

count = 0

for i in range(len(n) - 1):
    x = int(n[i:i+2])

    if x == 16 or x == 25 or x == 36 or x == 49 or x == 64 or x == 81:
        count = count + 1

print(count)