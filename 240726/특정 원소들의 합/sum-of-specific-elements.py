arr = [list(map(int, input().split())) for _ in range(4)]

sum_val = 0
for i in range(4):
    for j in range(4):
        if (i < 3 and j < 3) or (i == 3 and j >= 1):
            sum_val += arr[i][j]

print(sum_val)