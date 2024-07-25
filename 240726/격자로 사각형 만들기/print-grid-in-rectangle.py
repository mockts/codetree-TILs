n = int(input())

arr = [[0] * n for i in range(n)]

for i in range(n):
    arr[i][0] = 1
for j in range(n):
    arr[0][j] = 1

for i in range(1, n):
    for j in range(1, n):
        arr[i][j] = arr[i-1][j] + arr[i][j-1] + arr[i-1][j-1]

for row in arr:
    print(" ".join(map(str, row)))