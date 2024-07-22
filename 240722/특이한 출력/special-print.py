n = int(input())

for x in range(1, n + 1):
    for y in range(1, n + 1):
        print(f"({x}, {y})", end=' ')
        if (x + y) % 4 == 0:
            print()
    if (x + y) % 4 != 0:
        print()