n = int(input())
start_num = 11
for i in range(n):
    for j in range(n):
        print(start_num + 2 * (i + j), end=' ')
    print()