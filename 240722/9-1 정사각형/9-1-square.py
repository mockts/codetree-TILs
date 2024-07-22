n = int(input())

for i in range(n):
    for j in range(n):
        print(9 - (i * n + j) % 9, end='')
    print()