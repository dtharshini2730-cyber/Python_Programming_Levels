"""
Question 49:
Write a function to convert an integer array into a
character array and print it.
"""

def convert(a):
    for i in a:
        print(i, end="")

a = list(map(int, input("Enter array: ").split()))

convert(a)