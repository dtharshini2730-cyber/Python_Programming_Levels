"""
Question 33:
Print the total number of non-decreasing numbers from
1000 to 9999.
"""

count = 0

for i in range(1000, 10000):
    n = str(i)

    if n[0] <= n[1] <= n[2] <= n[3]:
        count = count + 1

print(count)