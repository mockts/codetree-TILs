arr = [input().split() for i in range(5)]

for row in arr:
    for j in range(3):
        row[j] = row[j].upper()
    print(" ".join(row))