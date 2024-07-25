n, m = map(int, input().split())

arr1 = [[int(x) for x in input().split()] for _ in range(n)]
arr2 = [[int(x) for x in input().split()] for _ in range(n)]

result = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr1[i][j] == arr2[i][j]:
            result[i][j] = 0
        else:
            result[i][j] = 1

for i in range(n):
    for j in range(m):
        print(result[i][j], end=' ')
    print()