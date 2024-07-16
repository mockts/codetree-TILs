n = int(input())

count_non_friendly = 0

for i in range(1, n + 1):
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
        count_non_friendly += 1

print(count_non_friendly)