a, b = map(int, input().split())

for i in range(1, a + 1):
    for j in range(1, b + 1):
        if j == b:
            print(i * j)
        else:
            print(i * j, end=" ")